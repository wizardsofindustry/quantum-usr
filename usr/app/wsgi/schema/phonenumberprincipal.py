"""The validation schema for ``#/components/schema/PhonenumberPrincipal`` objects,
see ``./etc/openapi.yml``).
"""
import sq.schema


class PhonenumberPrincipal(sq.schema.Schema):
    """An ITU-T E.164 formatted phonenumber to identity the **Subject**.
    """

    #: A string holding an ITU-T E.164 formatted phonenumber.
    phonenumber = sq.schema.fields.Phonenumber(
        required=True,
        allow_none=False
    )


#pylint: skip-file
