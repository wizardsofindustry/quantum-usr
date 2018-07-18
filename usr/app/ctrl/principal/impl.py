"""Contains the concrete implementation of :class:`BasePrincipalController`."""
from .base import BasePrincipalController


class PrincipalController(BasePrincipalController):

    async def post(self, request, *args, **kwargs):
        raise NotImplementedError("Subclasses must override this method.")
