from .base import BaseX509Service


class X509Service(BaseX509Service):

    def principals_from_pem(self):
        """Extract Principals from a X.509 client certificate."""
        raise NotImplementedError("Subclasses must override this method.")

    def email_from_san(self):
        """Extract email addresses from the Subject Alternative Names (SANs)."""
        raise NotImplementedError("Subclasses must override this method.")

    def fingerprint(self):
        """Extract the fingerprint from a X.509 certificate."""
        raise NotImplementedError("Subclasses must override this method.")

    def distinguished_names(self):
        """Return a tuple containing the Issuer Distinguished Name (DN) and the
        Subject DN.
        """
        raise NotImplementedError("Subclasses must override this method.")
