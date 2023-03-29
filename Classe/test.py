import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(user="postgres",
                        password="1992",
                        host="127.0.0.1",
                        port="5432")
conn.autocommit = True
# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
#Preparing query to create a database
sql = "CREATE database location_2"

#Creating a database
cur.execute(sql)
print("Database created successfully........")