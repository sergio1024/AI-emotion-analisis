import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } } 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header,timeout=10)
    formatted_response = json.loads(response.text)
    
    emotions = { 
                'anger': 0,
                'disgust': 0,
                'fear': 0,
                'joy': 0,
                'sadness': 0,
                'dominant_emotion': -1
    }
    emotions['anger'] = formatted_response['emotionPredictions'][0]['emotion']['anger']
    emotions['disgust'] = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    emotions['fear'] = formatted_response['emotionPredictions'][0]['emotion']['fear']
    emotions['joy'] = formatted_response['emotionPredictions'][0]['emotion']['joy']
    emotions['sadness'] = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions
