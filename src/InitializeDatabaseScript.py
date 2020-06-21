import psycopg2
import src.DBConfig as config
import src.DebugLogFile as Dfl

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Database:
    def __init__(self):
        self.db_server_conn = None
        self.database_params = None
        self.db_cursor = None
        self.db_name = None
        self.bug_table_name = "Bugs"
        self. debugLogFile = Dfl.debugLogFile()

    # Open a connection to the host server that the database is stored on.
    def connect(self):
        try:
            # Get the server params from Database.ini
            params = config.config('postgres_server')
            # Create a connection to the posgresql database server
            self.db_server_conn = psycopg2.connect(**params)

            self.db_cursor = self.db_server_conn.cursor()
            # Print PostgreSQL Connection properties
            print(self.db_server_conn.get_dsn_parameters(), "\n")

            # Print PostgreSQL version
            # possibly do not need class based cursor so this might need to be removed.
            # TODO

            self.db_cursor.execute("SELECT version();")
            record = self.db_cursor.fetchone()
            print("You are connected to - ", record, "\n")

        except (Exception, psycopg2.Error) as e:
            self.debugLogFile.writeToFile("Error while connecting to PostgreSQL " + str(e))
            # raise Exception("Error while connecting to PostgreSQL " + str(e))

            # print("Error while connecting to PostgreSQL", error)

    # Disconnect is its own function so that the connection to the
    # databases server can remain open while the database and table are being
    # queried.
    def disconnect(self):
        if self.db_server_conn:
            self.db_cursor.close()
            self.db_server_conn.close()
            print("PostgreSQL connection is closed")

    def create_database(self):
        if self.db_server_conn:
            try:
                self.database_params = config.config('postgres_db')
                self.db_server_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                database_name = self.database_params.get('database')
                sqlCreateDatabase = "create database " + database_name + ""
                self.db_cursor.execute(sqlCreateDatabase)

            except (Exception, psycopg2.Error) as e:
                self.debugLogFile.writeToFile("Could not create Database " + str(e))

    def create_table(self):
        # need to connect to the database that I am actually creating the table in.
        conn = None
        cursor = None
        try:
            # connect to the database on the postgres server.
            conn = psycopg2.connect(**self.database_params)
            # conn = self.database_connect()
            # once we are connected to the database that we created on the postgreSQL server
            # we can create a table in that database.
            cursor = conn.cursor()
            # self.bug_table_name =

            # basic Table
            table = ("CREATE TABLE " + self.bug_table_name + """ (
                        bug_title text NULL,
                        bug_description text NULL,
                        bug_traceback_info text NULL,
                        bug_resolved BOOL NULL,
                        PRIMARY KEY (bug_title)
                        ); """)
            # execute the sql query
            cursor.execute(table)
            # commit the changes so they are saved
            conn.commit()

        except (Exception, psycopg2.Error) as e:
            self.debugLogFile.writeToFile("Could not create table " + str(e))

        finally:
            # close the connection to the database to prevent memory leaks
            if conn:
                cursor.close()
                conn.close()

    def list_insert(self, bug_record):
        conn = None
        cursor = None
        try:
            conn = psycopg2.connect(**self.database_params)
            cursor = conn.cursor()
            # sql_values = []
            # for item in bug_record:
                # sql_values.append(item)
            # insert_values = (bug_record[0], bug, "traceback info test", False)
            insert_query = (" INSERT INTO " + self.bug_table_name + """(
                            bug_title, 
                            bug_description, 
                            bug_traceback_info, 
                            bug_resolved) 
                            VALUES (%s, %s, %s, %s) """)

            cursor.execute(insert_query, bug_record)
            conn.commit()
            # count = cursor.rowcount
            # print(count, "Record inserted successfully into table.")

        except (Exception, psycopg2.Error) as e:
            self.debugLogFile.writeToFile("Could not insert record into table " + str(e))

        finally:
            if conn:
                cursor.close()
                conn.close()

    # update item in table
    # the title of the bug is the primary key. To update date a specific record enter the title of the bug.
    def update_record(self, title):
        conn = None
        cursor = None
        try:
            conn = psycopg2.connect(**self.database_params)
            cursor = conn.cursor()

            # When a bug is updated it means that it has been resolved so the bug_resolve flag is switched
            # from false to true.
            sql_update_query = (" UPDATE " + self.bug_table_name + """
                                SET bug_resolved = True
                                WHERE bug_resolved = %s
                                AND bug_title = %s """)

            update_values = (False, title)
            cursor.execute(sql_update_query, update_values)
            conn.commit()

            count = cursor.rowcount
            print(count, "Record updated successfully")

        except (Exception, psycopg2.Error) as e:
            self.debugLogFile.writeToFile("Could not update record in table " + str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    # Retrieves all records with the same bug_title, bug_title is the primary key.
    def retrieve_record(self, title):
        conn = None
        cursor = None
        try:
            conn = psycopg2.connect(**self.database_params)
            cursor = conn.cursor()

            sql_retrieve_query = ("SELECT * from " + self.bug_table_name + """
                                WHERE bug_title = %s """)

            # record_name has to be a tuple or list to convert properly to execute the query.
            sql_query_values = (title,)
            cursor.execute(sql_retrieve_query, sql_query_values)
            # retrieves all the records that were queried.
            table_record = cursor.fetchall()

            for row in table_record:
                print("Title: ", row[0])
                print("Description: ", row[1])
                print("Traceback Info: ", row[2])
                print("Resolved: ", row[3])

        except (Exception, psycopg2.Error) as e:
            self.debugLogFile.writeToFile("Could not retrieve record " + str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

    # This will list all the database on the postgresql server.
    def list_dbs(self):
        if self.db_server_conn:
            self.db_cursor.execute("""SELECT d.datname as "Name",
                pg_catalog.pg_get_userbyid(d.datdba) as "Owner",
                pg_catalog.pg_encoding_to_char(d.encoding) as "Encoding",
                d.datcollate as "Collate",
                d.datctype as "Ctype",
                pg_catalog.array_to_string(d.datacl, E'\n') AS "Access privileges"
                FROM pg_catalog.pg_database d
                ORDER BY 1;""")
            for datname in self.db_cursor:
                print(datname)
