''' Function for calling the IBM AI for emotion detection'''
import requests
import json


def emotion_detector(text_to_analyze):
    '''This is the function script, uses the post method from the requests method'''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    text = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, headers = headers, json = text, timeout = 30)
    if response.status_code == 400:
        empty_response = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
        }
        return empty_response
    json_response = json.loads(response.text)
    format_response = json_response['emotionPredictions'][0]['emotion']
    final_response = {
    'anger': format_response['anger'],
    'disgust': format_response['disgust'],
    'fear': format_response['fear'],
    'joy': format_response['joy'],
    'sadness': format_response['sadness'],
    'dominant_emotion': max(format_response, key = format_response.get)
    }
    return final_response
