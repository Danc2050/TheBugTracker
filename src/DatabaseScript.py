import psycopg2
import src.DBConfig as config

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Database:
    def __init__(self, debugLogFile):
        self.db_server_conn = None
        self.database_params = None
        self.db_cursor = None
        self.db_name = None
        self.bug_table_name = None
        self.debugLogFile = debugLogFile

    # Open a connection to the host server that the database is stored on.
    def connect(self, server_params):
        """
        Connects to the postgres server that has the bug tracker database on it.
        If an invalid key is provided then a connection will not be made.

        :param server_params: config file key
        :return:
        """
        try:
            # Get the server params from Database.ini
            params = config.config(server_params)
            # Create a connection to the posgresql database server
            self.db_server_conn = psycopg2.connect(**params)
            self.db_cursor = self.db_server_conn.cursor()
        except (Exception, psycopg2.Error) as e:
            self.debugLogFile.writeToFile("Error while connecting to PostgreSQL " + str(e))

    # Disconnect is its own function so that the connection to the
    # databases server can remain open while the database and table are being
    # queried.
    def disconnect(self):
        if self.db_server_conn:
            self.db_cursor.close()
            self.db_server_conn.close()
            print("PostgreSQL connection is closed")

    def create_database(self, database_params):
        if self.db_server_conn:
            try:
                self.database_params = config.config(database_params)
                self.db_server_conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
                database_name = self.database_params.get('database')
                sqlCreateDatabase = "create database " + database_name + ""
                self.db_cursor.execute(sqlCreateDatabase)

            except (Exception, psycopg2.Error) as e:
                self.debugLogFile.writeToFile("Could not create Database " + str(e))

    def create_table(self, table_name):
        # need to connect to the database that I am actually creating the table in.
        conn = None
        cursor = None
        self.bug_table_name = table_name
        try:
            # connect to the database on the postgres server.
            conn = psycopg2.connect(**self.database_params)
            # once we are connected to the database that we created on the postgreSQL server
            # we can create a table in that database.
            cursor = conn.cursor()
            # basic Table
            table = ("CREATE TABLE " + table_name + """ (
                        Title text NULL,
                        Traceback_info text NULL,
                        Resolved BOOL NULL,
                        Version text NULL,
                        PRIMARY KEY (Title)
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

    def list_insert(self, bugRecordDTO):
        conn = None
        cursor = None
        try:
            conn = psycopg2.connect(**self.database_params)
            cursor = conn.cursor()
            insert_query = (" INSERT INTO " + self.bug_table_name + """(
                            Title,  
                            Traceback_info, 
                            Resolved,
                            Version) 
                            VALUES (%s, %s, %s, %s); """)

            cursor.execute(insert_query,
                           (bugRecordDTO.title,
                            bugRecordDTO.tracebackInfo, bugRecordDTO.resolved, bugRecordDTO.version))
            conn.commit()
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
                                SET Resolved = True
                                WHERE Resolved = %s
                                AND Title = %s """)

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
                                WHERE Title = %s """)

            # record_name has to be a tuple or list to convert properly to execute the query.
            sql_query_values = (title,)
            cursor.execute(sql_retrieve_query, sql_query_values)
            # retrieves all the records that were queried.
            table_record = cursor.fetchall()


        except (Exception, psycopg2.Error) as e:
            self.debugLogFile.writeToFile("Could not retrieve record " + str(e))
        finally:
            if conn:
                cursor.close()
                conn.close()

            return table_record