from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.transposition import TranspositionCipher
from cipher.railfence import RailFenceCipher
from cipher.playfair import PlayFairCipher


app = Flask(__name__)

# Trang chủ
@app.route("/")
def home():
    return render_template('index.html')

# Giao diện Caesar Cipher
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

# Mã hoá Caesar Cipher
@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

# Giải mã Caesar Cipher
@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"


@app.route("/vigenere")
def vigenere():
    return render_template("vigenere.html")

@app.route("/encrypt_vigenere", methods=["POST"])
def encrypt_vigenere():
    text = request.form["inputPlainText"]
    key = request.form["inputKey"]
    cipher = VigenereCipher()
    encrypted = cipher.vigenere_encrypt(text, key)
    return f"<h3>Encrypted: {encrypted}</h3><a href='/vigenere'>Back</a>"

@app.route("/decrypt_vigenere", methods=["POST"])
def decrypt_vigenere():
    text = request.form["inputCipherText"]
    key = request.form["inputKey"]
    cipher = VigenereCipher()
    decrypted = cipher.vigenere_decrypt(text, key)
    return f"<h3>Decrypted: {decrypted}</h3><a href='/vigenere'>Back</a>"

@app.route("/railfence")
def railfence():
    return render_template("railfence.html")

@app.route("/encrypt_railfence", methods=["POST"])
def encrypt_railfence():
    text = request.form["inputPlainText"]
    key = int(request.form["inputKey"])
    cipher = RailFenceCipher()
    result = cipher.rail_fence_encrypt(text, key)
    return f"<h3>Encrypted: {result}</h3><a href='/railfence'>Back</a>"

@app.route("/decrypt_railfence", methods=["POST"])
def decrypt_railfence():
    text = request.form["inputCipherText"]
    key = int(request.form["inputKey"])
    cipher = RailFenceCipher()
    result = cipher.rail_fence_decrypt(text, key)
    return f"<h3>Decrypted: {result}</h3><a href='/railfence'>Back</a>"

@app.route("/playfair")
def playfair():
    return render_template("playfair.html")

@app.route("/encrypt_playfair", methods=["POST"])
def encrypt_playfair():
    text = request.form["inputPlainText"]
    key = request.form["inputKey"]
    cipher = PlayFairCipher()
    result = cipher.playfair_encrypt(text, key)
    return f"<h3>Encrypted: {result}</h3><a href='/playfair'>Back</a>"

@app.route("/decrypt_playfair", methods=["POST"])
def decrypt_playfair():
    text = request.form["inputCipherText"]
    key = request.form["inputKey"]
    cipher = PlayFairCipher()
    result = cipher.playfair_decrypt(text, key)
    return f"<h3>Decrypted: {result}</h3><a href='/playfair'>Back</a>"

@app.route("/transposition")
def transposition():
    return render_template("transposition.html")

@app.route("/encrypt_transposition", methods=["POST"])
def encrypt_transposition():
    text = request.form["inputPlainText"]
    key = request.form["inputKey"]
    cipher = TranspositionCipher()
    result = cipher.encrypt(text, key)
    return f"<h3>Encrypted: {result}</h3><a href='/transposition'>Back</a>"

@app.route("/decrypt_transposition", methods=["POST"])
def decrypt_transposition():
    text = request.form["inputCipherText"]
    key = request.form["inputKey"]
    cipher = TranspositionCipher()
    result = cipher.decrypt(text, key)
    return f"<h3>Decrypted: {result}</h3><a href='/transposition'>Back</a>"

# Chạy ứng dụng
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)
