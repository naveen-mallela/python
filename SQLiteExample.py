import os
import DBcm

db_details = "CoachDB.sqlite3"

SQL_CREATE_TABLE_SWIMMERS = """
    CREATE TABLE IF NOT EXISTS swimmers
    (
        id integer not null primary key autoincrement,
        name varchar(32) not null,
        age integer not null
    )
"""

SQL_CREATE_TABLE_EVENTS = """
    CREATE TABLE IF NOT EXISTS events
    (
        id integer not null primary key autoincrement,
        distance vvarchar(16) not null,
        stroke varchar(16) not null
    )
"""

SQL_CREATE_TABLE_TIMES = """
    CREATE TABLE IF NOT EXISTS times
    (
        id integer not null primary key autoincrement,
        swimmer_id integer not null,
        event_id integer not null,
        time varchar(16) not null,
        ts timestamp DEFAULT current_timestamp
    )
"""

with DBcm.UseDatabase(db_details) as db:
    db.execute("pragma table_list")
    results = db.fetchall()
    print(results)
    
    db.execute(SQL_CREATE_TABLE_SWIMMERS)
    db.execute("pragma table_list")
    results = db.fetchall()
    print(results)

    db.execute(SQL_CREATE_TABLE_EVENTS)
    db.execute("pragma table_list")
    results = db.fetchall()
    print(results)

    db.execute("SQL_CREATE_TABLE_TIMES")
    db.execute("pragma table_list")
    results = db.fetchall()
    print(results)