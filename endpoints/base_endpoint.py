class Endpoint:
    url = 'http://memesapi.course.qa-practice.com/'
    response = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200, f'{self.response.status_code}: Status code is incorrect'

    def check_that_body_is_json(self):
        assert type(self.response.json()) == dict, 'Type body is incorrect'
        assert self.response.json() != {}, 'Empty body'
