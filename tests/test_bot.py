import unittest
import unittest.mock
from src.main import BackRunBot

class TestBackRunBot(unittest.TestCase):
    def test_bot_initialization(self):
        bot = BackRunBot("wss://dummy", "0x" + "a" * 64)
        self.assertIsNotNone(bot)
        
if __name__ == '__main__':
    unittest.main()
