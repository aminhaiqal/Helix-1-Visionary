from app import mongo

def get_message_collection():
    return mongo.db.messages