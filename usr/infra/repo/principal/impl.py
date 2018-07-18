"""Declares :class:`PrincipalRepository`."""
import re

from ...orm import CertificateFingerprint
from ...orm import CertificateKeyIdentifier
from ...orm import CertificateNames
from ...orm import EmailAddress
from .base import BasePrincipalRepository


class PrincipalRepository(BasePrincipalRepository):
    """Knows how to persist domain data to the persistent storage
    backend.
    """

    def persist(self, dto):
        """Persists an association of a Principal to a Subject."""
        if dto.type not in self.allowed_types:
            raise TypeError(f"Invalid storage class: {dto.type}")
        storage_class = re.sub('[\\:\\.]', '_', dto.pop('type'))
        func = getattr(self, f'persist_{storage_class}')
        func(**dto)
        self.session.flush()

    def persist_email(self, gsid, email):
        """Persists an association of an RFC822 email address to a Subject."""
        self.session.add(EmailAddress(gsid=gsid, email=email))

    def persist_x509_distinguished_names(self, gsid, names):
        """Persists an association of a Issuer DN/Subject DN combination to a
        Subject.
        """
        issuer, subject = names
        self.session.add(
            CertificateNames(gsid=gsid, issuer=issuer, subject=subject))

    def persist_x509_fingerprint(self, gsid, fingerprint):
        """Persists an association of a X.509 certificate fingerprint to a
        Subject.
        """
        self.session.add(CertificateFingerprint(gsid=gsid, fingerprint=fingerprint))

    def persist_x509_keyid(self, gsid, keyid):
        self.session.add(CertificateKeyIdentifier(gsid=gsid, keyid=keyid))

    allowed_types = [
        'x509.distinguished_names',
        'x509.fingerprint',
        'x509.keyid',
        'email'
    ]
