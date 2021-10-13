import sqlite3

class DB:
    def __init__(self, db, table):
        self.db = db
        self.table = table
        self.connstr = sqlite3.connect(self.db)
        self.cur = self.connstr.cursor()

    def get(self):
        self.cur.execute(f"select rowid,name,mobile from {self.table}")
        return self.cur.fetchall()

    def remove(self, id):
        self.cur.execute(f"delete from {self.table} where rowid = {id}")
        self.connstr.commit()
        return True

    def add(self, fields, vals):
        self.cur.execute(f"insert into {self.table} {fields} values {vals}")
        self.connstr.commit()
        return True
