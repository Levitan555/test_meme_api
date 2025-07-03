import pytest
import allure
from utils.body_list import combine_data_500
from utils.body_list import combine_data_400
from utils.body_list import combine_post_negative_body_400
from utils.body_list import combine_post_negative_body_500


@allure.title('Авторизация')
def test_authorize(return_token):
    return_token.auth_post()
    return_token.check_status_code_is_200()
    return_token.check_type_body()


@allure.title('Проверяем код 500 на авторизацию, при невалидном теле')
@pytest.mark.parametrize('status, body', combine_data_500)
def test_authorized_with_invalid_body_code_500(return_token, status, body):
    return_token.check_authorization_with_invalid_body(status, body)


@allure.title('Проверяем код 400 на авторизацию, при невалидном теле')
@pytest.mark.parametrize('status, body', combine_data_400)
def test_authorized_with_invalid_body_code_400(return_token, status, body):
    return_token.check_authorization_with_invalid_body(status, body)


@allure.title('Проверка, жив ли токен')
def test_life_token(return_assert_live_token, return_token):
    return_assert_live_token.check_life_token(return_token)
    return_assert_live_token.check_status_code_is_200()
    return_assert_live_token.check_authorize_response_text()


@allure.title('Авторизация с невалидным токеном')
def test_authorized_with_invalid_token(return_assert_live_token):
    return_assert_live_token.check_authorize_with_invalid_token()


@allure.title('Получаем все объекты')
def test_get_meme(return_get_meme, return_token):
    return_get_meme.get_all_meme(return_token.auth_post())
    return_get_meme.check_status_code_is_200()
    return_get_meme.check_that_body_is_json()


@allure.title('Запрос на получение мема по id')
def test_get_meme_id(return_get_meme_id, create_meme, return_token):
    return_get_meme_id.get_meme_id(create_meme, return_token.auth_post())
    return_get_meme_id.check_status_code_is_200()
    return_get_meme_id.check_that_id_is_correct(create_meme)
    return_get_meme_id.check_that_body_is_json()


@allure.title('Создание мема')
def test_post_meme(return_post_meme, return_token):
    post_data = return_post_meme.post_meme(return_token.auth_post())
    return_post_meme.check_status_code_is_200()
    return_post_meme.check_that_body_is_json()
    return_post_meme.check_that_post_created(post_data, return_token.auth_post())


@allure.title('Проверяем код 400, при создании мема с невалидным телом')
@pytest.mark.parametrize('status, body', combine_post_negative_body_400)
def test_post_meme_with_invalid_body_code_400(return_post_meme, status, body, return_token):
    return_post_meme.check_post_meme_with_invalid_body(status, body, return_token.auth_post())


@allure.title('Проверяем код 500, при создании мема с невалидным телом')
@pytest.mark.parametrize('status, body', combine_post_negative_body_500)
def test_post_meme_with_invalid_body_code_500(return_post_meme, status, body, return_token):
    return_post_meme.check_post_meme_with_invalid_body(status, body, return_token.auth_post())


@allure.title('Изменение мема')
def test_update_meme(return_change_meme, create_meme, return_token):
    meme_data_update = return_change_meme.change_meme(create_meme, return_token.auth_post())
    return_change_meme.check_status_code_is_200()
    return_change_meme.check_that_meme_updated(meme_data_update, return_token.auth_post())
    return_change_meme.check_that_body_is_json()


@allure.title('Пробуем изменить чужой мем')
def test_change_someone_meme(return_change_meme, return_token):
    return_change_meme.trying_to_change_someone_meme(return_token.auth_post())


@allure.title('Пробуем изменить тело мема на пустое')
def test_put_meme_with_empty_body(return_change_meme, create_meme, return_token):
    return_change_meme.check_put_empty_body(create_meme, return_token.auth_post())


@allure.title('Удаление мема')
def test_delete_meme(return_delete_meme, return_post_meme, create_meme, return_token):
    meme_data = return_post_meme.post_meme(return_token.auth_post())
    return_delete_meme.delete_meme(meme_data['id'], return_token.auth_post())
    return_delete_meme.check_that_meme_deleted(create_meme, return_token.auth_post())
