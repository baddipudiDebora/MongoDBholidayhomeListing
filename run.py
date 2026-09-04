import os
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)

# Secret key configuration for sessions
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "fallback_default_secret")

# Ensure serverSelectionTimeoutMS is set to prevent Vercel 30s function hangs
mongo_uri = os.environ.get("MONGO_URI", "")
if mongo_uri and "serverSelectionTimeoutMS" not in mongo_uri:
    separator = "&" if "?" in mongo_uri else "?"
    mongo_uri += f"{separator}serverSelectionTimeoutMS=5000"

app.config["MONGO_URI"] = mongo_uri
mongo = PyMongo(app)

# Standard App Routes
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/viewlisting")
def view_listing():
    # Example collection fetch
    listings = list(mongo.db.listings.find()) if mongo.db else []
    return render_template("ad-list-view.html", listings=listings)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)