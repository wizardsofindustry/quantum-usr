from .base import BasePrincipalRepository


class PrincipalRepository(BasePrincipalRepository):

    def persist(self, dto):
        """Persists an association of a Principal to a Subject."""
        raise NotImplementedError("Subclasses must override this method.")

    def persist_email(self, gsid, email):
        """Persists an association of an RFC822 email address to a Subject."""
        raise NotImplementedError("Subclasses must override this method.")

    def persist_x509_distinguished_name(self, gsid, distinguished_name):
        """Persists an association of a Issuer DN/Subject DN combination to a
        Subject.
        """
        raise NotImplementedError("Subclasses must override this method.")

    def persist_x509_fingerprint(self, gsid, fingerprint):
        """Persists an association of a X.509 certificate fingerprint to a
        Subject.
        """
        raise NotImplementedError("Subclasses must override this method.")
