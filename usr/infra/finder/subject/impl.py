from .base import BaseSubjectFinder


class SubjectFinder(BaseSubjectFinder):

    def by(self, principals=None):
        """Resolve a list of Principal objects to a Global Subject Identifier
        (GSID).
        """
        raise NotImplementedError("Subclasses must override this method.")

    def by_email(self, email):
        """Resolve a Subject by email address."""
        raise NotImplementedError("Subclasses must override this method.")

    #def by_certificate_fingerprint(self):
    #    raise NotImplementedError("Subclasses must override this method.")

    #def by_distinguished_name(self):
    #    raise NotImplementedError("Subclasses must override this method.")

    #def by_keyid(self):
    #    raise NotImplementedError("Subclasses must override this method.")
