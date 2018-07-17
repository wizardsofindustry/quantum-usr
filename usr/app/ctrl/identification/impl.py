"""Contains the concrete implementation of :class:`BaseIdentificationCtrl`."""
from .base import BaseIdentificationCtrl


class IdentificationCtrl(BaseIdentificationCtrl):

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
