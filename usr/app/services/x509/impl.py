from .base import BaseX509Service


class X509Service(BaseX509Service):

    def principals_from_pem(self):
        raise NotImplementedError("Subclasses must override this method.")

    def email_from_san(self):
        raise NotImplementedError("Subclasses must override this method.")

    def fingerprint(self):
        raise NotImplementedError("Subclasses must override this method.")

    def distinguished_names(self):
        raise NotImplementedError("Subclasses must override this method.")
