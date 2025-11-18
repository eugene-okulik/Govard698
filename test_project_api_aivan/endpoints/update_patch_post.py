import requests
import allure

from test_project_api_aivan.endpoints.endpoint import Endpoint


class UpdatePatchPost(Endpoint):

    @allure.step('update patch post')
    def full_req_patch_post(self, post_id, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{post_id}',
            headers=headers,
            json=payload
        )
        self.json = self.response.json()
        return self.response
