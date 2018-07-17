"""Contains the base class for :class:`IdentificationCtrl`."""
import ioc
from sq.ctrl import EndpointCtrl

class BaseIdentificationCtrl(EndpointCtrl):
    """Generated by SG to serve as an abstract base class for:

        usr.app.ctrl.IdentificationCtrl

    This class encapsulates external dependencies (such as the inversion-of-control
    requirements) and specifies the interface for the concrete implementation.
    """
    subject = ioc.class_property('SubjectIdentificationService')

    async def post(self, request, *args, **kwargs):
        """This method specifies the signature for :meth:`IdentificationCtrl.post()`
        and should be implemented in the following file:

            ./usr/ctrl/identification/impl.py
        """
        raise NotImplementedError("Subclasses must override this method.")


#pylint: skip-file
# !!! SG MANAGED FILE -- DO NOT EDIT -- VERSION:  !!!