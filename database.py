import hashlib
import sqlite3

DBNAME = "../data.db"


def request(content, params=None):
    with sqlite3.connect(DBNAME) as db:
        c = db.cursor()
        if params is None:
            c.execute(content)
        else:
            c.execute(content, params)
        res = c.fetchall()
    return res


def commit(requete, params=None):
    with sqlite3.connect(DBNAME) as db:
        c = db.cursor()
        if params is None:
            c.execute(requete)
        else:
            c.execute(requete, params)
        db.commit()
    return


def create_user(name, pswd):
    hash_pswd = hashlib.sha256(pswd.encode()).hexdigest()
    args = [name, hash_pswd]
    sql = "INSERT INTO users (username, password) VALUES (?, ?)"
    return commit(sql, params=tuple(args))


def check_user_exist(name):
    args = [name]
    sql = "SELECT * FROM users WHERE username == ?"
    return True if request(sql, params=tuple(args)) else False


def check_if_valid(name, pswd):
    hash_pswd = hashlib.sha256(pswd.encode()).hexdigest()
    args = [name, hash_pswd]
    sql = "SELECT * FROM users WHERE username == ? AND password == ?"
    return True if request(sql, params=tuple(args)) else False


def load_user_info(name):
    args = [name]
    sql = "SELECT * FROM users WHERE username == ?"
    return request(sql, params=tuple(args))
