from main import create_user, fetch_all_users_with_posts, fetch_posts_by_is_active, get_user, get_user_posts, update_user, delete_user
from main import create_post, get_post, update_post, delete_post


# ===== USER CRUD
print(">>>>>>>>>>>> USER OPERATIONS <<<<<<<<<<<")
print("***** Creating new user *****")
user = create_user("Mike aJ", "mike@developerske.com", +2547888999)
print(f"Created User => {user.username}")

print("")
print("***** Fetching user by id *****")
retrieved_user = get_user(user.id) 
print(f"Retrieved User => {retrieved_user.username}, ID => {retrieved_user.id}, phone => {retrieved_user.phone} ")

print("***** Update User *****")
updated_user_data = {'username': 'Kelvi', 'email': 'kelvink@developerske.com', "phone": +254700000000}
updated_user = update_user(user.id, updated_user_data)
print(f"Updated User => {updated_user.username}, Email => {updated_user.email}")


user_posts = get_user_posts(user.id) #you can pass a random id so long it is available in the db
print(f"Posts related to {user.username}: {[post.title for post in user_posts]}")

print("***** Fetch all users with their own posts *****")
users_with_posts = fetch_all_users_with_posts() # Fetch all users combined with their related posts
for user in users_with_posts:
    print(f"User: {user.username}")
    for post in user.posts:
        print(f"  Post: {post.title}")

print("***** Delete user by id *****")
deleted_user = delete_user(user.id)
print(f"Deleted User => {deleted_user.username}, ID => {deleted_user.id}")


# ====== POSTS CRUD
print()
print(">>>>>>>>>>>> POST OPERATIONS <<<<<<<<<<<")
user = create_user("Mercy Mikes", "mmikes@developerske.com", +25478889909)

print("***** Create post *****")
post = create_post("First Post", user.id, "This is the content of the first post.")
print(f"Created Post => {post.title}, ID => {post.id}")

print("***** Get a single post *****")
retrieved_post = get_post(post.id)
print(f"Retrieved Post => {retrieved_post.title}, ID => {retrieved_post.id}")

print("***** Update post *****")
updated_post_data = {'title' : 'Updated Post', 'description' : 'Updated description test', "is_active" : False}
updated_post = update_post(post.id, updated_post_data)
print(f"Updated Post => {updated_post.title}")

print("***** Delete post *****")
deleted_post = delete_post(post.id)
print(f"Deleted Post => {deleted_post.title}")

print("***** Fetch all active posts - by is_active column  *****")
active_posts = fetch_posts_by_is_active()
print(f"Active Posts: {[post.title for post in active_posts]}")

