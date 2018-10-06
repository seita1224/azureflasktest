from flask import Flask,render_template
from app.models import bitflyer_api
app = Flask(__name__,template_folder='app/templates/')


# ログインページ
@app.route('/login')
def home():
    title = "ログインページ"
    return render_template('login.html', title=title, url="")


# メニュー
@app.route('/menu')
def menu():
    return render_template('index.html', url="https://api.bitflyer.jp/v1/getexecutions")


if __name__ == '__main__':
  app.run()
