"""Start the main :mod:`usr` application using the
specified command-line parameters.
"""
import argparse
import logging
import os
import sys

import sq.runtime


DEFAULT_SECRET_KEY = "30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460"
SECRET_KEY = os.environ.setdefault('USR_SECRET_KEY', DEFAULT_SECRET_KEY)
os.environ.setdefault('USR_SECRET_KEY', "30b465e0c882f37671cca0f142ec292493c1009c0baa0a39aa684b1259301460")
os.environ.setdefault('USR_RDBMS_DSN', "postgresql+psycopg2://usr:usr@rdbms:5432/usr")


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

    if DEFAULT_SECRET_KEY == SECRET_KEY:
        logger.critical("The application is started using the default secret key.")


    try:
        sys.exit(p.start() or 0)
    except Exception: #pylint: disable=broad-except
        logger.exception("Fatal exception caused program termination")
        sys.exit(1)


# !!! SG MANAGED FILE -- DO NOT EDIT !!!
