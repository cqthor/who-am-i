import sqlite3


class DBHelper:
    def __init__(self):
        self.conn = sqlite3.connect("datas.sqlite", check_same_thread=False)
        self.setup()
        self.setup_users_name()

    def create_table(self, table_name):
        stmt = "CREATE TABLE IF NOT EXISTS {} ( name text)".format(table_name)
        self.conn.execute(stmt)
        self.conn.commit()

    def del_table(self, table_name):
        stmt = "DROP TABLE IF EXISTS {}".format(table_name)
        self.conn.execute(stmt)
        self.conn.commit()

    def edit_table(self, table_name, new_name):
        stmt = "ALTER TABLE {} RENAME TO {}".format(table_name, new_name)
        self.conn.execute(stmt)
        self.conn.commit()

    def add_name(self, table_name, name):
        stmt = "INSERT INTO {} (name) VALUES (?)".format(table_name)
        args = (name,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_names(self, table_name):
        stmt = "SELECT * FROM {}".format(table_name)
        return self.conn.execute(stmt).fetchall()

    def del_name(self, table_name, name):
        stmt = "DELETE FROM {} WHERE name = (?)".format(table_name)
        args = (name,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_tables(self):
        stmt = "SELECT name FROM sqlite_master WHERE type='table'"
        tables = [table[0] for table in self.conn.execute(stmt).fetchall()]
        tables.remove("users")
        tables.remove("users_name")
        return tables

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS users (user_id INTEGER PRIMARY KEY, username text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_user(self, user_id, username):
        stmt = "INSERT INTO users (user_id, username) VALUES (?,?)"
        args = (user_id, username)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_user_ids(self):
        stmt = "SELECT user_id FROM users"
        ids = [id[0] for id in self.conn.execute(stmt).fetchall()]
        return ids

    def get_users(self):
        stmt = "SELECT * FROM users"
        return self.conn.execute(stmt).fetchall()

    def del_all_users(self):
        stmt = "DELETE FROM users"
        self.conn.execute(stmt)
        self.conn.commit()

    def setup_users_name(self):
        stmt = "CREATE TABLE IF NOT EXISTS users_name (user_id INTEGER, name text, user_name text)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_users_name(self, user_id, name, user_name):
        stmt = "INSERT INTO users_name (user_id, name, user_name) VALUES (?,?,?)"
        args = (user_id, name, user_name)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_users_name(self, user_id, name):
        stmt = "SELECT * FROM users_name WHERE user_id = (?) AND name = (?)"
        args = (user_id, name)
        return self.conn.execute(stmt, args).fetchone()

    def del_all_users_name(self):
        stmt = "DELETE FROM users_name"
        self.conn.execute(stmt)
        self.conn.commit()
