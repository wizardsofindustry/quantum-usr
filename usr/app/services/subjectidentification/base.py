import ioc
from sq.exceptions import ObjectDoesNotExist
from sq.service import Service


class BaseSubjectIdentificationService(Service):
    finder = ioc.class_property('SubjectFinder')

    SubjectDoesNotExist = type('SubjectDoesNotExist', (ObjectDoesNotExist,), {})

    def identify(self):
        raise NotImplementedError("Subclasses must override this method.")

    def identify_x509(self):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
