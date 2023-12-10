from flask import Blueprint, request, jsonify
from flask_pymongo import PyMongo
from werkzeug.utils import secure_filename
from app.services import doc_ask
import os

upload_route = Blueprint('upload_route', __name__)

mongo = PyMongo()

@upload_route.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        # Save the uploaded file to the upload folder
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Process the PDF and extract vector data using the document service
        knowledge_base, chunks = doc_ask(file_path)

        # Save the knowledge base and file information to MongoDB
        document = {
            'filename': filename,
            'knowledge_base': knowledge_base.to_dict(),
            'chunks': chunks
        }

        mongo.db.documents.insert_one(document)

        # Remove the uploaded file after processing
        os.remove(file_path)

        return jsonify({'message': 'File uploaded successfully'}), 200

    return jsonify({'error': 'Internal server error'}), 500
