"""Contains the concrete implementation of :class:`BaseIdentificationCtrl`."""
from .base import BaseIdentificationCtrl


class IdentificationCtrl(BaseIdentificationCtrl):

    async def post(self, request, *args, **kwargs):
        return self.render_to_response(
            ctx=self.subject.identify(request.payload))
