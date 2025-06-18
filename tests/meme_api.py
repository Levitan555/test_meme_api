import requests
import pytest



url = 'http://167.172.172.115:52355/'


def auth_post():
    body = {'name': 'sergey'}
    response = requests.post(f'{url}/authorize', json=body)
    auth_token = response.json()['token']
    assert response.status_code == 200, 'Status code is incorrect'
    return {'Authorization': auth_token}

def assert_life_token(auth_token):
    response = requests.get(f'{url}/authorize/{auth_token}')
    assert response.status_code == 200, 'Status code is incorrect'
    print(response.status_code)
    print(response.text)

# assert_life_token(auth_post()['Authorization'])

def get_meme(auth_token):
    response = requests.get(f'{url}/meme', headers=auth_token)
    print(response.status_code)
    assert response.status_code == 200, 'Status code is incorrect'
    return response


def post_meme(auth_token):
    body = {
        'text': 'No stress', 'url': 'https://img.freepik.com/free-vector/'
                                    'simple-vibing-cat-square-meme_742173-4493.jpg?'
                                    't=st=1749916116~exp=1749919716~hmac='
                                    '74974ce61c7ae19b5b022890ab206993548e869cce097b33936f255091e27aa4&w=1800',
        'tags': ['stress', 'vibe'],
        'info': {'cat': 'no stress'}
    }
    response = requests.post(f'{url}/meme', headers=auth_token, json=body)
    print(response.json()['id'])
    meme_id = response.json()['id']
    print(response.status_code)
    assert response.status_code == 200, 'Status code is incorrect'
    return meme_id

# post_meme(auth_post())

def get_meme_id(auth_token, meme_id):
    response = requests.get(f'{url}/meme/{meme_id}', headers=auth_token)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200, 'Status code is incorrect'
    return response

# get_meme_id(auth_post(), post_meme(auth_post()))

def change_meme(auth_token, meme_id):
    body = {
        'id': meme_id,
        'text': 'But first', 'url': 'https://i.imgflip.com/7f9vxf.jpg',
        'tags': ['first', 'selfie'],
        'info': {'monkey': 'selfie'}
    }
    response = requests.put(f'{url}/meme/{meme_id}', headers=auth_token, json=body)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200, 'Status code is incorrect'
    return response

# change_meme(auth_post(), post_meme(auth_post()))


def delete_meme(auth_token, meme_id):
    response = requests.delete(f'{url}/meme/{meme_id}', headers=auth_token)
    print(response.status_code)
    assert response.status_code == 200, 'Status code is incorrect'
    return response

# delete_meme(auth_post(), post_meme(auth_post()))

def qqq(return_token):
    print(return_token)

qqq()