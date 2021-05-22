import pymysql
import sys

class SqlUtil():

    def __init__(self):
        rds_host = "testdb.cwomgpjrietf.us-east-2.rds.amazonaws.com"
        password = "sato310238"
        name = "admin"
        db_name = "ExampleDB"
        try:
            self.conn = pymysql.connect(host=rds_host, user=name,passwd=password, db=db_name, connect_timeout=5)
        except pymysql.MySQLError as e:
            sys.exit()
    
    def create_table(self):
        with self.conn.cursor() as cur:
            create_sql = 'create table if not exists User (TwitterID int NOT NULL)'
            cur.execute(create_sql)
            self.conn.commit()
        self.conn.commit()

    def insert_user(self, twitter_id):
        with self.conn.cursor() as cur:
            insert_sql = 'insert into User (TwitterID) values (%s)'
            cur.execute(insert_sql,(twitter_id))
            self.conn.commit()
        self.conn.commit()
    
    def select_twitterid(self):
        user_id_list = []
        with self.conn.cursor() as cur:
            cur.execute("select TwitterID from User")
            for row in cur:
                user_id_list.append(row)
        self.conn.commit()
        return user_id_list

    def delete_twitterid(self, twitter_id):
        with self.conn.cursor() as cur:
            delete_sql = 'delete from User where (TwitterID) values (%s)'
            cur.execute(delete_sql, (twitter_id))
            self.conn.commit()
        self.conn.commit()
