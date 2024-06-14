from sqlalchemy import create_engine,MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database URL for MySQL
DATABASE_URL = "mysql+pymysql://root@localhost:3306/python"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)
metadata = MetaData()
Base = declarative_base()