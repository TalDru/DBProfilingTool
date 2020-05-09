# Write DB test

from base_test import TestBase
from common.generate_data import data_generator
from common.timer import time_execution_length


class Test(TestBase):
    def __init__(self, connector):
        super(Test, self).__init__(connector)

    def __enter__(self):
        return self

    @time_execution_length
    def run_test(self, metadata=None):
        # Write a set amount of randomly generated data into the DB

        for data in data_generator(self.sample_size):
            self.connector.write(data)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
