import ioc
from sq.readmodel import Finder


class BaseSubjectFinder(Finder):
    session = ioc.class_property('DatabaseSessionFactory')

    def by(self, principals):
        raise NotImplementedError("Subclasses must override this method.")

    def by_email(self, email):
        raise NotImplementedError("Subclasses must override this method.")

    def by_x509_fingerprint(self, fingerprint):
        raise NotImplementedError("Subclasses must override this method.")

    def by_x509_distinguished_names(self, names):
        raise NotImplementedError("Subclasses must override this method.")

    def by_x509_keyid(self, keyid):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
