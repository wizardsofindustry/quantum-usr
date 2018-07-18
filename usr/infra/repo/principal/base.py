import ioc
from sq.persistence import Repository


class BasePrincipalRepository(Repository):
    session = ioc.class_property('DatabaseSessionFactory')

    def persist(self, dto):
        raise NotImplementedError("Subclasses must override this method.")

    def persist_email(self, gsid, email):
        raise NotImplementedError("Subclasses must override this method.")

    def persist_x509_distinguished_names(self, gsid, names):
        raise NotImplementedError("Subclasses must override this method.")

    def persist_x509_fingerprint(self, gsid, fingerprint):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
