from flask import current_app

def get_db():
    """Get the MongoDB database instance."""
    return current_app.config["DB"]

def register_user(username, password):
    """Register a new user."""
    db = get_db()
    user = {"username": username, "password": password}
    db.users.insert_one(user)

def find_user_by_username(username):
    """Find a user by username."""
    db = get_db()
    return db.users.find_one({"username": username})
