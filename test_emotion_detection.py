from emotion_detection import emotion_detector
import unittest

class EmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        # Test 1
        result_1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        # Test 2
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'], 'anger')
        # Test 3
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'], 'disgust')
        # Test 4
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'], 'sadness')
        # Test 5
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'], 'fear')

if __name__ =="__main__":
    unittest.main()