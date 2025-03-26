from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>Smart & Adaptive Street Light System is Running...</h2>'

if __name__ == '__main__':
    app.run(debug=True)
