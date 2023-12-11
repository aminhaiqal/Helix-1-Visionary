from flask import request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from dotenv import load_dotenv
from services import doc_processing, img_processing
import os

from . import app  # Import the Flask app instance

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'mediaFile' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['mediaFile']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file and allowed_file(file.filename):
        try:
            if file.filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                # Process image
                processed_image = img_processing(file)
            elif file.filename.lower().endswith('.pdf'):
                # Process PDF
                knowledge_base, chunks = doc_processing(file)
            else:
                return jsonify({'error': 'Invalid file type'}), 400

            # Use the configuration for MongoDB
            client = MongoClient(app.config['MONGO_URI'])
            db = client[app.config['DATABASE_NAME']]
            collection_name = app.config['COLLECTION_NAMES']['pdf_data']
            collection = db[collection_name]

            # Save to MongoDB
            data_to_insert = {
                'knowledge_base': knowledge_base,
                'chunks': chunks
            }

            result = collection.insert_one(data_to_insert)

            return jsonify({'message': 'File uploaded successfully', 'document_id': str(result.inserted_id)}), 200

        except Exception as e:
            return jsonify({'error': str(e)}), 400

    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True)
