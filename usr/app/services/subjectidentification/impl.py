"""Declares service :class:`SubjectIdentificationService`."""
from .base import BaseSubjectIdentificationService


class SubjectIdentificationService(BaseSubjectIdentificationService):
    """Provides an interface to resolve **Principal** objects to a
    Global Subject Identifier (GSID), and to create associations
    between them.
    """

    def associate(self, gsid, principal):
        """Associates Principal `principal` to the Subject identified by
        `gsid`.
        """
        func = self._get_method(principal, 'associate')
        return func(gsid, **principal)

    def associate_x509(self, gsid, crt):
        """Associates the Principals in a X.509 certificate, signed by a trusted
        Certification Authority (CA), to the Subject identified by string
        `gsid`.
        """
        for principal in self.x509.principals_from_pem(bytes.fromhex(crt)):
            dto = self.dto(gsid=gsid, **principal)
            self.repo.persist(dto)

    def associate_phonenumber(self, gsid, phonenumber):
        """Associates a phonenumber to a **Subject**."""
        self.repo.persist(
            self.dto(type='phonenumber', gsid=gsid, phonenumber=phonenumber))

    def identify(self, principal):
        """Identify a Subject using the given Principal object."""
        func = self._get_method(principal, 'identify')
        subjects = func(**principal)
        return subjects

    def identify_x509(self, crt):
        """Identify a Subject using the Issuer Distinguished Name (DN) and
        Subject DN, email address and certificate fingerprint.
        """
        principals = self.x509.principals_from_pem(bytes.fromhex(crt))
        return self.finder.by(principals)

    def identify_phonenumber(self, phonenumber):
        """Identify a **Subject** using an international phonenumber."""
        return self.finder.by(
            [self.dto(type='phonenumber', phonenumber=phonenumber)])

    def _get_method(self, principal, action):
        assert action in ('identify', 'associate')
        principal_type = principal.pop('type', None)
        if principal_type not in self.allowed_methods:
            raise self.UnknownPrincipalType(
                f'Unknown Principal Type: {principal_type}')
        return getattr(self, f'{action}_{principal_type}', None)

    # TODO: Docstring updating messes up the code if this is put at the
    # top of the class.
    allowed_methods = ['x509', 'phonenumber']
