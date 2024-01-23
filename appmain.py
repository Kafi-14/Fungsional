from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)


def db_connection():
    """
    koneksi database.
    """
    conn = None
    try:
        conn = pymysql.connect(
            host="sql6.freesqldatabase.com",
            database="sql6679140",
            user="sql6679140",
            password="68tnEMKUJZ",
            cursorclass=pymysql.cursors.DictCursor,
        )
    except pymysql.Error as e:
        print(e)
    return conn


@app.route("/", methods=["GET", "POST"])
def index():
    """
    index atau utama.
    """
    conn = db_connection()
    cursor = conn.cursor()
    if request.method == "GET":
        cursor.execute("SELECT * FROM game2")
        game = [
            dict(
                id=row["id"], nama=row["nama"], genre=row["genre"], rating=row["rating"]
            )
            for row in cursor.fetchall()
        ]
        if game:
            return jsonify(game)
        else:
            return jsonify({"error": "data tidak ditemukan"}), 404

    if request.method == "POST":
        add_nama = request.form["nama"]
        add_genre = request.form["genre"]
        add_rating = request.form["rating"]

    query_insert = """ INSERT INTO game2 (nama, genre, rating) VALUES (%s,%s,%s) """
    cursor.execute(query_insert, (add_nama, add_genre, add_rating))
    conn.commit()
    return "Data berhasil Diinput"


if __name__ == "__main__":
    app.run(debug=True)
