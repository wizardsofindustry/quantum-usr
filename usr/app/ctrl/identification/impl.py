"""Contains the concrete implementation of :class:`BaseIdentificationCtrl`."""
from .base import BaseIdentificationCtrl


class IdentificationCtrl(BaseIdentificationCtrl):
    """Deserializes a **Principal** from the request payload and resolves
    it to a Global Subject Identifier (GSID).
    """

    async def post(self, request, *args, **kwargs):
        subject = {'gsid': None}
        status = 200
        principals = []
        try:
            principals = self.subject.identify(request.payload)
        except self.subject.UnknownPrincipalType:
            status = 404
        if principals:
            if len(principals) > 1:
                raise NotImplementedError
            subject['gsid'] = principals[0].gsid
        return self.render_to_response(ctx=subject, status_code=status)
