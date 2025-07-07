body_auth = {'name': 'sergey'}
body_auth_for_update = {'name': 'andrey'}

expected_text = 'Token is alive. Username is '

auth_invalid_body_500 = [262567165, ['name', 'sergey'], 'name sergey', ('name', 'sergey')]
auth_invalid_body_400 = [
    {'name': ''}, {'batman': 'sergey'}, '', {'name': 675387}, {'': ''}, {'name': ' sergey'}, {'name': 'sergey '}
]
combine_data_500 = [('500', body) for body in auth_invalid_body_500]
combine_data_400 = [('400', body) for body in auth_invalid_body_400]
invalid_token = '9e1VKdNBc3vFhN3'
