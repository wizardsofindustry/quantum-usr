"""The validation schema for ``#/components/schema/BankIdentificationNumberPrincipal`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class BankIdentificationNumberPrincipal(sq.schema.Schema):
    """A Bank Identification Number (BIN) returned by the iDIN issuer
    after succesful login dialog.
    """

    #: A string holding the Bank Identification Number (BIN). May be up to
    #: 256 characters.
    bin = sq.schema.fields.String(
        required=True,
        allow_none=False
    )


#pylint: skip-file
