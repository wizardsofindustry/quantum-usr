"""Contains the concrete implementation of :class:`BasePrincipalController`."""
from .base import BasePrincipalController


class PrincipalController(BasePrincipalController):
    """Provides a handler function for ``POST`` requests holding a
    **SubjectPrincipalSet** and associates them to the appropriate
    **Subject**.
    """

    async def post(self, request, *args, **kwargs):
        """Deserialize a **SubjectPrincipalSet** from the request payload
        and associate the enclosed **Principals** to the specified
        **Subject**.
        """
        for principal in request.payload.principals:
            self.subject.associate(request.payload.gsid, principal)
        return self.render_to_response({}, status_code=200)
