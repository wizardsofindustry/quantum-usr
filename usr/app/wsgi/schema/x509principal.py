"""The validation schema for ``#/components/schema/X509Principal`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class X509Principal(sq.schema.Schema):
    """A X.509 certificate identifying a user through the combination of
    Issuer Distinguished Name (DN) and Subject DN, or a Subject
    Altnernative Name (SAN) holding an email address.
    """

    #: A string holding the hex-encoded X.509 certificate in the PEM
    #: format.
    crt = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
