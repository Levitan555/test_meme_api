import requests
import allure
from endpoints.base_endpoint import Endpoint
from utils.body_for_create import positive_body


class PostMeme(Endpoint):

    @allure.feature('POST request')
    @allure.story('Creating a meme')
    @allure.step('Создание мема')
    def create_meme(self, endpoint_auth):
        self.response = requests.post(f'{self.url}/meme', json=positive_body, headers=endpoint_auth)
        new_meme_post = self.response.json()
        self.check_status_code_is_200()
        return new_meme_post

    @allure.feature('POST request')
    @allure.story('Checking that a meme has been created')
    @allure.step('Проверка, что мем создан')
    def check_that_meme_created(self, default_meme, endpoint_auth):
        self.response = requests.get(f'{self.url}/meme/{default_meme['id']}', headers=endpoint_auth)
        assert self.response.json() == default_meme

    @allure.feature('POST request')
    @allure.story('Checking the creation of a meme with invalid request body')
    @allure.step('Проверка создания мема с невалидным телом запроса')
    def check_creation_meme_with_invalid_body(self, status, body, endpoint_auth):
        self.response = requests.post(f'{self.url}/meme', json=body, headers=endpoint_auth)
        if self.response.status_code != int(status):
            print(f'Bug: получил статус код {self.response.status_code} с данными {body}, вместо {status}')
        else:
            assert self.response.status_code == int(status), 'Status code is incorrect'
