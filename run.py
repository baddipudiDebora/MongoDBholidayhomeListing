import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Secret key configuration for Flask sessions
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback_default_secret")

# Ensure timeout parameter is present to prevent Vercel 30s hangs
mongo_uri = os.environ.get("MONGO_URI", "")
if mongo_uri and "serverSelectionTimeoutMS" not in mongo_uri:
    separator = "&" if "?" in mongo_uri else "?"
    mongo_uri += f"{separator}serverSelectionTimeoutMS=5000"

app.config["MONGO_URI"] = mongo_uri

# Instantiate PyMongo lazily to prevent crashing during module import
mongo = PyMongo()

def get_db():
    """Safely initialize and return the MongoDB instance on request."""
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
    try:
        db = get_db()
        listings = list(db.listings.find()) if db is not None else []
        return render_template("index.html", listings=listings)
    except Exception as e:
        print(f"Template rendering error on index: {e}")
        return f"<h1>Template Error</h1><p>{e}</p>", 500


@app.route("/viewlisting")
def view_listing():
    try:
        db = get_db()
        listings = list(db.listings.find()) if db is not None else []
        return render_template("ad-list-view.html", listings=listings)
    except Exception as e:
        print(f"Error on viewlisting route: {e}")
        return f"<h1>Error loading listings</h1><p>{e}</p>", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)