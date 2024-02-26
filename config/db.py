from sqlalchemy import create_engine
from sqlalchemy import MetaData

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:Password272801%23%40!@localhost:3306/fastapidb")

meta = MetaData()
connection = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()