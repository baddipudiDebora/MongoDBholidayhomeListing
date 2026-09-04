import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback_default_secret")

# Safely sanitize MONGO_URI
mongo_uri = os.environ.get("MONGO_URI", "")
if mongo_uri and "serverSelectionTimeoutMS" not in mongo_uri:
    separator = "&" if "?" in mongo_uri else "?"
    mongo_uri += f"{separator}serverSelectionTimeoutMS=5000"

app.config["MONGO_URI"] = mongo_uri

# Instantiate PyMongo lazily
mongo = PyMongo()

def get_db():
    """Helper function to safely fetch the database instance per request."""
    if mongo.db is None and app.config.get("MONGO_URI"):
        try:
            mongo.init_app(app)
        except Exception as e:
            print(f"MongoDB connection init failed: {e}")
            return None
    return mongo.db

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/viewlisting")
def view_listing():
    listings = []
    db = get_db()
    if db is not None:
        try:
            listings = list(db.listings.find())
        except Exception as e:
            print(f"Database query error: {e}")
    return render_template("ad-list-view.html", listings=listings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)