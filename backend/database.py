from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL de conexão com o banco de dados SQLite local
SQLALCHEMY_DATABASE_URL = "sqlite:///backend/kanban.db"

# Engine: gerencia pool de conexões síncronas que podem trabalhar em paralelo
# Permite que o FastAPI (assíncrono) delegue tarefas para múltiplas conexões simultâneas
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Fábrica de sessões: cria instâncias para interagir com o banco de dados
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Modelo base para as tabelas do banco de dados
Base = declarative_base()