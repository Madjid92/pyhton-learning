
import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(user="postgres",
                        password="1992",
                        host="127.0.0.1",
                        port="5432",
                        database="location")

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a query
cur.execute("SELECT * FROM public.voiture")

# Retrieve query results
#records = cur.fetchall()

#for i in range(len(records)) :
#   print(records[i])