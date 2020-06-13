# DB Connector for ZODB
import base64

import ZODB
import ZODB.FileStorage
import transaction
from BTrees.OOBTree import OOBTree
from ZODB.FileStorage import FileStorage
from persistent import Persistent

from base_connector import ConnectorBase
from common.consts import DEFAULT_DB_NAME, DEFAULT_TABLE_NAME

CONNECTION_STRING = r"C:\DB\ZODB\{}.fs"


class Connector(ConnectorBase):

    def __init__(self):
        super(Connector, self).__init__()

    def __enter__(self):
        storage = FileStorage(CONNECTION_STRING.format(DEFAULT_DB_NAME), create=True, pack_keep_old=False)
        self.zdb = ZODB.DB(storage)
        self.connection = self.zdb.open()
        self.db = self.connection.root()

        self.db[DEFAULT_TABLE_NAME] = OOBTree()
        transaction.commit()

        return self

    def _transform(self, data):
        data['picture'] = base64.b64encode(data['picture'])
        data_obj = DataObj(**data)
        return data_obj

    def read(self, index):
        return self.db[DEFAULT_TABLE_NAME][index]

    def write(self, data):
        transformed_data = self._transform(data)
        self.db[DEFAULT_TABLE_NAME].update({transformed_data.index: transformed_data})

    def update(self, index, data):
        transformed_data = self._transform(data)
        self.db[DEFAULT_TABLE_NAME].update({index: transformed_data})

    def flush(self):
        transaction.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        del self.db[DEFAULT_TABLE_NAME]
        self.flush()

        self.connection.close()
        self.zdb.pack()
        self.zdb.close()


class DataObj(Persistent):

    def __init__(self, index, name, is_male, picture):
        self.index = index
        self.name = name
        self.is_male = is_male
        self.picture = picture
