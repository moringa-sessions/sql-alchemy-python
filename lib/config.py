from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship,joinedload
from models import Base, User, Post

# Set up SQLite database engine
engine = create_engine("sqlite:///database.sqlite")

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()