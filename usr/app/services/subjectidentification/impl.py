from .base import BaseSubjectIdentificationService


class SubjectIdentificationService(BaseSubjectIdentificationService):

    def identify(self, principal):
        """Identify a Subject using the given Principal object."""
        principal_type = principal.pop('type', None)
        if principal_type is None:
            raise TypeError('Missing `type` attribute.')
        if principal_type not in self.allowed_methods:
            raise self.UnknownPrincipalType(
                f'Unknown Principal Type: {principal_type}')
        func = getattr(self, f'identify_{principal_type}', None)
        if func is None:
            raise self.UnknownPrincipalType(
                f'Unknown Principal Type: {principal_type}')
        return func(**principal)

    def identify_x509(self, crt):
        """Identify a Subject using the Issuer Distinguished Name (DN) and
        Subject DN, email address and certificate fingerprint.
        """
        raise NotImplementedError("Subclasses must override this method.")

    # TODO: Docstring updating messes up the code if this is put at the
    # top of the class.
    allowed_methods = ['x509']
