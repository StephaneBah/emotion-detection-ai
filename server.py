"""
Flask application for emotion detection.
"""

from flask import Flask, render_template, request
from emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detector")

@app.route("/")
def render_index_page():
    """
    Render the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def rend_emotion():
    """
    Analyze the provided text and return detected emotions.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    if not text_to_analyze:
        return "No text provided! Please provide text to analyze.", 400

    response = emotion_detector(text_to_analyze)
    if not response:
        return "Error processing the text. Please try again.", 500

    if not response.get('dominant_emotion'):
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is: "
        f"'anger': {response.get('anger', 'N/A')}, "
        f"'disgust': {response.get('disgust', 'N/A')}, "
        f"'fear': {response.get('fear', 'N/A')}, "
        f"'joy': {response.get('joy', 'N/A')}, "
        f"and 'sadness': {response.get('sadness', 'N/A')}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
