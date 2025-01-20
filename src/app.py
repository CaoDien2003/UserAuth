from flask import Flask
from flask_pymongo import PyMongo
from src.auth.routes import auth_bp

app = Flask(__name__)
app.config.from_object("src.auth.config.Config")

# MongoDB connection
mongo = PyMongo(app, uri=app.config["MONGO_URI"])
db = mongo.cx[app.config["DB_NAME"]]  # Access the database by name

# Pass the database instance to Blueprints
app.config["DB"] = db

# Register Blueprints
app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)
