"""Add user flow """
import sqlite3
import hashlib


def add_user(user, pwd, privilege):
    """Adds new user to database"""
    conn = sqlite3.connect("quiz.db")
    cursor = conn.cursor()
    cursor.execute(
        'Insert into USER(user,pass,type) values("{0}","{1}","{2}");'.format(
            user, pwd, privilege
        )
    )
    conn.commit()
    conn.close()


with open("users.csv", "r") as file:
    lines = file.read().splitlines()

for users in lines:
    (name, role) = users.split(",")
    print(name)
    print(role)
    add_user(name, hashlib.md5(name.encode()).hexdigest(), role)
