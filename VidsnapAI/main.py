from flask import Flask, render_template, request
import uuid
from werkzeug.utils import secure_filename
import os


UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = {'txt', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create",methods=["GET", "POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print (request.files.keys())
        rec_id = (request.form.get("uuid"))
        desc = (request.form.get("text"))
        input_files = []
        for key, value in request.files.items():
            print (key, value)

            #Upload the files
            file = request.files[key]
            if file:
                filename = secure_filename(file.filename)
                os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'], rec_id), exist_ok=True)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, filename))
                input_files.append(file.filename)
        with open(
            os.path.join(app.config['UPLOAD_FOLDER'],rec_id, "desc.txt"),
                "w",
                   encoding="utf-8"
                     ) as f:
         f.write(desc) 
        for fl in input_files:
            with open(os.path.join(app.config['UPLOAD_FOLDER'],rec_id, "input.txt"),"a") as f:
                f.write(f"file '{fl}'\n")
                f.write("duration 1\n")


                   
    return render_template("create.html", myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels=reels)

app.run(debug=True)