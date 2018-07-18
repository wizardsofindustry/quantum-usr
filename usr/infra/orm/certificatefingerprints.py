""""Declares a Python object mapping to the ``certificatefingerprints`` relation."""
import sq.ext.rdbms.types
import sqlalchemy

from .base import Relation


class CertificateFingerprint(Relation):
    """Maps the fingerprint of a X.509 certificate, issued by a trusted
    Certification Authority (CA), to a Global Subject Identifier
    (GSID).
    """

    __tablename__ = 'certificatefingerprints'

    #: Specifies the Global Subject Identifier (GSID), uniquely
    #: identifying a Subject within the boundaries of a Quantum system.
    gsid = sqlalchemy.Column(
        sq.ext.rdbms.types.UUID,
        name='gsid',
        nullable=False
    )

    #: A hex-representation of the certificate fingerprint.
    fingerprint = sqlalchemy.Column(
        sqlalchemy.String,
        name='fingerprint',
        primary_key=True,
        nullable=False
    )


# pylint: skip-file
