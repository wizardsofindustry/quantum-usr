from werkzeug.routing import Map

from .health import HealthEndpoint
from .version import VersionEndpoint
from .identification import IdentificationEndpoint
from .principal import PrincipalEndpoint


urlpatterns = Map([
    HealthEndpoint.as_rule(),
    VersionEndpoint.as_rule(),
    IdentificationEndpoint.as_rule(),
    PrincipalEndpoint.as_rule(),
])


# !!! SG MANAGED FILE -- DO NOT EDIT -- VERSION:  !!!
