import psycopg2

try:
    connection = psycopg2.connect(
        host="localhost",
        port="5432",
        database="ai_helpdesk",
        user="postgres",
        password="Bindu@1412"
    )

    print("Connected to PostgreSQL successfully!")

    connection.close()

except Exception as e:
    print("Database connection failed:")
    print(e)