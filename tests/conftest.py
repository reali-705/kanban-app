import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend import app, Base, get_db

# Cria engine e sessão para banco em memória (compartilhado)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine_teste = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine_teste)

def get_db_temporario():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="function", autouse=True)
def preparar_db_temporario():
    # Cria as tabelas antes de cada teste
    Base.metadata.create_all(bind=engine_teste)
    yield
    # Remove as tabelas após cada teste
    Base.metadata.drop_all(bind=engine_teste)

@pytest.fixture(scope="function")
def cliente():
    app.dependency_overrides[get_db] = get_db_temporario
    with TestClient(app) as cliente:
        yield cliente
    app.dependency_overrides = {}