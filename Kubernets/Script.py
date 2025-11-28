from flask import Flask
app = Flask(__name__)
@app.route('/')
def retruntext():
    return "Hello this is I'm"
app.run(debug=True, host='0.0.0.0', port=5000)
