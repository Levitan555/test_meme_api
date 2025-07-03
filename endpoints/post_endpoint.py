import requests
import allure
from endpoints.base_endpoint import Endpoint
from utils.body_list import positive_body


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
    def check_that_post_created(self, create_meme, return_token):
        self.response = requests.get(f'{self.url}/meme/{create_meme['id']}', headers=return_token)
        assert self.response.json() == create_meme
        # return self.response.json()['id']

    @allure.feature('POST request')
    @allure.story('Checking the creation of a meme with invalid request body')
    @allure.step('Проверка создания мема с невалидным телом запроса')
    def check_post_meme_with_invalid_body(self, status, body, return_token):
        self.response = requests.post(f'{self.url}/meme', json=body, headers=return_token)
        if self.response.status_code != int(status):
            print(f'Bug: получил статус код {self.response.status_code} с данными {body}, вместо {status}')
        else:
            assert self.response.status_code == int(status), 'Status code is incorrect'
