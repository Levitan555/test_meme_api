import requests
import allure
from .base_endpoint import Endpoint
from body_list import positive_body


class PostMeme(Endpoint):

    @allure.feature('POST request')
    @allure.story('Creating a meme')
    @allure.step('Создание мема')
    def post_meme(self, return_token):
        self.response = requests.post(f'{self.url}/meme', json=positive_body, headers=return_token)
        new_meme_post = self.response.json()
        return new_meme_post

    @allure.feature('POST request')
    @allure.story('Checking that a meme has been created')
    @allure.step('Проверка, что мем создан')
    def check_that_post_created(self, create_post, return_token):
        self.response = requests.get(f'{self.url}/meme/{create_post['id']}', headers=return_token)
        assert self.response.json()['id'] == create_post['id']
        return self.response.json()['id']

    @allure.feature('POST request')
    @allure.story('Checking the creation of a meme with invalid request body')
    @allure.step('Проверка создания мема с невалидным телом запроса')
    def assert_post_invalid_body(self, status, body, return_token):
        self.response = requests.post(f'{self.url}/meme', json=body, headers=return_token)
        if self.response.status_code != int(status):
            print(f'Bug: получил статус код {self.response.status_code} с данными {body}, вместо {status}')
        else:
            assert self.response.status_code == int(status), 'Status code is incorrect'
