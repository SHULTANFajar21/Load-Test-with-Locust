from locust import HttpUser, constant, task

class MyAPI(HttpUser):
    host = "https://reqres.in/"
    wait_time = constant(1)

    @task
    def test_1(self):
        payload = {
            "name": "Shultan Maulana Fajar",
            "job": "QA Engineer"
        }

        req = self.client.post("api/users", json=payload)
        print(req.json())