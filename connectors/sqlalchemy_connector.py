# DB Connector for SqlAlchemy

import sqlalchemy
import sqlalchemy.orm
from sqlalchemy.dialects import mysql
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

        _id = sqlalchemy.Column(sqlalchemy.Integer(), primary_key=True)
        index = sqlalchemy.Column(sqlalchemy.Integer())
        name = sqlalchemy.Column(sqlalchemy.String(length=50))
        is_male = sqlalchemy.Column(sqlalchemy.Boolean())
        picture = sqlalchemy.Column(mysql.BLOB())

    def __enter__(self):
        self.db = sqlalchemy.create_engine(CONNECTION_STRING)
        self.db.execute("CREATE DATABASE IF NOT EXISTS {}".format(DEFAULT_DB_NAME))
        self.db = sqlalchemy.create_engine(CONNECTION_STRING + DEFAULT_DB_NAME)

        session = sqlalchemy.orm.sessionmaker()
        session.configure(bind=self.db)
        self.connection = session()

        self.SQLA_Base.metadata.create_all(self.db)

        return self

    def _transform(self, data):
        return self.DataTbl(**data)

    def read(self, index):
        return self.connection.query(self.DataTbl).filter_by(index=index).first()

    def write(self, data):
        transformed_data = self._transform(data)
        self.connection.add(transformed_data)
        return self.connection.commit()

    def update(self, index, data):
        self.connection.query(self.DataTbl).filter_by(index=index).update(data)
        return self.connection.commit()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.DataTbl.__table__.drop(self.db)
        self.db.execute("DROP DATABASE {}".format(DEFAULT_DB_NAME))
        self.connection.commit()

        self.connection.close()
        self.db.dispose()
