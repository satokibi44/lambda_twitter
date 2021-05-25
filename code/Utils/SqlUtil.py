import pymysql
import sys
import os

class SqlUtil():

    def __init__(self):
        rds_host = os.environ['RDS_HOST']
        password = os.environ['RDS_PASS']
        name = os.environ['RDS_NAME']
        db_name = os.environ['RDS_DB_NAME']
        try:
            self.conn = pymysql.connect(
                host=rds_host, user=name, passwd=password, db=db_name, connect_timeout=5)
        except pymysql.MySQLError as e:
            sys.exit()

    def create_table(self, table_name):
        with self.conn.cursor() as cur:
            create_sql = 'create table if not exists %s (TwitterID BIGINT NOT NULL)'
            cur.execute(create_sql,(table_name))
            self.conn.commit()
        self.conn.commit()

    def insert_twitterid(self, twitter_id):
        with self.conn.cursor() as cur:
            insert_sql = 'INSERT INTO User (TwitterID) SELECT %s WHERE NOT EXISTS (SELECT * FROM User WHERE TwitterID = %s)'
            cur.execute(insert_sql, (twitter_id, twitter_id))
            self.conn.commit()
        self.conn.commit()

    def select_twitterid(self):
        user_id_list = []
        with self.conn.cursor() as cur:
            cur.execute("select TwitterID from User")
            for row in cur:
                user_id_list.append(int(row[0]))
        self.conn.commit()
        return user_id_list

    def delete_twitterid(self, twitter_id):
        with self.conn.cursor() as cur:
            delete_sql = 'delete from User where TwitterID = %s'
            cur.execute(delete_sql, (twitter_id))
            self.conn.commit()
        self.conn.commit()
