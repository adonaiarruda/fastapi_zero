from contextlib import contextmanager
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
from sqlalchemy.orm import Session

from fastapi_zero.app import app
from fastapi_zero.models import table_registry


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine(
        "sqlite:///:memory:"
    )  # liga a conexão com o banco de dados
    table_registry.metadata.create_all(engine)  # cria a tabela do teste

    with Session(engine) as session:  # cria a session para o teste
        yield session  # retorna a session para o teste executar o teste

    table_registry.metadata.drop_all(engine)  # deleta a tabela do teste


@contextmanager  # contextmanager é um decorator que permite criar um contexto para o teste (usar with)
def _mock_db_time(
    *, model, time=datetime(2024, 1, 1)
):  # * é para desempacotar os argumentos
    # model é o modelo que vai ser mockado
    # time é o tempo que vai ser mockado
    def fake_time_handler(
        mapper, connection, target
    ):  # mapper é o mapper que vai ser mockado
        if hasattr(target, "created_at"):
            target.created_at = time
        if hasattr(target, "updated_at"):
            target.updated_at = time

    event.listen(model, "before_insert", fake_time_handler)

    yield time

    event.remove(model, "before_insert", fake_time_handler)


@pytest.fixture
def mock_db_time():
    return _mock_db_time
