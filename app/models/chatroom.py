from app import mongo

def get_chatroom_collection():
    return mongo.db.chatrooms