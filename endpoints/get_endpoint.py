import requests
import allure
from .base_endpoint import Endpoint

class GetMeme(Endpoint):

    @allure.feature('GET request')
    @allure.story('Request to receive all memes')
    @allure.step('Получение всех объектов')
    def get_meme(self, return_token):
        self.response = requests.get(f'{self.url}/meme', headers=return_token)
        return self.response

    @allure.feature('GET request')
    @allure.story('Request meme by id')
    @allure.step('Запрос мема по id')
    def get_meme_id(self, create_post, return_token):
        self.response = requests.get(f'{self.url}/meme/{create_post['id']}', headers=return_token)
        # assert self.response.json()['id'] == meme_id, 'ID is incorrect'
        return self.response


