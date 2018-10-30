from locust import TaskSet, task


class CdnFile(TaskSet):

    @task(3)
    def test_first(self):
        self.client.get("/resources/20180621/5d21d036b440ea90bb60ecaf4d8fed54.html")

    @task(2)
    def test_sencond(self):
        self.client.get("/resources/20180829/d4e9f2f5b3d77832f755d73325f14d30.html")

    @task(1)
    def test_third(self):
        self.client.get("/resources/20180829/c13c75d8a26856e973fb9dd4c0cfb049.html")
