# Base class for the DB connectors

from abc import ABCMeta, abstractmethod


class ConnectorBase(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        self.db = None
        self.connection = None

    @abstractmethod
    def __enter__(self):
        raise NotImplementedError

    @abstractmethod
    def _transform(self, data):
        raise NotImplementedError

    @abstractmethod
    def read(self, index):
        raise NotImplementedError

    @abstractmethod
    def write(self, data):
        raise NotImplementedError

    @abstractmethod
    def update(self, index, data):
        raise NotImplementedError

    @abstractmethod
    def flush(self):
        raise NotImplementedError

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError
