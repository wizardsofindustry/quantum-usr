"""Environment variables specified by the application Quantumfile."""
import os

import yaml


DEFAULT_SECRET_KEY = "30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460"

# Set up some variables serving as hints to the Quantum framework.
os.environ['SQ_ENVIRON_PREFIX'] = 'USR'


# This is a hook to load secrets or other environment variables
# from YAML-encoded file, for example when using Docker Swarm
# secrets.
if os.getenv('USR_SECRETS'):
    with open(os.getenv('USR_SECRETS')) as f:
        secrets = yaml.safe_load(f.read()) #pylint: disable=invalid-name
    for key, value in secrets.items():
        if not key.startswith('USR'):
            continue
        os.environ[key] = str(value)

    del secrets


# Provide some defaults to the environment prior to assigning the
# module-level constants.
os.environ.setdefault('USR_SECRET_KEY',
    "30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460")
os.environ.setdefault('USR_DEBUG',
    "1")
os.environ.setdefault('USR_IOC_DEFAULTS',
    "/etc/usr/ioc.conf")
os.environ.setdefault('USR_IOC_DIR',
    "/etc/usr/ioc.conf.d/")
os.environ.setdefault('USR_RDBMS_DSN',
    "postgresql+psycopg2://usr:usr@rdbms:5432/usr")
os.environ.setdefault('USR_HTTP_ADDR',
    "0.0.0.0")
os.environ.setdefault('USR_HTTP_PORT',
    "8443")


SECRET_KEY = os.getenv('USR_SECRET_KEY')
DEBUG = os.getenv('USR_DEBUG', '').lower() in ('yes', '1', 'true')
IOC_DEFAULTS = os.getenv('USR_IOC_DEFAULTS')
IOC_DIR = os.getenv('USR_IOC_DIR')
RDBMS_DSN = os.getenv('USR_RDBMS_DSN')
HTTP_ADDR = os.getenv('USR_HTTP_ADDR')
HTTP_PORT = os.getenv('USR_HTTP_PORT')
DEPLOYMENT_ENV = os.getenv('QUANTUM_DEPLOYMENT_ENV') or 'production'
CONFIG_DIR = os.getenv('QUANTUM_CONFIG_DIR')
TEST_PHASE = os.getenv('SQ_TESTING_PHASE')
