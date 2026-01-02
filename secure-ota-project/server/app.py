from flask import Flask, send_file

app = Flask(__name__)

@app.route("/firmware")
def firmware():
    return send_file("encrypted.bin", as_attachment=True)

@app.route("/checksum")
def checksum():
    return send_file("checksum.txt", as_attachment=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
