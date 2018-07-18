""""Declares a Python object mapping to the ``certificatenames`` relation."""
import sq.ext.rdbms.types
import sqlalchemy

from .base import Relation


class CertificateNames(Relation):
    """Associates a combination of Issuer Distinguished Name (DN) and
    Subject DN to a Global Subject Identifier (GSID).
    """

    __tablename__ = 'certificatenames'

    #: Specifies the Global Subject Identifier (GSID), uniquely
    #: identifying a Subject within the boundaries of a Quantum system.
    gsid = sqlalchemy.Column(
        sq.ext.rdbms.types.UUID,
        name='gsid',
        nullable=False
    )

    #: A hex-representation of a SHA-256 hash of the DER-encoded Issuer
    #: name as included in the X.509 certificate.
    issuer = sqlalchemy.Column(
        sqlalchemy.String,
        name='issuer',
        primary_key=True,
        nullable=False
    )

    #: A hex-representation of a SHA-256 hash of the DER-encoded Subject
    #: name as included in the X.509 certificate.
    subject = sqlalchemy.Column(
        sqlalchemy.String,
        name='subject',
        primary_key=True,
        nullable=False
    )


# pylint: skip-file
