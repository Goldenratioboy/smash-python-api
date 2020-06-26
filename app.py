import UltimateFrameData
from flask import Flask

app = Flask(__name__)

@app.route('/<character>')
def get_character(character):
    result = {"characterMoves": UltimateFrameData.UltimateFrameData(character).get_character_data()}
    return result

if __name__ == "__main__":
    app.run('0.0.0.0', port='5000')