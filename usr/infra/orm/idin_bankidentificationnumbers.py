""""Declares a Python object mapping to the ``idin_bankidentificationnumbers`` relation."""
import sq.ext.rdbms.types
import sqlalchemy

from .base import Relation


class BankIdentificationNumber(Relation):
    """Maps Bank Identification Numbers (BINs) to Subjects using the
    Global Subject Identifier (GSID).
    """

    __tablename__ = 'idin_bankidentificationnumbers'

    #: Specifies the Global Subject Identifier (GSID), uniquely
    #: identifying a Subject within the boundaries of a Quantum system.
    gsid = sqlalchemy.Column(
        sq.ext.rdbms.types.UUID,
        name='gsid',
        nullable=False
    )

    #: The BIN that resolves to the `gsid`.
    bin = sqlalchemy.Column(
        sqlalchemy.String,
        name='bin',
        primary_key=True,
        nullable=False
    )


# pylint: skip-file
