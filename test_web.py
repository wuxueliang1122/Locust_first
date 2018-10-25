from locust import HttpLocust, task, TaskSet, seq_task, TaskSequence
from test_h5 import H5Activity as H5
from test_file import CdnFile


class MainIndex(TaskSet):

    @task(10)
    def test_main(self):
        self.client.get('/')


class ChooseCar(TaskSequence):

    @seq_task(1)
    @task(3)
    def choosecar(self):
        self.client.get('/choosecar')

    @seq_task(2)
    @task(3)
    def carlist(self):
        self.client.get('/choosecar/carlist')

    @seq_task(3)
    @task(4)
    def cardetail(self):
        self.client.get('/choosecar/cardetail')

    @seq_task(4)
    @task(1)
    def carapply(self):
        self.client.get('/choosecar/carapply')


class HotNews(TaskSet):

    @task
    def newdetail(self):
        id = 526
        url = "/hotnews/detail?id=" + str(id)
        with self.client.get(url, catch_response=True) as response:
            print(response.status_code)


class CarSupermarket(TaskSet):

    @task(2)
    def storequery(self):
        self.client.get('/activities/storequery')


class Recommended(TaskSequence):

    @task(3)
    def recommend(self):
        self.client.get('/recommend')

    @seq_task(1)
    @task(4)
    def cardetail(self):
        self.client.get('/choosecar/cardetail')

    @seq_task(2)
    @task(1)
    def carapply(self):
        self.client.get('/choosecar/carapply')


class UserBehavior(TaskSet):

    tasks = {MainIndex: 10, ChooseCar: 4, HotNews: 3, CarSupermarket: 2, Recommended: 3}


class WebsiteUser(HttpLocust):
    weight = 3
    host = ""
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000


class H5ActivityUser(HttpLocust):
    weight = 2
    host = ""
    task_set = H5
    min_wait = 2000
    max_wait = 6000


class CdnFileUser(HttpLocust):
    weight = 1
    host = ""
    task_set = CdnFile
    min_wait = 10000
    max_wait = 50000
