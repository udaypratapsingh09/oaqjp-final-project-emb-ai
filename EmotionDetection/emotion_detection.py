import requests

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    response = response.json()
    emotions = response["emotionPredictions"][0]["emotion"]
    dominant_emotion = None
    max_score = 0
    for emotion, score in emotions.items():
        if score > max_score:
            max_score = score
            dominant_emotion = emotion

    emotions["dominant_emotion"] = dominant_emotion

    return emotions