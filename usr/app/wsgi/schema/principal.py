"""The validation schema for ``#/components/schema/Principal`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema

from .x509principal import X509Principal


class Principal(sq.schema.Schema):
    """Represents an identity of a Subject.
    """

    #: Specifies the concrete type of Principal.
    type = sq.schema.fields.String(
        required=True,
        allow_none=False
    )

    __oneof__ = [
        X509Principal
    ]


#pylint: skip-file
