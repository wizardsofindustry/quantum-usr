import hashlib

from cryptography.hazmat.primitives.serialization import Encoding
from cryptography.hazmat.primitives.serialization import PublicFormat
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.x509 import load_pem_x509_certificate
from cryptography.x509 import RFC822Name
from cryptography.x509 import ExtensionOID
from cryptography.x509 import NameOID
from cryptography.x509.extensions import ExtensionNotFound

from .base import BaseX509Service


class X509Service(BaseX509Service):

    def principals_from_pem(self, pem):
        crt = load_pem_x509_certificate(pem, default_backend())
        principals = self.email_from_san(crt)
        principals.append(self.fingerprint(crt))
        principals.append(self.distinguished_names(crt))
        principals.append(self.keyid(crt))
        email = self.email_from_subject(crt)
        if email is not None:
            principals.append(email)
        return [self.dto(**p) for p in principals]

    def email_from_subject(self, crt):
        attr = crt.subject.get_attributes_for_oid(NameOID.EMAIL_ADDRESS)
        return {'type': 'email', 'email':attr[0].value}\
            if attr is not None else None

    def email_from_san(self, crt):
        """Extract email addresses from the Subject Alternative Names (SANs)."""
        try:
            ext = crt.extensions.get_extension_for_oid(
                ExtensionOID.SUBJECT_ALTERNATIVE_NAME)
            return [{'type': 'email', 'email': x}
                for x in set(ext.get_values_for_type(RFC822Name))]
        except ExtensionNotFound:
            return []

    def fingerprint(self, crt):
        """Extract the fingerprint from a X.509 certificate."""
        return {
            'type': 'x509.fingerprint',
            'fingerprint': bytes.hex(crt.fingerprint(SHA256()))
        }

    def distinguished_names(self, crt):
        """Return a tuple containing the Issuer Distinguished Name (DN) and the
        Subject DN.
        """
        # TODO: This should actually be implemented in a way so that it is
        # case-insensitive.
        issuer = crt.issuer.public_bytes(default_backend())
        subject = crt.subject.public_bytes(default_backend())
        return {
            'type': 'x509.distinguished_names',
            'names': (
                hashlib.sha256(issuer).hexdigest(),
                hashlib.sha256(subject).hexdigest(),
            )
        }

    def keyid(self, crt):
        """Return the hex-encoded, SHA-256 hashed public key associated
        to the X.509 certificate.
        """
        key = crt.public_key()
        pem = key.public_bytes(
            encoding=Encoding.PEM,
            format=PublicFormat.SubjectPublicKeyInfo
        )
        return {
            'type': 'x509.keyid',
            'keyid': hashlib.sha256(pem).hexdigest()
        }
