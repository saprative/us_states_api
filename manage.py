from flask import Flask
from states import states

app = Flask(__name__)

app.register_blueprint(states)


if __name__ == '__main__':
 app.run(debug=True)
