from app import mongo

def get_document_collection():
    return mongo.db.documents