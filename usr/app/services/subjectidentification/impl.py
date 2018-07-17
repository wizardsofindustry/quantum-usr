from .base import BaseSubjectIdentificationService


class SubjectIdentificationService(BaseSubjectIdentificationService):

    def identify(self):
        raise NotImplementedError("Subclasses must override this method.")

    def identify_x509(self):
        raise NotImplementedError("Subclasses must override this method.")
