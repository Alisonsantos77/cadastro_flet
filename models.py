from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

CONN = "sqlite:///cadastro.db"

engine = create_engine(CONN, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'Clientes'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    age = Column(Integer())
    
Base.metadata.create_all(engine)