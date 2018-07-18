"""The validation schema for ``#/components/schema/SubjectPrincipalSet`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema

from .principal import Principal


class SubjectPrincipalSet(sq.schema.Schema):
    """A set of Principals associated to a specific Subject.
    """

    #: The Global Subject Identifier (GSID), uniquely identifying a
    #: Subject within a single Quantum system.
    gsid = sq.schema.fields.UUID(
        required=True,
        allow_none=False
    )

    #: One or many Principals to associate to the Subject identified by
    #: `gsid`.
    principals = sq.schema.fields.Nested(
        nested=Principal(many=True),
        required=True,
        allow_none=False
    )


#pylint: skip-file
