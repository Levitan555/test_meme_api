import pytest
from endpoints.authorize import Authorize
from endpoints.get_endpoint import GetMeme
from endpoints.post_endpoint import PostMeme
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme


@pytest.fixture(scope='session')
def create_meme(return_post_meme, return_token, return_delete_meme):
    post_data = return_post_meme.post_meme(return_token.auth_post())
    yield post_data
    return_delete_meme.delete_meme(post_data['id'], return_token.auth_post())


@pytest.fixture(scope='session')
def return_token():
    return Authorize()


@pytest.fixture()
def return_assert_live_token():
    return Authorize()


@pytest.fixture()
def return_get_meme():
    return GetMeme()


@pytest.fixture()
def return_get_meme_id():
    return GetMeme()


@pytest.fixture(scope='session')
def return_post_meme():
    return PostMeme()


@pytest.fixture()
def return_change_meme():
    return UpdateMeme()


@pytest.fixture(scope='session')
def return_delete_meme():
    return DeleteMeme()
