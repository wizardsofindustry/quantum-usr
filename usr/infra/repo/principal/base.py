from sq.persistence import Repository


class BasePrincipalRepository(Repository):

    def persist(self, dto):
        raise NotImplementedError("Subclasses must override this method.")

    def persist_email(self, gsid, email):
        raise NotImplementedError("Subclasses must override this method.")

    def persist_x509_distinguished_name(self, gsid, distinguished_name):
        raise NotImplementedError("Subclasses must override this method.")

    def persist_x509_fingerprint(self, gsid, fingerprint):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
