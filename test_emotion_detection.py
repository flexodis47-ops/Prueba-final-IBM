"""
Módulo de pruebas unitarias para validar las salidas del detector de emociones.
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Clase de pruebas unitarias para la función emotion_detector."""

    def test_emotion_detector(self):
        """Prueba enunciados individuales y verifica su emoción dominante."""
        # Caso 1: Alegría
        res_1 = emotion_detector("I am glad this happened")
        self.assertEqual(res_1['dominant_emotion'], 'joy')

        # Caso 2: Ira
        res_2 = emotion_detector("I am really mad about this")
        self.assertEqual(res_2['dominant_emotion'], 'anger')

        # Caso 3: Disgusto
        res_3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(res_3['dominant_emotion'], 'disgust')

        # Caso 4: Tristeza
        res_4 = emotion_detector("I am so sad about this")
        self.assertEqual(res_4['dominant_emotion'], 'sadness')

        # Caso 5: Miedo
        res_5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(res_5['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
