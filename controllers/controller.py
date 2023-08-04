from app import app

@app.route('/')
def index():
    return "test 2!"