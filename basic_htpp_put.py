from locust import HttpUser, constant, task


class MyAPI(HttpUser):
    host = "https://reqres.in/"
    wait_time = constant(1)

    @task
    def test_1(self):
        payload = {
            "name": "cibau",
            "job": "QA Lead"
        }

        req = self.client.put("api/users/2", json=payload)
        print(req.json())