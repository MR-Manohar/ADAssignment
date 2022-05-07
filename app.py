from crypt import methods
from flask import Flask, jsonify, request
import logging

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    logging.basicConfig(format='%(asctime)s | %(message)s', level=logging.DEBUG)
    logging.debug(f'{request.url} | In home route.')

    header_type = request.headers.get('Accept')

    if header_type == 'application/json':
        return jsonify({"message": "Hello, World"})

    return "<p>Hello, World</p>"

if __name__ == '__main__':
    app.run()

