from flask import Flask,render_template
from app.models import bitflyer_api
app = Flask(__name__,template_folder='app/templates/')

@app.route('/')
def home():
    board = bitflyer_api.bitFlyer_use_api()
    print(str(board.borad()))
    return render_template('index.html', url="https://api.bitflyer.jp/v1/getexecutions", message=str(board.borad()))

if __name__ == '__main__':
  app.run()
