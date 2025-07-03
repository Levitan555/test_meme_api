import requests
import allure
from endpoints.base_endpoint import Endpoint


class GetMeme(Endpoint):

    @allure.feature('GET request')
    @allure.story('Request to receive all memes')
    @allure.step('Получение всех объектов')
    def get_all_meme(self, return_token):
        self.response = requests.get(f'{self.url}/meme', headers=return_token)
        return self.response

    @allure.feature('GET request')
    @allure.story('Request meme by id')
    @allure.step('Запрос мема по id')
    def get_meme_id(self, create_meme, return_token):
        self.response = requests.get(f'{self.url}/meme/{create_meme['id']}', headers=return_token)
        return self.response

    def check_that_id_is_correct(self, create_meme):
        assert self.response.json()['id'] == create_meme['id'], 'ID is incorrect'
