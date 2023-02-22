
import psycopg2
import json


def save_json_to_table(json_data):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        user="your_postgres_username",
        password="your_postgres_password",
        host="db",
        port="5432",
        database="your_postgres_database_name"
    )



    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Define the SQL command to create the table (if it doesn't already exist)
    create_table_command = """
    CREATE TABLE IF NOT EXISTS mytable1 (
        id SERIAL PRIMARY KEY,
        title TEXT,
        url TEXT,
        image TEXT
    );
    """

    # Execute the create table command
    cur.execute(create_table_command)

    # Define the SQL command to insert data into the table
    insert_data_command = """
    INSERT INTO mytable1 (title, url, image)
    VALUES (%s, %s, %s);
    """
    with open('static/data.json') as f:
        data = json.load(f)

    # Print the data to verify that it has been loaded correctly

    for item in data:
        values = (item["title"], item["url"], item["image"])
        cur.execute(insert_data_command, values)

    # Commit the changes to the database and close the cursor and connection
    conn.commit()
    cur.close()
    conn.close()
