import ioc
from sq.exceptions import ObjectDoesNotExist
from sq.service import Service
from sq.exceptions import UnprocessableEntity
from sq.exceptions import UnprocessableEntity


class BaseSubjectIdentificationService(Service):
    finder = ioc.class_property('SubjectFinder')
    x509 = ioc.class_property('X509Service')
    repo = ioc.class_property('PrincipalRepository')

    SubjectDoesNotExist = type('SubjectDoesNotExist', (ObjectDoesNotExist,), {})
    InvalidPrincipalType = type('InvalidPrincipalType', (UnprocessableEntity,), {})
    MultipleSubjectsReturned = type('MultipleSubjectsReturned', (LookupError,), {})
    UnknownPrincipalType = type('UnknownPrincipalType', (UnprocessableEntity,), {})

    def associate(self, gsid, principal):
        raise NotImplementedError("Subclasses must override this method.")

    def associate_x509(self, gsid, crt):
        raise NotImplementedError("Subclasses must override this method.")

    def associate_phonenumber(self, gsid, phonenumber):
        raise NotImplementedError("Subclasses must override this method.")

    def associate_idin_bin(self, gsid, bin):
        raise NotImplementedError("Subclasses must override this method.")

    def identify(self, principal):
        raise NotImplementedError("Subclasses must override this method.")

    def identify_x509(self, crt):
        raise NotImplementedError("Subclasses must override this method.")

    def identify_phonenumber(self, phonenumber):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
