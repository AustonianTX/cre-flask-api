from flask import Flask, request
from werkzeug.utils import secure_filename
import json

from pdf import extract_text

from ai import process_text

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload():

    uploaded_file = request.files['brochure']

    text = extract_text(uploaded_file)

    response_text = process_text(text)

    response = json.loads(response_text)

    uploaded_file.save(
        f'uploads/{secure_filename(response.get("address"))}.pdf')

    return response
