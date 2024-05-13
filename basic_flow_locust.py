from locust import User, task

class MyfirstTest(User):

    @task
    def test1(self):
        print("pengujian ke : 1")


    @task
    def test2(self):
        print("pengujian ke : 2")