from flask import Flask, request, send_file, render_template
import qrcode
import io

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_qr():
    url = request.form.get("url")

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img_io = io.BytesIO()
    img.save(img_io, "PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
