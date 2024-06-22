from flask import Flask, request, jsonify
from parser_1 import parse_pdf_resume, parse_docx_resume, parse_with_openai, parse_text_resume
from db import get_db

app = Flask(__name__)
db = get_db()

@app.route('/parse', methods=['POST'])
def parse_resume():
    print("Received POST request to /parse")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = file.filename
    file_content = file.read()

    if filename.endswith('.pdf'):
        data = parse_pdf_resume(file_content)
    elif filename.endswith('.docx'):
        data = parse_docx_resume(file_content)
    elif filename.endswith('.txt'):
        data = parse_text_resume(file_content.decode())
    else:
        return jsonify({'error': 'Unsupported file format'}), 400

    # Optionally, use AI for more advanced parsing
    ai_data = parse_with_openai(file_content.decode())
    data.update(ai_data)

    # Save to MongoDB
    db.resumes.insert_one(data)

    return jsonify(data)

@app.route('/taxonomy', methods=['GET'])
def get_taxonomy():
    print("Received GET request to /taxonomy")
    taxonomy = db.taxonomy.find()
    return jsonify(list(taxonomy))

if __name__ == '__main__':
    app.run(debug=True)
