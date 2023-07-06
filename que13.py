
import re
from flask import Flask
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)
app.secret_key = 'Kirti@1807'

# MongoDB configuration
cluster0 = MongoClient('mongodb+srv://kirti:kirti@cluster0.xxyu7.mongodb.net/set-1?retryWrites=true&w=majority')
db = cluster0['set-1']
customers_collection = db['Customers']

customer_data = [
    {
        'id': 1,
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'address': '123 Main Street',
        'phone_number': '555-1234'
    },
    {
        'id': 2,
        'name': 'kirti',
        'email': 'kirti@example.com',
        'address': '123 Main Street',
        'phone_number': '555-1234'
    },
    {
        'id': 3,
        'name': 'John Doe3',
        'email': 'johndoe@example.com',
        'address': '123 Main Street',
        'phone_number': '555-1234'
    },
    {
        'id': 4,
        'name': 'kirti2',
        'email': 'kirti@example.com',
        'address': '123 Main Street',
        'phone_number': '555-1234'
    },
    {
        'id': 5,
        'name': 'kittu',
        'email': 'kittu@example.com',
        'address': '123 Main Street',
        'phone_number': '555-1234'
    }
]



regex_pattern = re.compile('^B', re.IGNORECASE)
result = customers_collection.find({'id': {'$gt': 2}, 'name': regex_pattern})

for document in result:
    print(document)





if __name__ == '__main__':
    app.run(port=5000, debug=True)

