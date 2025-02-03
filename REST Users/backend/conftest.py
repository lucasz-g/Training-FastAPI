import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from backend.main import app
from backend.models import table_registry

# Criar o banco de dados SQLite em memória
engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar as tabelas no banco de dados
table_registry.metadata.create_all(engine)


@pytest.fixture
def client():
    """Cria um cliente de testes para a API"""
    return TestClient(app)


@pytest.fixture
def session():
    """Cria uma sessão do banco de dados para os testes"""
    db = TestingSessionLocal()
    try:
        yield db  # Passa a sessão para os testes
    finally:
        db.close()  # Fecha a sessão após o teste

    # Limpa o banco de dados depois dos testes
    table_registry.metadata.drop_all(engine)