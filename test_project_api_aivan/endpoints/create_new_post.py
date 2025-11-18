import requests
import allure

from test_project_api_aivan.endpoints.endpoint import Endpoint


class CreateNewPost(Endpoint):
    post_id = None

    @allure.step('Create post')
    def req_create_new_post(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            headers=headers,
            json=payload
        )
        self.json = self.response.json()
        self.post_id = self.json["id"]
        return self.response
