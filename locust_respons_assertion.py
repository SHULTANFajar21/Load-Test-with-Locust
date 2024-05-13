from locust import task, HttpUser, constant
from assertpy import assert_that



class MyAPI(HttpUser):
    host = "https://reqres.in/"


    @task
    def test_GET(self):
        req = self.client.get("api/users?page=2")

        # aasertion status code
        assert_that(req.status_code).is_equal_to(200)

        # assertion type data
        assert_that(req.json().get("page")).is_type_of(int)