from config import *

# ----CRUD Operations for User
def create_user(username, email, phone):
    user = User(username=username, email=email, phone=phone)
    session.add(user)
    session.commit()
    return user

def get_user(user_id):
    return session.query(User).get(user_id)

def update_user(user_id, new_data):
    user = session.query(User).get(user_id)
    if user:
        for key, value in new_data.items():
            setattr(user, key, value)
        session.commit()
    return user

def delete_user(user_id):
    user = session.query(User).get(user_id)
    if user:
        session.delete(user)
        session.commit()
    return user


def get_user_posts(user_id):  # --- get user related posts
    user = session.query(User).get(user_id)
    if user:
        return user.posts
    return []

# def fetch_all_users_with_posts():
#     return session.query(User).options(relationship(User.posts)).all()
def fetch_all_users_with_posts():
    return session.query(User).options(joinedload(User.posts)).all()

# ----CRUD Operations for Post
def create_post(title, user_id, description):
    post = Post(title=title, user_id=user_id, description=description)
    session.add(post)
    session.commit()
    return post

def get_post(post_id):
    return session.query(Post).get(post_id)

def update_post(post_id, new_data):
    post = session.query(Post).get(post_id)
    if post:
        for key, value in new_data.items():
            setattr(post, key, value)
        session.commit()
    return post

def delete_post(post_id):
    post = session.query(Post).get(post_id)
    if post:
        session.delete(post)
        session.commit()
    return post

def fetch_posts_by_is_active(is_active=True):
    return session.query(Post).filter_by(is_active=is_active).all()



session.close()