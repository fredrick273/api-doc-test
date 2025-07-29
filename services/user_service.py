users = []

def create_user(username, email):
    user = {"id": len(users)+1, "username": username, "email": email}
    users.append(user)
    return user

def get_all_users():
    return users
