from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fastapi_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    """Teste de 3 etapas (AAA)
    - A: Arrange - (Fazer fixture)
    - A: Act     - Execute o SUT (System under test)
    - A: Assert  - Garanta que A é A
    """

    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}
