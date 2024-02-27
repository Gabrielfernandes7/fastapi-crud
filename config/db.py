from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import MetaData

from sqlalchemy.ext.declarative import declarative_base

URL_DATABASE = "mysql+pymysql://root:Password272801%23%40!@localhost:3306/fastapidb"

engine = create_engine(URL_DATABASE)

SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False, 
    bind=engine
)

meta = MetaData()
connection = engine.connect()


Base = declarative_base()
