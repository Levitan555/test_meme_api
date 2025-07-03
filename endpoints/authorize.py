import requests
import allure
from endpoints.base_endpoint import Endpoint
from utils.body_list import invalid_token


class Authorize(Endpoint):
    body = {'name': 'sergey'}

    @allure.feature('Authorization')
    @allure.story('Request for authorization')
    @allure.step('Отправка запроса на авторизацию')
    def auth_post(self):
        self.response = requests.post(f'{self.url}/authorize', json=self.body)
        auth_token = self.response.json()['token']
        return {'Authorization': auth_token}

    @allure.feature('Authorization')
    @allure.story('Checking that the token is alive')
    @allure.step('Проверка, что токен жив')
    def check_life_token(self, return_token):
        authorized = return_token.auth_post()['Authorization']
        self.response = requests.get(f'{self.url}/authorize/{authorized}')

    @allure.feature('Authorization')
    @allure.story('Checking the response text')
    @allure.step('Проверка текста ответа')
    def check_authorize_response_text(self):
        assert self.response.text == f'Token is alive. Username is {self.body['name']}'

    @allure.feature('Authorization')
    @allure.story('Checking authorisation with invalid token')
    @allure.step('Проверка авторизации с недействительным токеном')
    def check_authorize_with_invalid_token(self):
        self.response = requests.get(f'{self.url}/authorize/{invalid_token}')
        assert self.response.status_code == 404, 'Status code is incorrect'

    @allure.feature('Authorization')
    @allure.story('Checking body type')
    @allure.step('Проверка типа тела')
    def check_type_body(self):
        assert type(self.response.json()) == dict, 'Type is not dict'
        assert self.response.json()['user'] == self.body['name'], 'Value "name" is incorrect'

    @allure.feature('Authorization')
    @allure.story('Checking authorisation with invalid body')
    @allure.step('Проверка авторизации с недопустимым телом')
    def check_authorization_with_invalid_body(self, status, body):
        self.response = requests.post(f'{self.url}/authorize', json=body)
        if self.response.status_code != int(status):
            print(f' Bug: получил статус код {self.response.status_code} с данными {body}, вместо {status}')
        else:
            assert self.response.status_code == int(status), 'Status code is incorrect'
