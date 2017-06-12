from flask import (
        Flask,
        url_for,
        request
)
import json
from flask_restplus import (
        Resource, 
        Api, 
        reqparse
)

app = Flask(__name__)



if __name__ == '__main__':
 app.run(debug=True)
