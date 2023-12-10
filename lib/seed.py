import random
from config import *

fake = Faker()
# Seed the database with 4 users
print("=== Seeding Started ===")
def seed_users_and_posts():
    for _ in range(4):
        user = User(
            username=fake.user_name(),
            email=fake.email(),
            phone=fake.random_number(digits=10)
        )
        session.add(user)


    # Seed the database with 20 posts - 5 posts for each user - that is after fetching all users 
    for user in session.query(User).all():
        for _ in range(5):
            post = Post(
                title=fake.sentence(),
                user=user,
                description=fake.paragraph(),
                is_active=random.choice([True, False])
                # random is used to randomise True and False
            )
            session.add(post)
    session.commit()


seed_users_and_posts()   
session.close()
print("=== Done seeding ===")
