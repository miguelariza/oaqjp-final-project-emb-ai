from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        test_01 = emotion_detector("I am glad this happened")
        self.assertEqual(test_01['dominant_emotion'], 'joy')
        test_02 = emotion_detector("I am really mad about this")
        self.assertEqual(test_02['dominant_emotion'], 'anger')
        test_03 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(test_03['dominant_emotion'], 'disgust')
        test_04 = emotion_detector("I am so sad about this")
        self.assertEqual(test_04['dominant_emotion'], 'sadness')
        test_05 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(test_05['dominant_emotion'], 'fear')

unittest.main()