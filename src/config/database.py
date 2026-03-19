import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load environment variable
load_dotenv()

username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
ip = os.getenv('IP')
port = os.getenv('PORT_NUMBER')
database = os.getenv('DATABASE')

DATABASE_URL = (
    f"mssql+pyodbc://{username}:{password}@{ip},{port}/"
    f"{database}?driver=ODBC+Driver+17+for+SQL+Server"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
