from flask import Flask
import os


port = int(os.environ.get('PORT'))

app = Flask(__name__)

@app.route("/")
def home():
    return 'Deployed!'

@app.route('/about')
def about():
    return "This is the about page"












if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)