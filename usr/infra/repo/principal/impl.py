"""Declares :class:`PrincipalRepository`."""
import re

from ...orm import BankIdentificationNumber
from ...orm import CertificateFingerprint
from ...orm import CertificateKeyIdentifier
from ...orm import CertificateNames
from ...orm import EmailAddress
from ...orm import Phonenumber
from .base import BasePrincipalRepository


class PrincipalRepository(BasePrincipalRepository):
    """Knows how to persist domain data to the persistent storage
    backend.
    """

    def persist(self, dto):
        """Persists an association of a Principal to a Subject."""
        assert dto.type in self.allowed_types
        storage_class = re.sub('[\\:\\.]', '_', dto.pop('type'))
        func = getattr(self, f'persist_{storage_class}')
        func(**dto)
        self.session.flush()

    def persist_phonenumber(self, gsid, phonenumber):
        """Persists an association for an ITU-T E.164 international phonenumber
        to a Subject.
        """
        self.session.add(Phonenumber(gsid=gsid, phonenumber=phonenumber))

    def persist_email(self, gsid, email):
        """Persists an association of an RFC822 email address to a Subject."""
        self.session.add(EmailAddress(gsid=gsid, email=email))

    def persist_idin_bin(self, gsid, bin):
        """Persists an association of a Bank Identification Number (BIN), used
        in the iDIN authentication scheme, to a Subject.
        """
        self.session.add(BankIdentificationNumber(gsid=gsid, bin=bin))

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
        """Persists an association of a SHA-256 public key to a Subject."""
        self.session.add(CertificateKeyIdentifier(gsid=gsid, keyid=keyid))

    allowed_types = [
        'x509.distinguished_names',
        'x509.fingerprint',
        'x509.keyid',
        'email',
        'phonenumber',
        'idin:bin'
    ]
