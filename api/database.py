import pg8000


def get_db_connection():
    connection = pg8000.connect(
        host="localhost",
        database="ai_helpdesk",
        user="postgres",
        password="Bindu@1412",
        port="5432"
    )

    return connection