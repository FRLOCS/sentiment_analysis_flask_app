from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)
classifier = pipeline('sentiment-analysis')

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    sentiment = None
    face = None

    if request.method == "POST":
        text = request.form.get("text")
        if text:
            try:
                result = classifier(text)[0]  # Get the first (and usually only) result.
                sentiment = result['label']

                if sentiment == "POSITIVE":
                    face = ":)"
                elif sentiment == "NEGATIVE":
                    face = ":("
                else:  # Handle neutral or unexpected labels
                    face = "😐" # Neutral face

            except Exception as e:
                result = f"Error: {e}"  # Display error if something goes wrong.
                face = "🤔" # Confused face
                sentiment = "Error"


    return render_template("index.html", result=result, face=face, sentiment=sentiment)

if __name__ == "__main__":
    app.run(debug=True)  # debug=True is helpful during development