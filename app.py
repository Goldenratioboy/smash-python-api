import UltimateFrameData as UFD
from flask import Flask

app = Flask(__name__)

@app.route('/<character>')
def get_character(character):
    result = {"characterMoves": UFD.UltimateFrameData(character).get_character_data()}
    return result

@app.route('/favicon.ico')
def get_favicon():
    return 'Hello there'


if __name__ == "__main__":
    app.run('0.0.0.0', port='5000')