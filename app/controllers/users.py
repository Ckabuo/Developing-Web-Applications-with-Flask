from models import User, db
from sqlalchemy import exc

def get_users():
    # Retrieve all users from the User table
    users = User.query.all()
    return users

def get_user(id):
    # Retrieve a single user by their ID
    user = User.query.get(id)
    return user

def add_user(username, password, email, role):
    try:
        # Create a new user instance
        new_user = User(
            username = username,
            password = password,
            email = email,
            role = role
        )
        # Add the new user to the session and commit
        db.session.add(new_user)
        db.session.commit()
        return True
    except exc.IntegrityError:
        # Rollback the session in case of an integrity error
        db.session.rollback()
        return False

def update_user(id, username, password, email, role):
    try:
        # Retrieve the user to update by their ID
        user = User.query.get(id)
        # Update the user's information
        user.username = username
        user.password = password
        user.email = email
        user.role = role
        # Commit the changes
        db.session.commit()
        return True
    except exc.IntegrityError:
        # Rollback the session in case of an integrity error
        db.session.rollback()
        return False

def delete_user(id):
    try:
        # Retrieve the user to delete by their ID
        user = User.query.get(id)
        # Delete the user from the session and commit
        db.session.delete(user)
        db.session.commit()
        return True
    except exc.IntegrityError:
        # Rollback the session in case of an integrity error
        db.session.rollback()
        return False

def get_user_by_username(username):
    # Retrieve a user by their username
    user = User.query.filter_by(username = username).first()
    return user