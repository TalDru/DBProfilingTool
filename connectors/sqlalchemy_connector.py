# DB Connector for SqlAlchemy

import sqlalchemy
import sqlalchemy.orm
from sqlalchemy import INTEGER, String, Boolean, BLOB
from sqlalchemy.ext.declarative import declarative_base

from base_connector import ConnectorBase
from common.consts import DEFAULT_DB_NAME, DEFAULT_TABLE_NAME

CONNECTION_STRING = "mysql+pymysql://root:123456@localhost:3306/"


class Connector(ConnectorBase):

    def __init__(self):
        super(Connector, self).__init__()

    SQLA_Base = declarative_base()

    class DataTbl(SQLA_Base):
        __tablename__ = DEFAULT_TABLE_NAME

        _id = sqlalchemy.Column(INTEGER, primary_key=True)
        index = sqlalchemy.Column(INTEGER)
        name = sqlalchemy.Column(String(50))
        is_male = sqlalchemy.Column(Boolean)
        picture = sqlalchemy.Column(BLOB)

    def __enter__(self):
        self.db = sqlalchemy.create_engine(CONNECTION_STRING)
        self.db.execute("CREATE DATABASE IF NOT EXISTS {}".format(DEFAULT_DB_NAME))
        self.db = sqlalchemy.create_engine(CONNECTION_STRING + DEFAULT_DB_NAME)

        session = sqlalchemy.orm.sessionmaker()
        session.configure(bind=self.db)
        self.connection = session()

        self.SQLA_Base.metadata.drop_all(self.db)
        self.SQLA_Base.metadata.create_all(self.db)

        return self

    def _transform(self, data):
        return self.DataTbl(**data)

    def read(self, index):
        return self.connection.query(self.DataTbl).filter(self.DataTbl.index == index).first()

    def write(self, data):
        transformed_data = self._transform(data)
        self.connection.add(transformed_data)

    def update(self, index, data):
        data.pop('index')
        self.connection.query(self.DataTbl).filter_by(index=index).update(data)

    def flush(self):
        self.connection.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.flush()
        self.connection.execute("DROP TABLE IF EXISTS {}".format(DEFAULT_TABLE_NAME))
        self.flush()

        self.connection.close()
        self.db.dispose()
