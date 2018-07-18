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
            attname = f'by_{p.type}'
            if not hasattr(self, attname):
                continue
            principal = getattr(self, attname)(p)

            # Only append the result if the gsid is not already seen.
            if principal is None or principal.gsid in seen:
                continue
            results.append(principal)

        return results

    def by_email(self, dto):
        """Resolve a Subject by email address."""
        return self.session.query(EmailAddress)\
            .filter(EmailAddress.email==dto.email)\
            .first()

    #def by_certificate_fingerprint(self):
    #    raise NotImplementedError("Subclasses must override this method.")

    #def by_distinguished_name(self):
    #    raise NotImplementedError("Subclasses must override this method.")

    #def by_keyid(self):
    #    raise NotImplementedError("Subclasses must override this method.")
