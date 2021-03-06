from sq.service import Service
from sq.exceptions import UnprocessableEntity


class BaseX509Service(Service):

    InvalidCertificate = type('InvalidCertificate', (UnprocessableEntity,), {})

    def principals_from_pem(self, pem):
        raise NotImplementedError("Subclasses must override this method.")

    def email_from_san(self, crt):
        raise NotImplementedError("Subclasses must override this method.")

    def email_from_subject(self, crt):
        raise NotImplementedError("Subclasses must override this method.")

    def fingerprint(self, crt):
        raise NotImplementedError("Subclasses must override this method.")

    def distinguished_names(self, crt):
        raise NotImplementedError("Subclasses must override this method.")

    def keyid(self, crt):
        raise NotImplementedError("Subclasses must override this method.")


# pylint: skip-file
