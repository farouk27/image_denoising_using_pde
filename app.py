from flask import Flask, request, url_for
from flask.templating import render_template
import os
import cv2 as cv
import numpy


app = Flask(__name__)

app.config["IMAGES_UPLOADS"] = "./static/SavedData"
app.config["ALLOWED_IMAGE_EXENTIONS"] = ["PNG", "JPG", "JPEG"]


def allowed_image(file_name):
    if not "." in file_name:
        return False
    # setting the maxsplit parameter to 1, will return a list with 2 elements!
    ext = file_name.rsplit('.', 1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXENTIONS"]:
        return True
    else:
        return False


@app.route("/")
def index():
    return render_template("upload_image.html")


@app.route("/upload_image", methods=["GET", "POST"])
def UploadImage():
    if request.method == "POST":

        if request.files:

            imag = request.files['image']

            if imag.filename == "":
                print("image must have a file_name")
                return render_template("upload_image.html")

            if not allowed_image(imag.filename):
                msg = "The image extention is not allowed try to upload another image with allowed extention .jpg .jpeg .png"
                print(msg)
                return render_template("upload_image.html", not_allowed=msg)
            name_only = os.path.splitext(imag.filename)[0]
            path1 = os.path.join(app.config["IMAGES_UPLOADS"], name_only)
            try:
                os.mkdir(path1)
            except OSError as err:
                return render_template("view.html", already_generated=True, name_of_folder=name_only)
            img = cv.imdecode(numpy.fromstring(
                imag.read(), numpy.uint8), cv.IMREAD_UNCHANGED)
            cv.imwrite(os.path.join(path1, name_only+"_0"+str(0)+".png"), img)
            # image_encoded = cv.imencode('.jpg', img)
            # image_encoded = image_encoded[1]
            # up till here no change required
            # GenerateImagesDelayed(image_encoded, path1, name_only)
            median = cv.medianBlur(img, 5)
            PathToSaveImage = os.path.join(path1, name_only+"_0"+str(1)+".png")
            cv.imwrite(PathToSaveImage, median)
            return render_template("view.html", name_of_folder=name_only)

    return render_template("upload_image")


if __name__ == "__main__":
    app.run(debug=True)
