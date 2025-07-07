import pytest
from endpoints.authorize import Authorize
from endpoints.get_endpoint import GetMeme
from endpoints.post_endpoint import PostMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme
from utils.body_for_auth import body_auth


@pytest.fixture(scope='session')
def default_meme(create_endpoint, endpoint_auth, delete_endpoint):
    post_data = create_endpoint.create_meme(endpoint_auth.authorization(body_auth))
    yield post_data
    delete_endpoint.delete_meme(post_data['id'], endpoint_auth.authorization(body_auth))


@pytest.fixture(scope='session')
def endpoint_auth():
    return Authorize()


@pytest.fixture()
def auth_token_endpoint():
    return Authorize()


@pytest.fixture()
def get_endpoint():
    return GetMeme()


@pytest.fixture()
def get_id_endpoint():
    return GetMeme()


@pytest.fixture(scope='session')
def create_endpoint():
    return PostMeme()


@pytest.fixture()
def update_endpoint():
    return UpdateMeme()


@pytest.fixture(scope='session')
def delete_endpoint():
    return DeleteMeme()
