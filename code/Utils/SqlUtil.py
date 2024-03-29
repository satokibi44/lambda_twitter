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

    def create_table(self):
        with self.conn.cursor() as cur:
            create_sql = 'create table if not exists User (TwitterID BIGINT NOT NULL)'
            cur.execute(create_sql)
            self.conn.commit()
        self.conn.commit()

    def create_latestid_table(self):
        with self.conn.cursor() as cur:
            create_sql = 'create table if not exists latestID2 (Type VARCHAR(255) NOT NULL PRIMARY KEY, TwitterID BIGINT NOT NULL)'
            cur.execute(create_sql)
            self.conn.commit()
        self.conn.commit()

    def insert_latestid(self, type, id):
        with self.conn.cursor() as cur:
            insert_sql = 'INSERT INTO latestID2(Type, TwitterID) VALUES (%s, %s) ON duplicate KEY UPDATE Type = %s, TwitterID = %s'
            cur.execute(insert_sql, (type, id, type, id))
            self.conn.commit()

    def select_latestid(self, type):
        with self.conn.cursor() as cur:
            select_sql = 'select TwitterID from latestID2 Where Type = %s'
            cur.execute(select_sql, (type))
            for row in cur:
                print(int(row[0]))
                return int(row[0])
            return 0

    def create_calculate_kusorep_user_table(self):
        with self.conn.cursor() as cur:
            create_sql = 'create table if not exists KusorepScoringUser (AccountName VARCHAR(255) NOT NULL PRIMARY KEY, LatestID BIGINT NOT NULL)'
            cur.execute(create_sql)
            self.conn.commit()
        self.conn.commit()

    def insert_calculate_kusorep_user(self, account_name, tweet_id):
        with self.conn.cursor() as cur:
            insert_sql = 'INSERT INTO KusorepScoringUser(AccountName, LatestID) VALUES (%s, %s) ON duplicate KEY UPDATE AccountName = %s, LatestID = %s'
            cur.execute(insert_sql, (account_name,
                                     tweet_id, account_name, tweet_id))
            self.conn.commit()
        self.conn.commit()
        
    def delete_calculate_kusorep_user(self, account_name):
        with self.conn.cursor() as cur:
            delete_sql = 'delete from KusorepScoringUser where AccountName = %s'
            cur.execute(delete_sql, (account_name))
            self.conn.commit()
        self.conn.commit()

    def select_calculate_kusorep_user(self):
        user_name_list = []
        tweet_id_list = []
        with self.conn.cursor() as cur:
            cur.execute(
                "select AccountName, LatestID from KusorepScoringUser")
            for row in cur:
                user_name_list.append(row[0])
                tweet_id_list.append(int(row[1]))
        self.conn.commit()
        return user_name_list, tweet_id_list

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

    def select_mute_kusorep_user(self):
        mute_kusorep_user_info = []
        with self.conn.cursor() as cur:
            cur.execute("select * from UserOath2")
            for row in cur:
                if(row[2] == "3282531025"):
                    continue
                mute_kusorep_user_info.append(
                    {"oauth_token": row[0], "oauth_verifier": row[1], "user_id": row[2], "screen_name": row[3]})
        self.conn.commit()
        return mute_kusorep_user_info
