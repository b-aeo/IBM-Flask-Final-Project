'''Server application code for emotion detector app'''
## import flask and required modules
from flask import Flask, request, render_template
## import created emotion detection module from created package
from EmotionDetection.emotion_detection import emotion_detector
##initiate flask app
app = Flask('Emotion Detection Application')
## define an app route
@app.route("/emotionDetector")
def send_text():
    '''Function to execute the emotion detector method on the inputted text'''
    ## store get request for retrieving text for analysis from app interface
    text_sent = request.args.get('textToAnalyze')
    ## input retrieved text into the emotion detector function
    analyse_text = emotion_detector(text_sent)
    ## error handling for event that no text is entered on interface
    if analyse_text['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    ## output the function info
    return f"For the given statement, the system response is anger\
    : {analyse_text['anger']}, 'disgust': {analyse_text['disgust']},\
     'fear': {analyse_text['fear']}, 'joy': {analyse_text['joy']} and \
     'sadness': {analyse_text['sadness']}. The dominant emotion is\
      {analyse_text['dominant_emotion']}"
@app.route("/")
def render_index():
    '''Function to render the html template'''
    return render_template('index.html')
## ensure script is not run as a module
if __name__ == "__main__":
    ## run application in debug mode
    app.run(debug = True, host = "0.0.0.0", port = 5000)
