import unittest
from app import extract_secrets

class TestApp(unittest.TestCase):
    def test_extract_secrets(self):
        text = "This is a test {*secret1*} and another {*secret2*}."
        expected_secrets = ["secret1", "secret2"]
        self.assertEqual(extract_secrets(text), expected_secrets)

if __name__ == "__main__":
    unittest.main()
