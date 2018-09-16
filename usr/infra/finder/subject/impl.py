"""Declares :class:`SubjectFinder`."""
import re

from sqlalchemy.orm.exc import NoResultFound

from ...orm import BankIdentificationNumber
from ...orm import CertificateFingerprint
from ...orm import CertificateKeyIdentifier
from ...orm import CertificateNames
from ...orm import EmailAddress
from ...orm import Phonenumber
from .base import BaseSubjectFinder


class SubjectFinder(BaseSubjectFinder):
    """Provides an interface to resolve Principals to Global Subject
    Identifiers (GSIDs).
    """

    def by(self, principals=None):
        """Resolve a list of Principal objects to a Global Subject Identifier
        (GSID).
        """
        results = []
        seen = set()
        for dto in (principals or []):
            principal_type = re.sub('[\\.\\:]', '_', dto.pop('type'))
            attname = f'by_{principal_type}'

            # The handler function is assumed to handle all exception cases, such
            # as no principal existing.
            try:
                principal = getattr(self, attname)(**dto)
            except NoResultFound:
                principal = None

            # Only append the result if the gsid is not already seen.
            if principal is None or principal.gsid in seen:
                continue
            seen.add(principal.gsid)
            results.append(principal)

        return results

    def by_email(self, email):
        """Resolve a Subject by email address."""
        dao = self.session.query(EmailAddress)\
            .filter(EmailAddress.email == email)\
            .one()
        return self.dto({
            'type': 'email',
            'gsid': dao.gsid.hex,
        })

    def by_phonenumber(self, phonenumber):
        """Resolve a Subject by phone number."""
        dao = self.session.query(Phonenumber)\
            .filter(Phonenumber.phonenumber == phonenumber)\
            .one()
        return self.dto({
            'type': 'phonenumber',
            'gsid': dao.gsid.hex,
        })

    def by_idin_bin(self, bin):
        """Resolve a Subject by Bank Identification Number (BIN)."""
        dao = self.session.query(BankIdentificationNumber)\
            .filter(BankIdentificationNumber.bin == bin)\
            .one()
        return self.dto({
            'type': 'idin:bin',
            'gsid': dao.gsid.hex,
        })

    def by_x509_fingerprint(self, fingerprint):
        """Resolve a Subject by using the fingerprint of a X.509 certificate,
        issued by a trused Certification Authority (CA).
        """
        dao = self.session.query(CertificateFingerprint)\
            .filter(CertificateFingerprint.fingerprint == fingerprint)\
            .one()
        return self.dto({
            'type': 'x509.fingerprint',
            'gsid': dao.gsid.hex,
        })

    def by_x509_distinguished_names(self, names):
        """Resolve a Subject using the Distinguished Names (DNs) of the Issuer
        and Subject on a X.509 certificate, issued by a trusted Certification
        Authority (CA).
        """
        dao = self.session.query(CertificateNames)\
            .filter(CertificateNames.issuer == names[0])\
            .filter(CertificateNames.subject == names[1])\
            .one()
        return self.dto({
            'type': 'x509.distinguished_names',
            'gsid': dao.gsid.hex,
        })

    def by_x509_keyid(self, keyid):
        """Resolve a Subject using the SHA-256 hashed public key on a X.509
        certificate, issued by a trusted Certification Authority (CA).
        """
        dao = self.session.query(CertificateKeyIdentifier)\
            .filter(CertificateKeyIdentifier.keyid == keyid)\
            .one()
        return self.dto({
            'type': 'x509.keyid',
            'gsid': dao.gsid.hex,
        })
