import requests
import allure

from test_project_api_aivan.endpoints.endpoint import Endpoint


class DeletePost(Endpoint):

    @allure.step('delete post')
    def full_req_delete_post(self, post_id, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(
            f'{self.url}/{post_id}',
            headers=headers
        )
        return self.response
