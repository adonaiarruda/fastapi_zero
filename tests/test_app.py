from http import HTTPStatus

from fastapi.testclient import TestClient

from src.fastapi_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    """Teste de 3 etapas (AAA)
    - A: Arrange - (Fazer fixture)
    - A: Act     - Execute o SUT (System under test)
    - A: Assert  - Garanta que A é A
    """

    # Arrange
    client = TestClient(app)
    # Act
    response = client.get("/")
    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Olá Mundo!"}


def test_hello_world_html(client):
    response = client.get("/hello-world")
    assert response.status_code == HTTPStatus.OK
    assert response.headers["content-type"] == "text/html; charset=utf-8"
    assert response.text.startswith("<html>")


def test_create_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "alice",
            "email": "alice@example.com",
            "password": "123456",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "alice",
        "email": "alice@example.com",
    }


def test_read_users(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [
            {
                "id": 1,
                "username": "alice",
                "email": "alice@example.com",
            }  # Neste caso é um péssimo teste, pois são testes acoplados.
            # Code smells totalmente ruins.
        ]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "mynewpassword",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "bob",
        "email": "bob@example.com",
        "id": 1,
    }


def test_delete_user_should_return_not_found__exercicio(client):
    response = client.delete("/users/666")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User 666 not found"}


def test_update_user_should_return_not_found__exercicio(client):
    response = client.put(
        "/users/666",
        json={
            "username": "bob",
            "email": "bob@example.com",
            "password": "mynewpassword",
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User 666 not found"}


def test_get_user_should_return_not_found__exercicio(client):
    response = client.get("/users/666")

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User 666 not found"}


def test_get_user___exercicio(client):
    response = client.get("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "bob",
        "email": "bob@example.com",
        "id": 1,
    }


def test_delete_user(client):
    response = client.delete("/users/1")

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}
