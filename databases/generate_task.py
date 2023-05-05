from sqlalchemy import Column, String, Integer, DateTime, Text, func
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def migrate_database(engine):
    Base.metadata.create_all(engine)    

class GenerateTask(Base):
    __tablename__ = "generate_tasks"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    title = Column(String(1024), nullable=False)
    status = Column(Integer, nullable=False)
    prompt = Column(String(1024), nullable=False)
    negative_prompt = Column(String(1024), nullable=False)
    model_name = Column(String(1024), nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())
    updated_at = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())
