from flask import Flask
import json
import db

app = Flask(__name__)

@app.route("/drinking-data")
def drinking_data():
    return json.dumps(db.get_movement_data())

if __name__ == '__main__':
    app.run()
    print("hi")