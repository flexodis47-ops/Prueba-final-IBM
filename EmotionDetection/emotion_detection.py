"""
Módulo encargado de interactuar con la API de Watson NLP
para realizar la detección de emociones en textos.
"""
import json
import requests

def emotion_detector(text_to_analyze):
    """
    Analiza el texto introducido utilizando la API Watson NLP y devuelve
    las puntuaciones de las emociones junto con la emoción dominante.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Requisito de la Task 7: Manejo de cadenas vacías o espacios en blanco
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    response = requests.post(url, json=myobj, headers=headers, timeout=10)

    # Requisito de la Task 7: Manejo de código de estado de error 400
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None,
            'joy': None, 'sadness': None, 'dominant_emotion': None
        }

    # Procesamiento nativo del JSON de IBM Watson
    formatted_response = json.loads(response.text)
    
    # Extraemos el diccionario de emociones directo del índice 0 de la lista
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # Determinación de la emoción dominante
    emotion_dict = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_dict, key=emotion_dict.get)

    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
