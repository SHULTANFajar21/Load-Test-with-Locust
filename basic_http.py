from locust import task, HttpUser, constant



class myTesting(HttpUser):
    host = "https://reqres.in/"
    wait_time = constant(1)

    @task
    def test_GET(self):
        self.client.get("api/users?page=2")