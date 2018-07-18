from .base import BaseSubjectIdentificationService


class SubjectIdentificationService(BaseSubjectIdentificationService):

    def identify(self):
        """Identify a Subject using the given Principal object."""
        raise NotImplementedError("Subclasses must override this method.")

    def identify_x509(self):
        """Identify a Subject using the Issuer Distinguished Name (DN) and
        Subject DN, email address and certificate fingerprint.
        """
        raise NotImplementedError("Subclasses must override this method.")
