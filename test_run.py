from locust import HttpLocust
from testcases.test_web import UserBehavior
from testcases.test_h5 import H5Activity
from testcases.test_file import CdnFile
from common.config import Config


_web_host, _h5_host, _file_host = Config().get_host()


class WebsiteUser(HttpLocust):
    weight = 3
    host = _web_host
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 3000


class H5ActivityUser(HttpLocust):
    weight = 2
    host = _h5_host
    task_set = H5Activity
    min_wait = 2000
    max_wait = 6000


class CdnFileUser(HttpLocust):
    weight = 1
    host = _file_host
    task_set = CdnFile
    min_wait = 10000
    max_wait = 50000
