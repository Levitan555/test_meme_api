import requests
import allure
from endpoints.base_endpoint import Endpoint


class DeleteMeme(Endpoint):

    @allure.feature('DELETE request')
    @allure.story('Meme removal')
    @allure.step('Удаление мема')
    def delete_meme(self, created_meme_id, endpoint_auth):
        self.response = requests.delete(f'{self.url}/meme/{created_meme_id}', headers=endpoint_auth)
        self.check_status_code_is_200()
        return self.response

    @allure.feature('DELETE request')
    @allure.story('Checking for meme removal')
    @allure.step('Проверка удаления мема')
    def check_that_meme_deleted(self, created_meme_id, endpoint_auth):
        self.response = requests.get(f'{self.url}//meme/{created_meme_id}', headers=endpoint_auth)
        self.check_status_code_is_404()
