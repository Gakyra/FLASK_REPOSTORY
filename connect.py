import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данних створена і підключена до SQLite")

    sqlite_select_query = "select sqlite_version():"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версія база данних SQLite",record)
    cursor.close()


except sqlite3.Error as error:
    print("Помилка підключення до ", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("З'єднання з SQLite закрите")