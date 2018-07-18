from .base import BaseSubjectFinder


class SubjectFinder(BaseSubjectFinder):

    def by(self, principals=None):
        raise NotImplementedError("Subclasses must override this method.")

    def by_email(self, email):
        raise NotImplementedError("Subclasses must override this method.")

    #def by_certificate_fingerprint(self):
    #    raise NotImplementedError("Subclasses must override this method.")

    #def by_distinguished_name(self):
    #    raise NotImplementedError("Subclasses must override this method.")

    #def by_keyid(self):
    #    raise NotImplementedError("Subclasses must override this method.")
