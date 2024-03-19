from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the uploaded image
    file = request.files['file']
    # Perform prediction here
    # For demonstration purposes, let's assume you get the prediction result as a string
    prediction_result = "Melanoma"  # Replace this with your actual prediction result
    return render_template('prediction_result.html', prediction=prediction_result)

if __name__ == '__main__':
    app.run(debug=True)
