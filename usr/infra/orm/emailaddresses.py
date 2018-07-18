""""Declares a Python object mapping to the ``emailaddresses`` relation."""
import sq.ext.rdbms.types
import sqlalchemy

from .base import Relation


class EmailAddress(Relation):
    """Maps email addresses to Subjects using the Global Subject
    Identifier (GSID).
    """

    __tablename__ = 'emailaddresses'

    #: Specifies the Global Subject Identifier (GSID), uniquely
    #: identifying a Subject within the boundaries of a Quantum system.
    gsid = sqlalchemy.Column(
        sq.ext.rdbms.types.UUID,
        name='gsid',
        nullable=False
    )

    #: The email address that resolves to the `gsid`.
    email = sqlalchemy.Column(
        sqlalchemy.String,
        name='email',
        primary_key=True,
        nullable=False
    )


# pylint: skip-file
