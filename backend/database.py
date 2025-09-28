"""
Configuração da conexão com o banco de dados (Database Setup).

Este arquivo é responsável por criar o 'engine' de conexão do SQLAlchemy
e a fábrica de sessões que a aplicação usará para interagir com o banco.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão para o banco de dados SQLite local.
SQLALCHEMY_DATABASE_URL = "sqlite:///backend/kanban.db"

# Engine do SQLAlchemy, que gerencia as conexões.
# O argumento `connect_args` é necessário para o SQLite em ambientes multithread.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Fábrica de sessões. Cada instância de `SessionLocal` será uma sessão com o banco.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base para os modelos ORM. Nossas tabelas herdarão dela.
Base = declarative_base()