import os
from urllib.parse import urlparse
import psycopg2

url = (os.environ['BLOG_DATABASE_URL'])
result = urlparse(url)
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname

def get_database_connection():
    connection = psycopg2.connect(
        database=database,
        user=username,
        password=password,
        host=hostname
    )
    return connection