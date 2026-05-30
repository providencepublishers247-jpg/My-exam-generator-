from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    questions = ""

    if request.method == "POST":
        notes = request.form["notes"]

        questions = f"""
        Sample Questions Generated From:

        {notes[:100]}

        1. What is the main topic?
        A. Option A
        B. Option B
        C. Option C
        D. Option D

        2. Explain the topic briefly.
        """

    return render_template("index.html", questions=questions)

if __name__ == "__main__":
    app.run(debug=True)