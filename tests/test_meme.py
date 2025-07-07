import pytest
import allure
from utils.body_for_auth import combine_data_500
from utils.body_for_auth import combine_data_400
from utils.body_for_create import combine_post_negative_body_400
from utils.body_for_create import combine_post_negative_body_500
from utils.body_for_auth import body_auth
from utils.body_for_auth import body_auth_for_update
from utils.body_for_auth import expected_text
from utils.body_for_update import body_for_put


@allure.title('Авторизация')
def test_authorize(endpoint_auth):
    endpoint_auth.authorization(body_auth)
    endpoint_auth.check_type_body()


@allure.title('Проверяем код 500 на авторизацию, при невалидном теле')
@pytest.mark.parametrize('status, body', combine_data_500)
def test_authorized_with_invalid_body_code_500(endpoint_auth, status, body):
    endpoint_auth.check_authorization_with_invalid_body(status, body)


@allure.title('Проверяем код 400 на авторизацию, при невалидном теле')
@pytest.mark.parametrize('status, body', combine_data_400)
def test_authorized_with_invalid_body_code_400(endpoint_auth, status, body):
    endpoint_auth.check_authorization_with_invalid_body(status, body)


@allure.title('Проверка, жив ли токен')
def test_life_token(auth_token_endpoint, endpoint_auth):
    auth_token_endpoint.check_life_token(endpoint_auth, body_auth)
    auth_token_endpoint.check_authorization_response_text(expected_text)


@allure.title('Авторизация с невалидным токеном')
def test_authorized_with_invalid_token(auth_token_endpoint):
    auth_token_endpoint.check_authorization_with_invalid_token()


@allure.title('Получаем все объекты')
def test_get_meme(get_endpoint, endpoint_auth):
    get_endpoint.get_all_meme(endpoint_auth.authorization(body_auth))
    get_endpoint.check_that_body_is_json()
    get_endpoint.chack_that_json_is_not_empty()


@allure.title('Запрос на получение мема по id')
def test_get_meme_id(get_id_endpoint, default_meme, endpoint_auth):
    get_id_endpoint.get_meme_id(default_meme, endpoint_auth.authorization(body_auth))
    get_id_endpoint.check_that_id_is_correct(default_meme)
    get_id_endpoint.check_that_body_is_json()
    get_id_endpoint.chack_that_json_is_not_empty()


@allure.title('Создание мема')
def test_create_meme(create_endpoint, endpoint_auth):
    post_data = create_endpoint.create_meme(endpoint_auth.authorization(body_auth))
    create_endpoint.check_that_body_is_json()
    create_endpoint.chack_that_json_is_not_empty()
    create_endpoint.check_that_meme_created(post_data, endpoint_auth.authorization(body_auth))


@allure.title('Проверяем код 400, при создании мема с невалидным телом')
@pytest.mark.parametrize('status, body', combine_post_negative_body_400)
def test_create_meme_with_invalid_body_code_400(create_endpoint, status, body, endpoint_auth):
    create_endpoint.check_creation_meme_with_invalid_body(status, body, endpoint_auth.authorization(body_auth))


@allure.title('Проверяем код 500, при создании мема с невалидным телом')
@pytest.mark.parametrize('status, body', combine_post_negative_body_500)
def test_create_meme_with_invalid_body_code_500(create_endpoint, status, body, endpoint_auth):
    create_endpoint.check_creation_meme_with_invalid_body(status, body, endpoint_auth.authorization(body_auth))


@allure.title('Изменение мема')
def test_update_meme(update_endpoint, default_meme, endpoint_auth):
    updated_meme = update_endpoint.change_meme(default_meme, endpoint_auth.authorization(body_auth), body_for_put)
    update_endpoint.check_that_meme_updated(updated_meme, endpoint_auth.authorization(body_auth))
    update_endpoint.check_that_body_is_json()
    update_endpoint.chack_that_json_is_not_empty()


@allure.title('Пробуем изменить чужой мем')
def test_update_someone_meme(update_endpoint, default_meme, endpoint_auth):
    update_endpoint.trying_to_update_someone_meme(default_meme, endpoint_auth.authorization(body_auth_for_update))


@allure.title('Пробуем изменить тело мема на пустое')
def test_update_meme_with_empty_body(update_endpoint, default_meme, endpoint_auth):
    update_endpoint.check_update_empty_body(default_meme, endpoint_auth.authorization(body_auth))


@allure.title('Удаление мема')
def test_delete_meme(delete_endpoint, create_endpoint, default_meme, endpoint_auth):
    created_meme = create_endpoint.create_meme(endpoint_auth.authorization(body_auth))
    delete_endpoint.delete_meme(created_meme['id'], endpoint_auth.authorization(body_auth))
    delete_endpoint.check_that_meme_deleted(default_meme, endpoint_auth.authorization(body_auth))
