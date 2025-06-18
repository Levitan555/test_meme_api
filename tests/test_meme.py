import pytest
import allure
from body_list import combine_data
from body_list import combine_post_negative_body


@allure.title('Авторизация')
@pytest.mark.parametrize('status, body', combine_data)
def test_authorize(return_token, status, body):
    return_token.auth_post()
    return_token.check_status_code_is_200()
    return_token.assert_type_body()
    return_token.assert_invalid_body(status, body)

@allure.title('Проверка, жив ли токен')
def test_life_token(return_assert_live_token, return_token):
    return_assert_live_token.assert_life_token(return_token)
    return_assert_live_token.check_status_code_is_200()
    return_assert_live_token.assert_authorize_response_text()
    return_assert_live_token.assert_authorize_invalid_token()

@allure.title('Получаем все объекты')
def test_get_meme(return_get_meme, return_token):
    return_get_meme.get_meme(return_token.auth_post())
    return_get_meme.check_status_code_is_200()
    return_get_meme.check_that_body_is_json()

@allure.title('Запрос на получение мема по id')
def test_get_meme_id(return_get_meme_id, create_post, return_token):
    return_get_meme_id.get_meme_id(create_post, return_token.auth_post())
    return_get_meme_id.check_status_code_is_200()
    return_get_meme_id.check_that_body_is_json()

@allure.title('Создание мема')
@pytest.mark.parametrize('status, body', combine_post_negative_body)
def test_post_meme(return_post_meme, return_token, status, body):
    post_data = return_post_meme.post_meme(return_token.auth_post())
    return_post_meme.check_status_code_is_200()
    return_post_meme.check_that_body_is_json()
    return_post_meme.check_that_post_created(post_data, return_token.auth_post())
    return_post_meme.assert_post_invalid_body(status, body, return_token.auth_post())


@allure.title('Изменение мема')
def test_update_meme(return_change_meme, create_post, return_token):
    post_data_update = return_change_meme.change_meme(create_post, return_token.auth_post())
    return_change_meme.check_status_code_is_200()
    return_change_meme.check_that_post_updated(post_data_update, return_token.auth_post())
    return_change_meme.check_that_body_is_json()
    return_change_meme.trying_to_change_someone_meme(return_token.auth_post())
    return_change_meme.check_put_empty_body(create_post, return_token.auth_post())


@allure.title('Удаление мема')
def test_delete_meme(return_delete_meme, return_post_meme, create_post, return_token):
    post_data = return_post_meme.post_meme(return_token.auth_post())
    return_delete_meme.delete_meme(post_data['id'], return_token.auth_post())
    return_delete_meme.check_that_post_deleted(create_post, return_token.auth_post())

