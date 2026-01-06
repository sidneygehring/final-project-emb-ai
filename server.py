"""
Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from emotion_detection import emotion_detector  # pylint: disable=import-error

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze emotions in the provided text input.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    anger_score = response["anger"]
    disgust_score = response["disgust"]
    fear_score = response["fear"]
    joy_score = response["joy"]
    sadness_score = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {anger_score}, "
        f"'disgust': {disgust_score}, "
        f"'fear': {fear_score}, "
        f"'joy': {joy_score} and "
        f"'sadness': {sadness_score}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """
    Render the index HTML page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
