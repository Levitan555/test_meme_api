import requests
import allure
from endpoints.base_endpoint import Endpoint


class UpdateMeme(Endpoint):

    @allure.feature('PUT request')
    @allure.story('Changing the meme')
    @allure.step('Изменение мема')
    def change_meme(self, default_meme, endpoint_auth, body_for_put):
        data = body_for_put.copy()
        data['id'] = default_meme['id']
        self.response = requests.put(
            f'{self.url}/meme/{default_meme['id']}', json=data, headers=endpoint_auth)
        self.check_status_code_is_200()
        return self.response.json()

    @allure.feature('PUT request')
    @allure.story('Checking that the meme has been changed')
    @allure.step('Проверка, что мем изменен')
    def check_that_meme_updated(self, updated_meme, endpoint_auth):
        self.response = requests.get(f'{self.url}/meme/{updated_meme['id']}', headers=endpoint_auth)
        assert self.response.json() == updated_meme

    @allure.feature('PUT request')
    @allure.story("Changing someone else's meme")
    @allure.step('Изменение чужого мема')
    def trying_to_update_someone_meme(self, default_meme, endpoint_auth):
        self.response = requests.put(
            f'{self.url}/meme/{default_meme['id']}', json={
                'id': default_meme['id'],
                'text': 'But first',
                'url': 'https://i.imgflip.com/7f9vxf.jpg',
                'tags': ['first', 'selfie'],
                'info': {'monkey': 'selfie'}
            }, headers=endpoint_auth)
        assert self.response.status_code == 403, 'Status code is incorrect'

    @allure.feature('PUT request')
    @allure.story('Empty body meme edit')
    @allure.step('Изменение мема с пустым телом')
    def check_update_empty_body(self, default_meme, endpoint_auth):
        self.response = requests.put(
            f'{self.url}/meme/{default_meme['id']}', json={'id': default_meme['id']}, headers=endpoint_auth)
        assert self.response.status_code == 400, 'Status code is incorrect'
