"""Simple flask app to detect emotion based on text
Powered By IBM Watson AI API
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def detect():
    """Endpoint to detect emotion. Uses emotion_detector utility function
Sample output
For the given statement, the system response is
'anger': 0.006274985, 'disgust': 0.0025598293,
'fear': 0.009251528, 'joy': 0.9680386 and 
'sadness': 0.049744144.
The dominant emotion is joy.
"""
    print(request.args)
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    resp = "For the given statement the system response is\n"
    emotions = list(result.keys())[:-1]

    for emotion in emotions[:-2]:
        resp += f"\'{emotion}\': {result[emotion]}, "

    resp += f"\'{emotions[-2]}\': {result[emotions[-2]]} and"
    resp += f"\'{emotions[-1]}\': {result[emotions[-1]]}."

    dominant_emotion = result["dominant_emotion"]
    resp += f"\nThe dominant emotion is {dominant_emotion}"
    return resp

@app.route("/")
def index():
    """Handle default route
Serves static file (index.html)"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
