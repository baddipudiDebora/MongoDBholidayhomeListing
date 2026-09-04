import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Config
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback_default_secret")

# Ensure timeout parameter is attached
mongo_uri = os.environ.get("MONGO_URI", "")
if mongo_uri and "serverSelectionTimeoutMS" not in mongo_uri:
    separator = "&" if "?" in mongo_uri else "?"
    mongo_uri += f"{separator}serverSelectionTimeoutMS=5000"

app.config["MONGO_URI"] = mongo_uri

# Initialize PyMongo without binding application context immediately
mongo = PyMongo()

def get_db():
    if "db" not in mongo.__dict__ or mongo.db is None:
        mongo.init_app(app)
    return mongo.db

# Routes
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/viewlisting")
def view_listing():
    try:
        db = get_db()
        listings = list(db.listings.find()) if db is not None else []
    except Exception as e:
        print(f"Database error: {e}")
        listings = []
    return render_template("ad-list-view.html", listings=listings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
