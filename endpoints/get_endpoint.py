import requests
import allure
from endpoints.base_endpoint import Endpoint


class GetMeme(Endpoint):

    @allure.feature('GET request')
    @allure.story('Request to receive all memes')
    @allure.step('Получение всех объектов')
    def get_all_meme(self, endpoint_auth):
        self.response = requests.get(f'{self.url}/meme', headers=endpoint_auth)
        self.check_status_code_is_200()
        return self.response

    @allure.feature('GET request')
    @allure.story('Request meme by id')
    @allure.step('Запрос мема по id')
    def get_meme_id(self, default_meme, endpoint_auth):
        self.response = requests.get(f'{self.url}/meme/{default_meme['id']}', headers=endpoint_auth)
        self.check_status_code_is_200()
        return self.response

    def check_that_id_is_correct(self, default_meme):
        assert self.response.json()['id'] == default_meme['id'], 'ID is incorrect'
