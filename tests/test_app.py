from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste é composto por 3 etapas (AAA)
    - A: Arrange (Arranjo)
    - A: Act (Agir)
    - A: Assert (Garantia)
    """

    # arrange
    client = TestClient(app)

    # act
    response = client.get('/')

    # assert
    assert response.json() == {'message': 'Olá mundo'}
    assert response.status_code == HTTPStatus.OK


def test_dex_deve_retornar_ola_mundo_html():
    client = TestClient(app)
    response = client.get('/dex')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text


def test_create_user():
    client = TestClient(app)

    response = client.post(
        '/users/',
        json={
            'id': 0,
            'username': 'alice',
            'email': 'alice@exemple.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@exemple.com',
    }
