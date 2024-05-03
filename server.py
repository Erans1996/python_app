from flask import Flask, request
import subprocess

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return open('templates/index.html').read()

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    file_path = f"{app.config['UPLOAD_FOLDER']}/{file.filename}"
    file.save(file_path)

    # Execute the Python script to obtain the file path
    output = subprocess.run(['python', 'script.py', file_path], capture_output=True, text=True)
    file_path_result = output.stdout.strip()

    return file_path_result

if __name__ == '__main__':
    app.run(debug=True)
