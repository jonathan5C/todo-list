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
