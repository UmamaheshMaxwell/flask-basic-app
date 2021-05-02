from flask import Flask, render_template

app = Flask(__name__, template_folder="views")

@app.route("/")
def home():
    return render_template("index.html", title="Uma's Website", users=["uma", "swathi", "jagrav"])

@app.route("/test")
def test():
    return render_template("test.html")

if(__name__ == "__main__"):
    app.run(debug=True)