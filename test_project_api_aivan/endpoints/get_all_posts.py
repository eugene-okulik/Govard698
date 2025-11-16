import requests
import allure

from test_project_api_aivan.endpoints.endpoint import Endpoint


class GetAllPost(Endpoint):

    @allure.step('get post')
    def req_get_all_post(self, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.get(
            self.url,
            headers=headers
        )
        self.json = self.response.json()
        return self.response
