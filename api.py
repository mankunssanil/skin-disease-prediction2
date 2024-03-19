import os
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
UPLOAD_FOLDER = "skin main project.ipynb"
DEVICE = "cuda"
MODEL = None


@app.router("/", methods=["GET", "POST"])
def upload_predict():
    if request.method == "POST":
    image_file = request.files["image"]
    if imade_file:
        image_location = os.path.join(
            UPLOAD_FOLDER,
            image_file.filename
        )
        image_file.save(image_location)
        return render_template("nextpage.html", prediction=1)
    return render_template("nextpage.html", prediction=0)
    

if __name__ == "__main__":
    app.run(port=12000, debug=True)

