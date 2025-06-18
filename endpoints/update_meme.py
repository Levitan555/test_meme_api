import requests
import allure
from .base_endpoint import Endpoint


class UpdateMeme(Endpoint):

    @allure.feature('PUT request')
    @allure.story('Changing the meme')
    @allure.step('Изменение мема')
    def change_meme(self, create_post, return_token):
        self.response = requests.put(
            f'{self.url}/meme/{create_post['id']}', json={
                'id': create_post['id'],
                'text': 'But first',
                'url': 'https://i.imgflip.com/7f9vxf.jpg',
                'tags': ['first', 'selfie'],
                'info': {'monkey': 'selfie'}
            }, headers=return_token)
        return self.response.json()

    @allure.feature('PUT request')
    @allure.story('Checking that the meme has been changed')
    @allure.step('Проверка, что мем изменен')
    def check_that_post_updated(self, create_post, return_token):
        self.response = requests.get(f'{self.url}/meme/{create_post['id']}', headers=return_token)
        assert self.response.json()['id'] == create_post['id']

    @allure.feature('PUT request')
    @allure.story("Changing someone else's meme")
    @allure.step('Изменение чужого мема')
    def trying_to_change_someone_meme(self, return_token):
        self.response = requests.put(
            f'{self.url}/meme/2', json={
                'id': 2,
                'text': 'But first',
                'url': 'https://i.imgflip.com/7f9vxf.jpg',
                'tags': ['first', 'selfie'],
                'info': {'monkey': 'selfie'}
            }, headers=return_token)
        assert self.response.status_code == 403, 'Status code is incorrect'

    @allure.feature('PUT request')
    @allure.story('Empty body meme edit')
    @allure.step('Изменение мема с пустым телом')
    def check_put_empty_body(self, create_post, return_token):
        self.response = requests.put(
            f'{self.url}/meme/{create_post['id']}', json={'id': create_post['id']}, headers=return_token)
        assert self.response.status_code == 400, 'Status code is incorrect'
