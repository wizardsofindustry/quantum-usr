"""Contains the concrete implementation of :class:`BaseIdentificationCtrl`."""
from .base import BaseIdentificationCtrl


class IdentificationCtrl(BaseIdentificationCtrl):

    async def post(self, request, *args, **kwargs):
        subject = {'gsid': None}
        principals = self.subject.identify(request.payload)
        if principals:
            if len(principals) > 1:
                raise NotImplementedError
            subject['gsid'] = principals[0].gsid
        return self.render_to_response(ctx=subject)
