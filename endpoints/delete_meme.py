import requests
import allure
from endpoints.base_endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.feature('DELETE request')
    @allure.story('Meme removal')
    @allure.step('Удаление мема')
    def delete_meme(self, create_meme_id, return_token):
        self.response = requests.delete(f'{self.url}/meme/{create_meme_id}', headers=return_token)
        assert self.response.status_code == 200, f'{self.response.status_code}: Status code is incorrect'
        return self.response

    @allure.feature('DELETE request')
    @allure.story('Checking for meme removal')
    @allure.step('Проверка удаления мема')
    def check_that_meme_deleted(self, create_meme_id, return_token):
        self.response = requests.get(f'{self.url}//meme/{create_meme_id}', headers=return_token)
        assert self.response.status_code == 404, f'{self.response.status_code}: Status code is incorrect'
