import requests
import allure
from endpoints.base_endpoint import Endpoint
from utils.body_for_auth import invalid_token
from utils.body_for_auth import body_auth


class Authorize(Endpoint):

    @allure.feature('Authorization')
    @allure.story('Request for authorization')
    @allure.step('Отправка запроса на авторизацию')
    def authorization(self, body):
        self.response = requests.post(f'{self.url}/authorize', json=body)
        auth_token = self.response.json()['token']
        self.check_status_code_is_200()
        return {'Authorization': auth_token}

    @allure.feature('Authorization')
    @allure.story('Checking that the token is alive')
    @allure.step('Проверка, что токен жив')
    def check_life_token(self, endpoint_auth, body):
        authorized = endpoint_auth.authorization(body)['Authorization']
        self.response = requests.get(f'{self.url}/authorize/{authorized}')
        self.check_status_code_is_200()

    @allure.feature('Authorization')
    @allure.story('Checking the response text')
    @allure.step('Проверка текста ответа')
    def check_authorization_response_text(self, expected_text):
        assert self.response.text == f'{expected_text}{body_auth['name']}'

    @allure.feature('Authorization')
    @allure.story('Checking authorisation with invalid token')
    @allure.step('Проверка авторизации с недействительным токеном')
    def check_authorization_with_invalid_token(self):
        self.response = requests.get(f'{self.url}/authorize/{invalid_token}')
        self.check_status_code_is_404()

    @allure.feature('Authorization')
    @allure.story('Checking body type')
    @allure.step('Проверка типа тела')
    def check_type_body(self):
        assert type(self.response.json()) == dict, 'Type is not dict'
        assert self.response.json()['user'] == body_auth['name'], 'Value "name" is incorrect'

    @allure.feature('Authorization')
    @allure.story('Checking authorisation with invalid body')
    @allure.step('Проверка авторизации с недопустимым телом')
    def check_authorization_with_invalid_body(self, status, body):
        self.response = requests.post(f'{self.url}/authorize', json=body)
        if self.response.status_code != int(status):
            print(f' Bug: получил статус код {self.response.status_code} с данными {body}, вместо {status}')
        else:
            assert self.response.status_code == int(status), 'Status code is incorrect'
