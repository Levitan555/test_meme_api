class Endpoint:
    url = 'http://memesapi.course.qa-practice.com/'
    response = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200, f'{self.response.status_code}: Status code is incorrect'

    def check_status_code_is_404(self):
        assert self.response.status_code == 404, f'{self.response.status_code}: Status code is incorrect'

    def check_that_body_is_json(self):
        assert type(self.response.json()) == dict, 'Type body is incorrect'

    def chack_that_json_is_not_empty(self):
        assert self.response.json() != {}, 'Empty body'
