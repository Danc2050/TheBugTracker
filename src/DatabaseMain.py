import src.InitializeDatabaseScript as DB


if __name__ == "__main__":
    db = DB.Database()
    user_name = "postgres"
    password = "my_secret_password"
    host = "localhost"
    port = 5432
    database_name = "test_db5"
    table_name = "bug_table"
    record = ("bug_title", "bug_description", "bug_traceback_info", False)
    db.connect()
    db.create_database()
    db.create_table()
    db.list_insert(record)

"""
    create_database(db_object)
    insert_test(db_object)
    #update_record(db_object)
    retrieve_record(db_object)

    db_object.list_dbs()
    #answer = input("disconnect?(Y/N): ").upper()
    #if answer == 'Y':
        #disconnect(db_object)
        """
    # disconnect(db_object)
