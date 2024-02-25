from sqlalchemy import create_engine
from sqlalchemy import MetaData

engine = create_engine("mysql+pymysql://root@localhost:3306/fastapidb")

meta = MetaData()
connection = engine.connect()
