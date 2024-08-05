from flask import Flask, request, render_template
from scripts.preprocess import preprocess_text
from scripts.similarity import detect_plagiarism

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        content = file.read().decode('utf-8')
        preprocessed_content = preprocess_text(content)

        # Dummy database documents for testing
        database_documents = [
            {'id': 1, 'content': 'This is a sample document in the database.'},
            {'id': 2, 'content': 'Another academic document for testing.'}
        ]

        results = detect_plagiarism(preprocessed_content, database_documents)
        return render_template('results.html', results=results)

    return 'No file uploaded', 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
