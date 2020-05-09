# DB Connector for MongoDB

import base64

from pymongo import MongoClient

from base_connector import ConnectorBase
from common.consts import DEFAULT_DB_NAME, DEFAULT_TABLE_NAME

CONNECTION_STRING = "mongodb://127.0.0.1:27017/"


class Connector(ConnectorBase):

    def __init__(self):
        super(Connector, self).__init__()

    def __enter__(self):
        self.connection = MongoClient(CONNECTION_STRING)
        self.db = self.connection[DEFAULT_DB_NAME]

        return self

    def _transform(self, data):
        data['picture'] = base64.b64encode(data['picture'])
        return data

    def read(self, index):
        return self.db[DEFAULT_TABLE_NAME].find_one({'index': index})

    def write(self, data):
        transformed_data = self._transform(data)
        return self.db[DEFAULT_TABLE_NAME].insert_one(transformed_data)

    def update(self, index, data):
        transformed_data = self._transform(data)
        return self.db[DEFAULT_TABLE_NAME].update_one({'index': index}, {'$set': transformed_data})

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.drop_database(self.db.name)
        self.connection.close()
