#aqui se crea la session de la base de datos
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import settings # nos traemos los datos del archivo config.py de core

engine = create_engine(settings.DATABASE_URL) # creamos el motor de la base de datos

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # creamos la session local

