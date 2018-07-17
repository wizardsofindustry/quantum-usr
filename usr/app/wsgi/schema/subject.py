"""The validation schema for ``#/components/schema/Subject`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class Subject(sq.schema.Schema):
    """The agent identified by one or more Principals.
    """

    #: The Global Subject Identifier (GSID), uniquely identifying a
    #: Subject within a single Quantum system.
    gsid = sq.schema.fields.UUID(
        required=True,
        allow_none=False
    )


#pylint: skip-file
