import requests
import allure

from test_project_api_aivan.endpoints.endpoint import Endpoint


class UpdatePostPut(Endpoint):

    @allure.step('update put post')
    def full_req_update_put_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{post_id}',
            headers=headers,
            json=payload
        )
        self.json = self.response.json()
        return self.response
