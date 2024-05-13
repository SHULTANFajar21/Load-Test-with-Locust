from locust import HttpUser, constant, task, SequentialTaskSet

class MyAPI(SequentialTaskSet):

    @task
    def test_get(self):
        req = self.client.get("/api/users?page=2")
        print("test : GET")

    @task
    def test_post(self):
        payload = {
            "name": "shultan",
            "job": "QA"
        }
        req = self.client.post("/api/users", json=payload)
        print("test : POST")

    @task
    def test_put(self):
        payload = {
            "name": "fajar",
            "job": "QA lead"
        }
        req = self.client.put("/api/users/2", json=payload)
        print("test : PUT")

    @task
    def test_delete(self):
        req = self.client.delete("/api/users/2")



class setUpTest(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)
    tasks = [MyAPI]