from locust import HttpUser, constant, task

class MyAPI(HttpUser):
    host = "https://reqres.in/"
    wait_time = constant(1)


    @task
    def test_1(self):
        req = self.client.delete("api/users/2")
        print(req.status_code)