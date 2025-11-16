import allure


class Endpoint:
    url = "http://objapi.course.qa-practice.com/object"
    headers = {"Content-Type": "application/json"}
    response = None
    json = None

    @allure.step('Check that response is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200
