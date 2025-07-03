# body lists for authorize
auth_invalid_body_500 = [262567165, ['name', 'sergey'], 'name sergey', ('name', 'sergey')]
auth_invalid_body_400 = [
    {'name': ''}, {'batman': 'sergey'}, '', {'name': 675387}, {'': ''}, {'name': ' sergey'}, {'name': 'sergey '}
]
combine_data_500 = [('500', body) for body in auth_invalid_body_500]
combine_data_400 = [('400', body) for body in auth_invalid_body_400]
invalid_token = '9e1VKdNBc3vFhN3'

# body lists for post request
positive_body = {
    'text': 'No stress', 'url': 'https://img.freepik.com/free-vector/'
                                'simple-vibing-cat-square-meme_742173-4493.jpg?'
                                't=st=1749916116~exp=1749919716~hmac='
                                '74974ce61c7ae19b5b022890ab206993548e869cce097b33936f255091e27aa4&w=1800',
    'tags': ['stress', 'vibe'],
    'info': {'cat': 'no stress'}
}
post_negative_body_500 = [45673, 'text']
post_negative_body_400 = ['', {}, [], (), {
    'text': 'But first',
    'url': 'https://i.imgflip.com/7f9vxf.jpg',
    'tags': ['first', 'selfie'],
}, {
                              'text': 'But first',
                              'url': 'https://i.imgflip.com/7f9vxf.jpg',
                              'info': {'monkey': 'selfie'}
                          }, {
                              'url': 'https://i.imgflip.com/7f9vxf.jpg',
                              'tags': ['first', 'selfie'],
                              'info': {'monkey': 'selfie'}
                          }, {
                              'text': 'But first',
                              'tags': ['first', 'selfie'],
                              'info': {'monkey': 'selfie'}
                          }, {
                              'text': 79097,
                              'url': ['https://i.imgflip.com/7f9vxf.jpg'],
                              'tags': 'first',
                              'info': ('monkey', 'selfie')
                          }
                          ]
combine_post_negative_body_400 = [('400', body) for body in post_negative_body_400]
combine_post_negative_body_500 = [('500', body) for body in post_negative_body_500]
