# Read DB test

import random

from base_test import TestBase
from common.generate_data import data_generator
from common.timer import time_execution_length


class Test(TestBase):
    def __init__(self, connector):
        super(Test, self).__init__(connector)

    def __enter__(self):
        # Set up the DB to contain the test pool size

        for data in data_generator(self.pool_size):
            self.connector.write(data)

        self.connector.flush()

        return self

    @time_execution_length
    def run_test(self, metadata=None):
        # Read a set amount of randomly generated indexes from the DB

        for i in range(self.sample_size):
            index = random.randint(0, self.pool_size - 1)
            self.connector.read(index)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
