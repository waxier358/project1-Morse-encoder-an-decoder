import unittest
from morsecode import MorseCode


class TestMorseCode(unittest.TestCase):

    def setUp(self):
        self.morse = MorseCode()
        self.test_encode_dict = {'hello': 'Message hello is coded: .... . .-.. .-.. ---',
                                 'hello my friend!': 'Message hello my friend! is coded: .... . .-.. .-.. ---  -- -.--  ..-. .-. .. . -. -.. -.-.--',
                                 'latitude 45.27': 'Message latitude 45.27 is coded: .-.. .- - .. - ..- -.. .  ....- ..... .-.-.- ..--- --...',
                                 '': 'An error occurred: You enter an empty string or a string only with " ".',
                                 '+': "An error occurred: ValueError character + isn't in the alfabet!",
                                 '   ': "An error occurred: You enter an empty string or a string only with " ".",
                                 'he##llo': "An error occurred: ValueError character # isn't in the alfabet!"}
        self.test_decode_dict = {'.... . .-.. .-.. ---': 'Message .... . .-.. .-.. --- is decoded: HELLO',
            '.... . .-.. .-.. ---  -- -.--  ..-. .-. .. . -. -.. -.-.--': 'Message .... . .-.. .-.. ---  -- -.--  ..-. .-. .. . -. -.. -.-.-- is decoded: HELLO MY FRIEND!',
            '.-.. .- - .. - ..- -.. .  ....- ..... .-.-.- ..--- --...': 'Message .-.. .- - .. - ..- -.. .  ....- ..... .-.-.- ..--- --... is decoded: LATITUDE 45.27',
            '': 'An error occurred: You enter an empty string or a string only with " ".',
            '+': "An error occurred: ValueError character + isn't in the alfabet!",
            '   ': "An error occurred: You enter an empty string or a string only with " ".",
            '.... . .-.. .&.. ---': "An error occurred: ValueError character .&.. isn't in Morse Code!"
        }

    def test_encode(self):
        for test_word, expected_result in self.test_encode_dict.items():
            self.morse.set_message_to_code(test_word)
            if "An error occurred" in expected_result:  # Expected an exception
                with self.assertRaises(ValueError):
                    self.morse.code_message()
            else:
                self.assertEqual(self.morse.code_message(), expected_result)

    def test_decode(self):
        for test_word, expected_result in self.test_decode_dict.items():
            self.morse.set_message_to_decode(test_word)
            if "An error occurred" in expected_result:  # Expected an exception
                with self.assertRaises(ValueError):
                    self.morse.decode_message()
            else:
                self.assertEqual(self.morse.decode_message(), expected_result)


if __name__ == "__main__":
    unittest.main()
