''' Testing script for regression testing'''
## import emotion detection and testing packages/modules
from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        '''Test cases checking the emotions are test correctly'''
        test_case_1 = emotion_detector('I am glad this happened')
        self.assertEqual(test_case_1['dominant_emotion'], 'joy')
        test_case_2 = emotion_detector('I am really mad about this')
        self.assertEqual(test_case_2['dominant_emotion'], 'anger')
        test_case_3 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(test_case_3['dominant_emotion'], 'disgust')
        test_case_4 = emotion_detector('I am so sad about this')
        self.assertEqual(test_case_4['dominant_emotion'], 'sadness')
        test_case_5 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(test_case_5['dominant_emotion'], 'fear')
## execute testing
unittest.main()
