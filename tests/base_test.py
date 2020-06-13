# Base class for the DB tests

from abc import ABCMeta, abstractmethod

from common.consts import DEFAULT_SAMPLE_SIZE, DEFAULT_POOL_MAGNIFIER


class TestBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, connector):
        self.connector = connector
        self.sample_size = DEFAULT_SAMPLE_SIZE
        self.pool_size = int(self.sample_size * DEFAULT_POOL_MAGNIFIER)

    @abstractmethod
    def __enter__(self):
        # Implement the test setup here
        raise NotImplementedError

    @abstractmethod
    def run_test(self, metadata=None):
        # Implement the test here
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Implement the test cleanup here
        raise NotImplementedError
