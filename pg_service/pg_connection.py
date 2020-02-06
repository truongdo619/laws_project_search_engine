import psycopg2
from psycopg2 import pool
try:
    postgreSQL_pool = psycopg2.pool.SimpleConnectionPool(1, 20,user = "postgres",
                                              password = "12345678",
                                              host = "112.137.142.8",
                                              port = "5433",
                                              database = "lawtech")
    if(postgreSQL_pool):
        print("Connection pool created successfully")

    # Use getconn() to Get Connection from connection pool

except (Exception, psycopg2.DatabaseError) as error :
    print ("Error while connecting to PostgreSQL", error)
