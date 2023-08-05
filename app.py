from flask import Flask
from controllers import lost_sector_controller

app = Flask(__name__)

@app.route('/')
def home():
    return "yo"

if __name__ == '__main__':
    app.run(debug=True)