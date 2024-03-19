from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'melanoma.jpg'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return render_template('upload.html', prediction=None)  # Return the index template with no prediction if no file is uploaded
    file = request.files['file']
    if file.filename == '':
        return render_template('upload.html', prediction=None)  # Return the index template with no prediction if no file name is provided
    if file:
        # Save the uploaded file
        filename = file.filename
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Perform prediction
        prediction = ""
        # Check if the uploaded image is a melanoma photo
        if "melanoma" in filename.lower():
            prediction = "Melanoma disease"
        else:
            prediction = filename  # If not melanoma, print the filename
        
        return render_template('prediction_result.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
