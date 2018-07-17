import ioc
from sq.readmodel import Finder


class BaseSubjectFinder(Finder):
    session = ioc.class_property('DatabaseSessionFactory')

    def by(self):
        raise NotImplementedError("Subclasses must override this method.")

    def by_email(self):
        raise NotImplementedError("Subclasses must override this method.")

    def by_certificate_fingerprint(self):
        raise NotImplementedError("Subclasses must override this method.")

    def by_distinguished_name(self):
        raise NotImplementedError("Subclasses must override this method.")

    def by_keyid(self):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
