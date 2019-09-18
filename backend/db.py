import psycopg2

connection = psycopg2.connect(
        user = 'postgres',
        password = '',
        host = '127.0.0.1',
        port = '80',
        database = 'postgres'
    )

print("database created")