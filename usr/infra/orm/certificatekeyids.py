""""Declares a Python object mapping to the ``certificatekeyids`` relation."""
import sq.ext.rdbms.types
import sqlalchemy

from .base import Relation


class CertificateKeyIdentifier(Relation):
    """Associates a X.509 certificate public key SHA-256 hash to a Global
    Subject Identifier (GSID).
    """

    __tablename__ = 'certificatekeyids'

    #: Specifies the Global Subject Identifier (GSID), uniquely
    #: identifying a Subject within the boundaries of a Quantum system.
    gsid = sqlalchemy.Column(
        sq.ext.rdbms.types.UUID,
        name='gsid',
        nullable=False
    )

    #: A hex-representation of the SHA-256 hashed certificate public key.
    keyid = sqlalchemy.Column(
        sqlalchemy.String,
        name='keyid',
        primary_key=True,
        nullable=False
    )


# pylint: skip-file
