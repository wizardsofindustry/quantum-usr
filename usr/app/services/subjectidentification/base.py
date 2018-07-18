import ioc
from sq.exceptions import ObjectDoesNotExist
from sq.service import Service
from sq.exceptions import UnprocessableEntity


class BaseSubjectIdentificationService(Service):
    finder = ioc.class_property('SubjectFinder')

    SubjectDoesNotExist = type('SubjectDoesNotExist', (ObjectDoesNotExist,), {})
    InvalidPrincipalType = type('InvalidPrincipalType', (UnprocessableEntity,), {})

    def identify(self, principal):
        raise NotImplementedError("Subclasses must override this method.")

    def identify_x509(self, crt):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
