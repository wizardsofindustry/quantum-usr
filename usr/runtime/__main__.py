"""Start the main :mod:`usr` application using the
specified command-line parameters.
"""
import argparse
import logging
import os
import sys

import yaml

import sq.runtime


DEPLOYMENT_ENV = os.getenv('QUANTUM_DEPLOYMENT_ENV') or 'production'

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


os.environ['SQ_ENVIRON_PREFIX'] = 'USR'
DEFAULT_SECRET_KEY = "30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460"
os.environ.setdefault('USR_SECRET_KEY', "30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460")
os.environ.setdefault('USR_DEBUG', "1")
os.environ.setdefault('USR_IOC_DEFAULTS', "/etc/usr/ioc.conf")
os.environ.setdefault('USR_IOC_DIR', "/etc/usr/ioc.conf.d/")
os.environ.setdefault('USR_RDBMS_DSN', "postgresql+psycopg2://usr:usr@rdbms:5432/usr")
os.environ.setdefault('USR_HTTP_ADDR', "0.0.0.0")
os.environ.setdefault('USR_HTTP_PORT', "8443")


class MainProcess(sq.runtime.MainProcess):
    """The main :mod:`usr` process manager."""
    framerate = 10
    components = [
        sq.runtime.HttpServer,
    ]


parser = argparse.ArgumentParser() #pylint: disable=invalid-name
parser.add_argument('-c', dest='config',
    default='./etc/usr.conf',
    help="specifies the runtime configuration file (default: %(default)s)")
parser.add_argument('--loglevel',
    help="specifies the logging verbosity (default: %(default)s)",
    choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'], default='INFO')


if __name__ == '__main__':
    logger = logging.getLogger('usr') #pylint: disable=invalid-name
    args = parser.parse_args() #pylint: disable=invalid-name
    p = MainProcess(args, logger=logger) #pylint: disable=invalid-name

    if DEFAULT_SECRET_KEY == os.getenv('USR_SECRET_KEY'):
        logger.critical("The application is started using the default secret key")
        if DEPLOYMENT_ENV == 'production':
            logger.critical("DEFAULT_SECRET_KEY may not be used in production")
            sys.exit(128)


    try:
        sys.exit(p.start() or 0)
    except Exception: #pylint: disable=broad-except
        logger.exception("Fatal exception caused program termination")
        sys.exit(1)


# !!! SG MANAGED FILE -- DO NOT EDIT !!!
