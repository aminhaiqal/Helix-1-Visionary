from flask import Flask, request, jsonify
from app.services import doc_ask, user_query

app = Flask(__name__)
knowledge_base = None


@app.route('/')
def home():
    return 'Hello, Docker!'


@app.before_first_request
def load_knownledge_base(pdf_path):
    global knowledge_base
    knowledge_base = doc_ask(pdf_path)


@app.route('/chatroom', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if user_message:
        response = user_query(user_message, knowledge_base)
        return jsonify(response)
    else:
        return jsonify({'error': 'No message provided'}), 400 


if __name__ == '__main__':
    app.run(debug=True)