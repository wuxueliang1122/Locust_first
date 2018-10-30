from locust import task, TaskSet


class H5Activity(TaskSet):

    @task(5)
    def activity_installment(self):
        """

        :return:
        """
        self.client.get('/installmentWap/#/')

