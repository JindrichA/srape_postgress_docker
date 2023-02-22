
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



import_data_to_postgresql('static/data.json', 'your_postgres_database_name', 'your_postgres_username', 'your_postgres_password', '0.0.0.0')