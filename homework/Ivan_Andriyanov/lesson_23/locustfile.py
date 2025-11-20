from locust import HttpUser, task


class TestApi(HttpUser):

    @task(1)
    def get_all_posts(self):
        self.client.get("/object")

    @task(2)
    def get_one_post(self):
        self.client.get("/object/1")

    @task(3)
    def send_post(self):
        self.client.post(
            "/object",
            json={
                "name": "test andriyanov",
                "data": {
                    "group": 13121231,
                },
            },
        )
