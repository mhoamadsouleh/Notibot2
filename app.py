from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    if f.filename.endswith('.py'):
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
    return redirect('/')

if __name__ == "__main__":
    app.run()