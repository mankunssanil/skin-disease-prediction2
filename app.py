from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'Skin-Disease'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('nextpage.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # Here you would typically perform your prediction
        # For demonstration purposes, let's assume prediction results are stored in a list called 'prediction'
        prediction = [0.2, 0.4, 0.1, 0.3, 0.5, 0.7, 0.6]
        return render_template('nextpage.html', prediction=prediction, filename=filename)

if __name__ == '__main__':
    app.run(debug=True)
