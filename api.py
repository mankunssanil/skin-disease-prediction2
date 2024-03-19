from flask import Flask,  render_template, request
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import cv2

app = Flask(__name__)

# Load the trained model
model = load_model('skin_cancer.h5')

# Define the classes
classes = {
    0: 'akiec',
    1: 'bcc',
    2: 'bkl',
    3: 'df',
    4: 'nv',
    5: 'vasc',
    6: 'mel'
}
@app.route('/')
def index():
    return render_template('nextpage.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    file = request.files['image']
    
    # Read the image
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    
    # Resize the image to match the input shape of the model
    img_resized = cv2.resize(img, (28, 28))
    
    # Preprocess the image (if needed)
    # Your preprocessing steps here
    
    # Make prediction
    prediction = model.predict(np.expand_dims(img_resized, axis=0))
    
    # Get the predicted class
    predicted_class = classes[np.argmax(prediction)]
    
    # Get the confidence score
    confidence_score = np.max(prediction)
    
    # Prepare the response
    response = {
        'predicted_class': predicted_class,
        'confidence_score': float(confidence_score)
    }
    
    
    return render_template('nextpage.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
