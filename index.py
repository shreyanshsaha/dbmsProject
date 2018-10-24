from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def renderHome():
  return render_template("home.html")


if __name__ == "__main__":
  app.run(port=80, debug=True)