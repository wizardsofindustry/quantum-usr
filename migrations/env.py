from logging.config import fileConfig
import os

from alembic import context
from sqlalchemy import create_engine
from sqlalchemy import engine_from_config
from sqlalchemy import pool

import usr.infra.orm


config = context.config
fileConfig(config.config_file_name)
target_metadata = usr.infra.orm.Relation.metadata


def get_dsn():
    """Returns a string containing the Data Source Name (DSN) that
    is used by Alembic to establish a database connection.
    """
    return os.getenv('USR_RDBMS_DSN')


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = get_dsn()
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True)

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = create_engine(get_dsn())
    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()


#pylint: skip-file
