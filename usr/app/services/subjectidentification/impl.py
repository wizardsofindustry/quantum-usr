from .base import BaseSubjectIdentificationService


class SubjectIdentificationService(BaseSubjectIdentificationService):

    def associate(self, gsid, principal):
        """Associate a principal to a Subject, identified by string `gsid`"""
        func = self._get_method(principal, 'associate')
        return func(gsid, **principal)

    def associate_x509(self, gsid, crt):
        """Associate the Principals contained in a X.509 certificate
        signed by a trusted Certification Authority (CA) to a
        Subject.

        Args:
            gsid (string): a Global Subject Identifier (GSID)
            crt (string): a hex-encoded X.509 certificate in the
                PEM-format.

        Returns:
            None
        """
        for principal in self.x509.principals_from_pem(bytes.fromhex(crt)):
            dto = self.dto(storage_class=principal.type, gsid=gsid, **principal)
            self.repo.persist(dto)

    def identify(self, principal):
        """Identify a Subject using the given Principal object."""
        func = self._get_method(principal, 'identify')
        return func(**principal)

    def identify_x509(self, crt):
        """Identify a Subject using the Issuer Distinguished Name (DN) and
        Subject DN, email address and certificate fingerprint.
        """
        principals = self.x509.principals_from_pem(bytes.fromhex(crt))
        subjects = self.finder.by(principals)
        if len(subjects) > 1:
            raise self.MultipleSubjectsReturned
        return subjects

    def _get_method(self, principal, action):
        assert action in ('identify', 'associate')
        principal_type = principal.pop('type', None)
        if principal_type is None:
            raise TypeError('Missing `type` attribute.')
        if principal_type not in self.allowed_methods:
            raise self.UnknownPrincipalType(
                f'Unknown Principal Type: {principal_type}')
        func = getattr(self, f'{action}_{principal_type}', None)
        if func is None:
            raise self.UnknownPrincipalType(
                f'Unknown Principal Type: {principal_type}')
        return func

    # TODO: Docstring updating messes up the code if this is put at the
    # top of the class.
    allowed_methods = ['x509']
