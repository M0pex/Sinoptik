import sqlite3
from tgbot.data.config import PATH_DATABASE



def db():
    conn = sqlite3.connect(PATH_DATABASE)
    cur = conn.cursor()

    if len(cur.execute("PRAGMA table_info(storage_users)").fetchall()) == 8:
        print("DB storage_users was found")
    else:
        cur.execute("CREATE TABLE IF NOT EXISTS storage_users("
                    "id INTEGER PRIMARY KEY,"
                    "user_id INTEGER NOT NULL,"
                    "user_login TEXT,"
                    "user_name TEXT,"
                    "city TEXT,"
                    "language TEXT,"
                    "alarm TEXT,"
                    "evry_day INTEGER)")
        print("DB storage_users was not found | Creating...")

    conn.commit()

    cur.close()
    conn.close()




