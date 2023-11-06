import unittest
from io import StringIO
import sys
from xor_crack import xor_and_base64

class TestXORCrack(unittest.TestCase):
    def test_xor_and_base64(self):
        plaintext = "Hello"
        cipher = "World"

        expected_key = ''.join(chr(ord(i) ^ ord(j)) for i, j in zip(plaintext, cipher))
        expected_base64 = cipher.encode().hex()

        with StringIO() as captured_output, unittest.mock.patch('sys.stdout', captured_output):
            xor_and_base64(plaintext, cipher)
            actual_output = captured_output.getvalue()

        self.assertIn(f"Key: {expected_key}\nCipher Base64 encoded: {expected_base64}", actual_output)

if __name__ == '__main__':
    unittest.main()
