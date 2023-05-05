from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def migrate_database(engine):
    Base.metadata.create_all(engine)    

class ApiToken(Base):
    __tablename__ = "api_tokens"

    token = Column(String(255), primary_key=True)
    user_id = Column(Integer, nullable=False)
