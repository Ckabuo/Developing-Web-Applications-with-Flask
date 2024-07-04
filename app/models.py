from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class Product(db.Model):
    # Primary key for the Product table
    id = db.Column(db.Integer, primary_key = True)

    # Title of the product, cannot be null
    title = db.Column(db.String(50), nullable = False)

    # Description of the product, cannot be null
    description = db.Column(db.String(100), nullable = False)

    # Price of the product, cannot be null
    price = db.Column(db.Float, nullable = False)

    # Category to which the product belongs, cannot be null
    category = db.Column(db.String(50), nullable = False)

    # Image URL/path for the product, cannot be null
    image = db.Column(db.String(50), nullable = False)

class User(db.Model, UserMixin):
    # Primary key for the User table
    id = db.Column(db.Integer, primary_key = True)

    # Username of the user, cannot be null
    username = db.Column(db.String(50), nullable = False)

    # Hashed password of the user, cannot be null
    password = db.Column(db.String(100), nullable = False)

    # Email of the user, cannot be null
    email = db.Column(db.String(50), nullable = False)

    # Role of the user (e.g., admin, customer), cannot be null
    role = db.Column(db.String(50), nullable = False)