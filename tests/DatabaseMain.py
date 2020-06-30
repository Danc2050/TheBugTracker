import src.DatabaseScript as DB


if __name__ == "__main__":
    db = DB.Database()
    record = ("A title asdfasdf", "a bug asdf", "some info qwer", False)
    db.connect(server_params="postgres_server")
    db.create_database(database_params="postgres_db")
    db.create_table(table_name="Bugs")
    db.list_insert(bug_record=record)
    db.disconnect()

