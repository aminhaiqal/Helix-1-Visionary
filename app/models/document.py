from app import mongo

def get_document_collection():
    return mongo.db.documents

def save_document(knowledge_base, chunks):
    document_collection = get_document_collection()
    
    document = {
        'knowledge_base': knowledge_base,
        'chunks': chunks
    }
    
    document_collection.insert_one(document)
    
    return document