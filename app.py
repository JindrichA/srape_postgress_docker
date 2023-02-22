import time
import redis
from flask import Flask, render_template, jsonify
import psycopg2
import json


def import_data_to_postgresql(json_file_path, database, user, password, host="localhost"):
    # připojení k databázi
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    # vytvoření tabulky
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS mytable (
            id SERIAL PRIMARY KEY,
            title TEXT,
            img_url TEXT
        )
    """)
    conn.commit()

    # načtení dat z JSON souboru
    with open(json_file_path) as f:
        data = json.load(f)

    # vložení dat do tabulky
    for record in data['records']:
        cur.execute("""
            INSERT INTO mytable (title, img_url) VALUES (%s, %s)
        """, (record['title'], record['img_url']))
        conn.commit()

    # ukončení spojení s databází
    cur.close()
    conn.close()



def read_postgres_table_and_save_as_json(host, database, user, password, table_name):
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a SELECT statement to retrieve all data from the table
    cur.execute(f"SELECT * FROM {table_name}")

    # Fetch all rows and columns from the result set
    rows = cur.fetchall()

    # Define a list to store the row data
    data = []

    # Loop through each row and add its values to the data list
    for row in rows:
        data.append({
            'column1': row[0],
            'column2': row[1],
            'column3': row[2],
            # add more columns as necessary
        })

    # Close the cursor and connection
    cur.close()
    conn.close()

    # Write the data as a JSON file
    with open(f'{table_name}.json', 'w') as f:
        json.dump(data, f)


app = Flask(__name__)

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/get_json_data')
def get_json_data():
    with open('static/data.json') as json_file:
        data = json.load(json_file)
    return jsonify(data)


"""
@app.route('/test')
def test():

    return render_template('test.html')


@app.route('/uploaded')
def uploaded():
    read_postgres_table_and_save_as_json(
        host='db',
        database='your_postgres_database_name',
        user='your_postgres_username',
        password='your_postgres_password',
        table_name='mytable'
    )
    return render_template('uploaded.html')


@app.route('/data')
def data():
    try:
        import_data_to_postgresql('data.json', 'your_postgres_database_name', 'your_postgres_username', 'your_postgres_password', 'db')
        return ("povedlo se")
    except Exception as e:
        return str(e)

"""
if __name__ == '__main__':
    import_data_to_postgresql('data.json', 'your_postgres_database_name', 'your_postgres_username', 'your_postgres_password', 'db')
    app.run()