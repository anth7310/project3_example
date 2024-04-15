
import sqlalchemy
from sqlalchemy import text

def create_mock_data_in_sqlite3():
    """ Create mock data in the sqlite3 database
    """
    # Create a connection to the database
    conn = sqlalchemy.create_engine('sqlite:///data.sqlite3').connect()
    # Execute a query
    conn.execute(text('DROP TABLE IF EXISTS country'))
    conn.execute(text('CREATE TABLE country (Country TEXT, Value INTEGER)'))
    conn.execute(text('INSERT INTO country (Country, Value) VALUES ("United States", 12394)'))
    conn.execute(text('INSERT INTO country (Country, Value) VALUES ("Russia", 6148)'))
    conn.execute(text('INSERT INTO country (Country, Value) VALUES ("Germany (FRG)", 1653)'))
    conn.execute(text('INSERT INTO country (Country, Value) VALUES ("France", 2162)'))
    conn.execute(text('INSERT INTO country (Country, Value) VALUES ("United Kingdom", 1214)'))
    conn.execute(text('INSERT INTO country (Country, Value) VALUES ("China", 1131)'))
    conn.execute(text('INSERT INTO country (Country, Value) VALUES ("Spain", 814)'))
    conn.execute(text('INSERT INTO country (Country, Value) VALUES ("Netherlands", 1167)'))
    conn.execute(text('INSERT INTO country (Country, Value) VALUES ("Italy", 660)'))
    

def get_data_from_sqlite3():
    """ Return data for the country chart
    """
    # Create a connection to the database
    conn = sqlalchemy.create_engine('sqlite:///data.sqlite3').connect()
    # Execute a query
    result = conn.execute('SELECT * FROM country')
    # Fetch the results
    data = result.fetchall()
    # Close the connection
    conn.close()
    return data

if __name__ == "__main__":
    create_mock_data_in_sqlite3()