import psycopg2
from utils import dbutils


class PostgresCls:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def db_connect(self):
        try:
            self.conn = psycopg2.connect(
                host=dbutils.db_host,
                user=dbutils.db_user,
                password=dbutils.db_password,
                port=dbutils.db_port,
                dbname=dbutils.db_name
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(str(e))

    def db_disconnect(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.conn:
                self.conn.close()
        except Exception as e:
            print(str(e))

    def commit_changes(self):
        try:
            self.conn.commit()
        except Exception as e:
            print(str(e))

    def rollback(self):
        try:
            self.conn.rollback()
        except Exception as e:
            print(str(e))
