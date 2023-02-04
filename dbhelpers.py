import mariadb
import dbcreds

def connect_db():
    try:
        conn = mariadb.connect(
            user=dbcreds.user, 
            password=dbcreds.password, 
            host=dbcreds.host, 
            port=dbcreds.port, 
            database=dbcreds.database, 
            autocommit=True
        )
        cursor = conn.cursor()
        return cursor
    except mariadb.OperationalError as error:
        print("OPERATIONAL ERROR:", error)
    except Exception as error:
        print("UNEXPECTED ERROR:", error)

def disconnect_db(cursor):
    try:
        conn = cursor.connection
        cursor.close()
        conn.close()    
    except mariadb.OperationalError as error:
        print("OPERATIONAL ERROR:", error)
    except mariadb.InternalError as e:
        print("INTERNAL ERROR: ", e)
    except Exception as error:
        print("UNEXPECTED ERROR:", error)

def execute_statement(cursor, statement, args=[]):
    try:
        cursor.execute(statement, args)
        # Looks for valid SQL query to execute
        results = cursor.fetchall()
        return results
    except mariadb.ProgrammingError as e:
        print("Syntax error in your SQL statement: ", e)
    except mariadb.IntegrityError as e:
        print("The statement failed to execute due to integrity error: ", e)
    except mariadb.DataError as e:
        print("DATA ERROR: ", e)
    except Exception as e:
        print("Unexpected error: ", e)

def run_statement(statement, args=[]):
    """
    This function expects a valid SQL statement and an optional list of arguments. It connects to the DB,
    executes the statement and closes the connection.
    If the connection to the DB fails, it returns None without running the statement

    Args:
        statement (str): A valid SWL quey
        args (list, option): The list of arguments. Defaults to []
    """
    cursor = connect_db
    if (cursor == None):
        print("Failed to connect to the DB, statement will not run")
        return None
    result = execute_statement(cursor, statement, args)
    disconnect_db(cursor)
    return result