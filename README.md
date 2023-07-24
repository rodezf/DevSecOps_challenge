Password Generator REST API
Overview
This REST API allows users to generate random passwords based on certain criteria. It provides a single endpoint, /generate-password, which accepts query parameters to customize the generated password.

Installation
Ensure you have Python installed on your system. If not, you can download it from here.
Install the required Python packages by running pip install -r requirements.txt in your terminal.
Running the API
To start the API, navigate to the directory containing the application file in your terminal and run python app.py. The API will start running at http://localhost:5000.

API Endpoints
/generate-password
Generates a random password.

Method: GET

Query Parameters:

length: The total length of the password.
lowercase: The number of lowercase letters the password should contain.
uppercase: The number of uppercase letters the password should contain.
digits: The number of digits the password should contain.
Response: A JSON object containing the generated password.

Example Usage:

scss
Copy code
GET /generate-password?length=20&lowercase=10&uppercase=5&digits=5
Save to grepper
Example Response:

json
Copy code
{
    "password": "aB1cD2eF3gH4iJ5kL6mN7oP8qR9sT0"
}
Save to grepper
Error Handling
The API will return an HTTP 403 error if any of the following conditions are met:

The total number of password characters specified by the parameters is less than 20.
The number of lowercase letters is less than 10.
The number of uppercase letters is less than 10.
The number of digits is less than 10.
Testing
Unit tests for the password generation function can be run by executing python test_password_generator.py in your terminal.

Contact
For any issues or suggestions, please contact [franrodez33@gmail.com].
CI/CD SAST Tooling 
