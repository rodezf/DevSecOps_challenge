from flask import Flask, request
from flask_restx import Api, Resource, fields
import random
import string


app = Flask(__name__)
api = Api(app, version='1.0', title='Password Generator API',
    description='A sophisticated password generator API',
)

ns = api.namespace('generate-password', description='Password generation operations')

password_model = api.model('PasswordParameters', {
    'length': fields.Integer(required=True, description='The total length of the password'),
    'lowercase': fields.Integer(required=True, description='The number of lowercase letters in the password'),
    'uppercase': fields.Integer(required=True, description='The number of uppercase letters in the password'),
    'digits': fields.Integer(required=True, description='The number of digits in the password'),
})

@ns.route('/')
class PasswordGenerator(Resource):
    @ns.expect(password_model)
    @ns.response(403, 'Invalid parameters')
    @ns.response(200, 'Success')
    def get(self):
        '''Generate a new password'''
        args = request.args
        length = int(args.get('length', 0))
        lowercase = int(args.get('lowercase', 0))
        uppercase = int(args.get('uppercase', 0))
        digits = int(args.get('digits', 0))

        if length < 20 or lowercase < 10 or uppercase < 10 or digits < 10:
            api.abort(403, "Invalid parameters")

        password_characters = string.ascii_lowercase * lowercase + string.ascii_uppercase * uppercase + string.digits * digits
        password = ''.join(random.choice(password_characters) for i in range(length))

        return {'password': password}







if __name__ == '__main__':

    app.run(debug=True)

