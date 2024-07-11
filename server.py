'''Server application code for emotion detector app'''

from flask import Flask, request, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detection Application')

@app.route("/emotionDetector")
def send_text():
    text_sent = request.args.get('textToAnalyze')
    analyse_text = emotion_detector(text_sent)
    return f"For the given statement, the system response is anger\
    : {analyse_text['anger']}, 'disgust': {analyse_text['disgust']},\
     'fear': {analyse_text['fear']}, 'joy': {analyse_text['joy']} and \
     'sadness': {analyse_text['sadness']}. The dominant emotion is\
      {analyse_text['dominant_emotion']}"

@app.route("/")
def render_index():
    return render_template('index.html')

if __name__ == "__main__":

    app.run(debug = True, host = "0.0.0.0", port = 5000)
