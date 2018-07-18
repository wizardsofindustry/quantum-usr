from sqlalchemy.orm.exc import NoResultFound

from ...orm import EmailAddress
from .base import BaseSubjectFinder


class SubjectFinder(BaseSubjectFinder):

    def by(self, principals=None):
        """Resolve a list of Principal objects to a Global Subject Identifier
        (GSID).
        """
        results = []
        seen = set()
        for p in (principals or []):
            principal_type = re.sub('[\.\:]', '_', p.pop('type'))
            attname = f'by_{principal_type}'
            if not hasattr(self, attname):
                continue
            try:
                principal = getattr(self, attname)(p)
            except NoResultFound:
                continue

            # Only append the result if the gsid is not already seen.
            if principal is None or principal.gsid in seen:
                continue
            results.append(principal)

        return results

    def by_email(self, email):
        """Resolve a Subject by email address."""
        dao = self.session.query(EmailAddress)\
            .filter(EmailAddress.email==email)\
            .one()
        return self.dto({
            'type': 'email',
            'gsid': dao.gsid.hex,
        })

    def by_x509_fingerprint(self):
        """Resolve a Subject by using the fingerprint of a X.509 certificate,
        issued by a trused Certification Authority (CA).
        """
        raise NotImplementedError("Subclasses must override this method.")

    def by_x509_distinguished_names(self):
        """Resolve a Subject using the Distinguished Names (DNs) of the Issuer
        and Subject on a X.509 certificate, issued by a trusted Certification
        Authority (CA).
        """
        raise NotImplementedError("Subclasses must override this method.")

    def by_x509_keyid(self):
        """Resolve a Subject using the Subject Key Identifier (SKI) on a X.509
        certificate, issued by a trusted Certification Authority (CA).
        """
        raise NotImplementedError("Subclasses must override this method.")
