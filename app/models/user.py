from app import mongo

def get_user_collection():
    return mongo.db.users