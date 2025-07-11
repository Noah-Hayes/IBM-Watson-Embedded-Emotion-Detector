'''
This module defines a Flask-based web app that detects the
primary emotion in user-provided text. Contained is an endpoint for 
the emotion_detector function and index.html.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_det():
    '''Calls the emotion_detector function'''

    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        response_text = "Invalid text! Please try again!"
    else:
        response_text = f"For the given statement, the system response is 'anger': \
                        {response['anger']}, 'disgust': {response['disgust']}, \
                        'fear': {response['fear']}, 'joy': {response['joy']}, and \
                        'sadness': {response['sadness']}. \
                        The dominant emotion is {response['dominant_emotion']}."
    return response_text

@app.route("/")
def render_index_page():
    '''Renders the HTML'''

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
