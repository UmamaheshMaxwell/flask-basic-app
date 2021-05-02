from flask import Flask, render_template

# template_folder will help us letting flask know the folder for html files
app = Flask(__name__, template_folder="views")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return render_template("index.html", content=name, value=9, users=["uma","swathi","jagrav"])

if __name__ == "__main__":
    app.run()