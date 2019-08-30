#!/usr/bin/env python3


"""

单元测试

"""

import unittest
import io
import sys

from chatbot import chatbot


class TestChatbot(unittest.TestCase):
    def setUp(self):
        self.chatbot = chatbot.Chatbot()

    def test_training_simple(self):
        self.chatbot.main([
            '--maxLength', '3', 
            '--numEpoch', '1', 
            '--modelTag', 'unit-test'
        ])
    # 测试多伦对话
    def test_training_watson(self):
        pass


    # 测试所有
    def test_testing_all(self):
        pass

    # 测试实时对话功能
    def test_testing_interactive(self):
        progInput = io.StringIO()
        progInput.write('Hi!\n')
        progInput.write('How are you ?\n')
        progInput.write('aersdsd azej qsdfs\n')  # Unknown words
        progInput.write('é"[)=è^$*::!\n')  # Encoding
        progInput.write('ae e qsd, qsd 45 zeo h qfo k zedo. h et qsd qsfjze sfnj zjksdf zehkqf jkzae?\n')  # Too long sentences
        progInput.write('exit\n')

        #sys.stdin = progInput

        #self.chatbot.main(['--test', 'interactive', '--modelTag', 'unit-test'])

    def test_testing_daemon(self):
        pass

if __name__ == '__main__':
    unittest.main()
