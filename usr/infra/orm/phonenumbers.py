""""Declares a Python object mapping to the ``phonenumbers`` relation."""
import sq.ext.rdbms.types
import sqlalchemy

from .base import Relation


class Phonenumber(Relation):
    """Maps phonenumbers to Subjects using the Global Subject Identifier
    (GSID).
    """

    __tablename__ = 'phonenumbers'

    #: Specifies the Global Subject Identifier (GSID), uniquely
    #: identifying a Subject within the boundaries of a Quantum system.
    gsid = sqlalchemy.Column(
        sq.ext.rdbms.types.UUID,
        name='gsid',
        nullable=False
    )

    #: The phonenumber that resolves to the `gsid`.
    phonenumber = sqlalchemy.Column(
        sqlalchemy.String,
        name='phonenumber',
        primary_key=True,
        nullable=False
    )


# pylint: skip-file
