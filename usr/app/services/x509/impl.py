import hashlib

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.x509 import load_pem_x509_certificate
from cryptography.x509 import RFC822Name
from cryptography.x509 import ExtensionOID
from cryptography.x509.extensions import ExtensionNotFound

from .base import BaseX509Service


class X509Service(BaseX509Service):

    def principals_from_pem(self, pem):
        """Extract Principals from a X.509 client certificate."""
        crt = load_pem_x509_certificate(pem, default_backend())
        principals = self.email_from_san(crt)
        """Extract email addresses from the Subject Alternative Names (SANs)."""
        principals.append(self.fingerprint(crt))
        """Extract the fingerprint from a X.509 certificate."""
        principals.append(self.distinguished_names(crt))
        """Return a tuple containing the Issuer Distinguished Name (DN) and the
        Subject DN.
        """
        return principals

    def email_from_subject(self, crt):
        """Extract the email address from the Subject Distinguished Name (DN)"""
        raise NotImplementedError

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
        issuer = crt.issuer.public_bytes(default_backend())
        subject = crt.subject.public_bytes(default_backend())
        return {
            'type': 'x509.distinguished_name',
            'distinguished_name': (
                hashlib.sha256(issuer).hexdigest(),
                hashlib.sha256(subject).hexdigest(),
            )
        }
