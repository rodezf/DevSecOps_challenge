import unittest
from password_generator import app  # Import the Flask application instance

class TestPasswordGenerator(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()  # Create a test client

    def test_password_generation(self):
        # Send a GET request to the /generate-password route
        response = self.client.get('/generate-password?length=20&lowercase=10&uppercase=10&digits=10')

        # Check that the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check that the response is a JSON object
        self.assertEqual(response.content_type, 'application/json')

        # Check that the password in the response is the correct length
        password = response.get_json()['password']
        self.assertEqual(len(password), 20)

        # Check that the password contains the correct number of each type of character
        self.assertEqual(sum(c.islower() for c in password), 10)
        self.assertEqual(sum(c.isupper() for c in password), 10)
        self.assertEqual(sum(c.isdigit() for c in password), 10)

if __name__ == '__main__':
    unittest.main()
