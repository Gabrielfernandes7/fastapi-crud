from sqlalchemy import Table, Column
from config.db import engine

# types
from sqlalchemy.sql.sqltypes import Integer, String

from config.db import meta

users = Table(
    "users", meta,
    Column("id_user", Integer, primary_key=True),
    Column("name", String(255)),
    Column("email", String(255)),
    Column("password", String(255))
)

meta.create_all(engine)
