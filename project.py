from flask import Flask, send_file, abort

app = Flask(__name__)

@app.route("/home")
def home():
    matn = "<h2>Salom! Siz hozir bosh sahifadasiz.</h2>"
    return matn

@app.route("/about")
def about():
    matn_haqida = "<h2>Bu sahifa 'waitress' mavzusi uchun mahalliy sahifa hisoblanadi.</h2>"
    return matn_haqida

@app.route("/bobur")
def bobur():
    rasm_html = '<img src="/bobur/image" alt="Boburning rasmi" width="300"><br>'

    bobur_haqida = """
        <h2>Inomov Bobur</h2>
        <p>
            <span style="font-size: 18px;">Yoshi: 17</span><br>
            <span style="font-size: 18px;">Qiziqishi: Futbol</span><br>
            <span style="font-size: 18px;">Sevimli kasbi: Dasturlash</span><br>
            <span style="font-size: 18px;">Hobbysi: Basketbol o‘ynash</span><br>
            <span style="font-size: 18px;">Ishi: Savdo va Dasturlash</span><br>
            <span style="font-size: 18px;">Asosiy vazifasi: Maktabda o‘qish</span><br>
            <span style="font-size: 18px;">Bo‘sh vaqtida: Kitob o‘qish</span><br>
        </p>
    """
    return rasm_html + bobur_haqida

@app.route("/bobur/image")
def bobur_image():
    try:
        rasm_manzili = r"C:\Users\lwcar\Downloads\bobur.jpg"
        return send_file(rasm_manzili, mimetype="image/jpg")
    except FileNotFoundError:
        abort(404)

@app.route("/saloh")
def saloh():
    rasm_html = '<img src="/saloh/image" alt="Salohiddinning rasmi" width="300"><br>'

    saloh_haqida = """
    <h2>Abdullayev Salohiddin</h2>
    <p>
        <span style="font-size: 18px;">Yoshi: 16</span><br>
        <span style="font-size: 18px;">Qiziqishi: Shaxmat</span><br>
        <span style="font-size: 18px;">Sevimli kasbi: Aniqlanmagan</span><br>
        <span style="font-size: 18px;">Hobbysi: O‘yin o‘ynash</span><br>
        <span style="font-size: 18px;">Asosiy vazifasi: Maktabda o‘qish</span><br>
        <span style="font-size: 18px;">Bo‘sh vaqtida: Video ko‘rish va o‘yin o‘ynash</span><br>
    </p>    
    """
    return rasm_html + saloh_haqida

@app.route("/saloh/image")
def saloh_image():
    try:
        rasm_manzili = r"C:\Users\lwcar\Downloads\saloh.jpg"
        return send_file(rasm_manzili, mimetype="image/jpg")
    except FileNotFoundError:
        abort(404)

if __name__ == "__main__":
    app.run(debug=True)
