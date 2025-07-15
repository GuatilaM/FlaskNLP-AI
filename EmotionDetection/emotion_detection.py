import json
import requests

def emotion_detection(text_to_analyse):
    """Calls Watson Emotion AI to get emotion scores of a text, identifying the dominant emotion"""

    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, headers=headers, json=payload)
    
    # extract emotions and scores
    res_data = json.loads(response.text)
    emotions_dict = res_data['emotionPredictions'][0]['emotion']
    # sort emotion scores from highest to lowest
    emotion_scores = list(emotions_dict.values())
    emotion_scores.sort(reverse=True)
    # get dominant emotion
    dominant_emotion = ''
    for emotion, score in emotions_dict.items():
        if score == emotion_scores[0]:
            dominant_emotion = emotion

    emotions_dict['dominant_emotion'] = dominant_emotion
    return emotions_dict
