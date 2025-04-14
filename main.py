import json
import os
from flask import Flask, send_file, abort

app = Flask(__name__)


def load_users():
    with open("users.json", "r") as file:
        users = json.load(file)
        return users
def load_views():
    with open("view.json", "r") as file:
        return json.load(file)

def save_views(data):
    with open("view.json", "w") as file:
        json.dump(data, file, indent=4)

@app.route("/home")
def home():
    views = load_views()
    views["home"] += 1
    save_views(views)
    return f"<h2>Home sahifasi: {views['home']} ta tashrif</h2>"


@app.route("/about")
def about():
    views = load_views()
    views["about"] += 1
    save_views(views)
    return f"<h2>About sahifasi: {views['about']} ta tashrif</h2>"

USERS_FILE = 'users.json'

def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as f:
        return json.load(f)

def save_users(data):
    with open(USERS_FILE, 'w') as f:
        json.dump(data, f, indent=4)

@app.route('/u/<int:user_id>')
def user_page(user_id):
    views = load_views()
    users = load_users()  # users.json faylni o‘qiydi

    user_id_str = str(user_id)

    # u_totalni oshiramiz (view.json)
    views['u_total'] += 1
    if user_id_str not in views['u_ids']:
        views['u_ids'][user_id_str] = 0
    views['u_ids'][user_id_str] += 1

    # foydalanuvchi mavjud bo‘lsa, view ni oshiramiz (users.json)
    if user_id_str in users:
        users[user_id_str]['view'] += 1
        save_users(users)
    else:
        return "Bunday foydalanuvchi topilmadi", 404

    save_views(views)

    user = users[user_id_str]
    return f"""
    Ism: {user['ism']}<br>
    Yoshi: {user['yoshi']}<br>
    Roli: {user['rol']}<br>
    Ko‘rilganlar soni: {user['view']}
    """


@app.route("/")
def index():
    return """
    <h1>Asosiy Sahifa</h1>
    <ul style="font-size: 20px;">
        <li><a href="/home">🏠 Home</a></li>
        <li><a href="/about">ℹ️ About</a></li>
        <li><a href="/bobur">👤 Bobur</a></li>
        <li><a href="/saloh">👤 Saloh</a></li>
        <li><a href="/admin/1">👨‍💻 get_admin</a></li>   
        <li><a href="/u/123">🆔 Foydalanuvchi ID (misol: 123)</a></li>
    </ul>
    """

@app.route("/admin")
def admin_menu():
    return f"""
    <h2>Admin Ma'lumotlari</h2>
    <h3>Siz admin  bosh panelidasiz</h3>"""

@app.route("/admin/<id>")
def get_admin(id):
    users = load_users()
    user = users.get(id)
    if user and user.get("rol") == "admin":
        return f"""
        <h2>Admin Ma'lumotlari</h2>
        <p>
            Ism: {user['ism']}<br>
            Yoshi: {user['yoshi']}<br>
            Roli: {user['rol']}
        </p>
        """
    else:
        return "<h3>Bunday ID bilan admin topilmadi.</h3>", 404


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
