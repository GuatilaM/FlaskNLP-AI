import unittest
from EmotionDetection.emotion_detection import emotion_detection

class TestEmotionDetection(unittest.TestCase):
    """Tests for emotion detection module"""

    def test_emotion_detection(self):
        test_cases = [
            {
                'statement': 'I am glad this happened',
                'dominant_emotion': 'joy'
            },
            {
                'statement': 'I am really mad about this',
                'dominant_emotion': 'anger'
            },
            {
                'statement': 'I feel disgusted just hearing about this',
                'dominant_emotion': 'disgust'
            },
            {
                'statement': 'I am so sad about this',
                'dominant_emotion': 'sadness'
            },
            {
                'statement': 'I am really afraid that this will happen',
                'dominant_emotion': 'fear'
            },
        ]
        for case in test_cases:
            output = emotion_detection(case['statement'])
            self.assertEqual(output['dominant_emotion'], case['dominant_emotion'])

unittest.main()
