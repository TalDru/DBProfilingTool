# Update DB test

import random

from base_test import TestBase
from common.generate_data import data_generator
from common.timer import time_execution_length


class Test(TestBase):
    def __init__(self, connector):
        super(Test, self).__init__(connector)

    def __enter__(self):
        # Set up the DB to contain 2 times the amount of the test size

        for data in data_generator(self.pool_size):
            self.connector.write(data)
        return self

    @time_execution_length
    def run_test(self, metadata=None):
        # Update a set amount of randomly generated indexes from the DB with new data

        for data in data_generator(self.sample_size):
            index = random.randint(0, self.pool_size-1)
            data['index'] = index
            _ = self.connector.update(index, data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
