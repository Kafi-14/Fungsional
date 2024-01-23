from flask import Flask, request, jsonify

app = Flask(__name__)


mahasiswa_list = [
    {"id": 1, "nim": "12345", "nama": "Jack", "ipk": 2.9},
    {"id": 2, "nim": "54321", "nama": "Jill", "ipk": 3.1},
    {"id": 3, "nim": "13542", "nama": "Golliath", "ipk": 3.5},
]


@app.route("/", methods=["GET", "POST"])
def index():
    """
    index atau utama.
    """
    if request.method == "GET":
        if len(mahasiswa_list) > 0:
            return jsonify(mahasiswa_list)
        else:
            return "Not Found"

    if request.method == "POST":
        new_id = mahasiswa_list[-1]["id"] + 1
        new_nim = request.form["nim"]
        new_nama = request.form["nama"]
        new_ipk = request.form["ipk"]

        new_mhs = {"id": new_id, "nim": new_nim, "nama": new_nama, "ipk": new_ipk}

        mahasiswa_list.append(new_mhs)
        return jsonify(mahasiswa_list), 200


@app.route("/<name>")
def test(name):
    """
    masukkan nama sesuai link.
    """
    return "Hi, {}".format(name)


@app.route("/test")
def lol():
    """
    test link.
    """
    return "<h1>asndiandoanoiwd</h1>"


@app.route("/mahasiswa", methods=["GET", "POST"])
def mahasiswa():
    """
    nama sesuai data yang tersedia.
    """
    if request.method == "GET":
        if len(mahasiswa_list) > 0:
            return jsonify(mahasiswa_list)
        else:
            return "Not Found"

    if request.method == "POST":
        new_id = mahasiswa_list[-1]["id"] + 1
        new_nim = request.form["nim"]
        new_nama = request.form["nama"]
        new_ipk = request.form["ipk"]

        new_mhs = {"id": new_id, "nim": new_nim, "nama": new_nama, "ipk": new_ipk}

        mahasiswa_list.append(new_mhs)
        return jsonify(mahasiswa_list), 200


if __name__ == "__main__":
    app.run(debug=True)
