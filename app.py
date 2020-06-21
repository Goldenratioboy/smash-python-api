import UltimateFrameData
from flask import Flask

app = Flask(__name__)

@app.route('/<character>')
def get_character(character):
    return UltimateFrameData.UltimateFrameData(character).get_character_data()

# @app.route('/banjo_and_kazooie')
# def get_banjo_and_kazooie():
#     return UltimateFrameData.UltimateFrameData('Banjo & Kazooie').get_character_data()

# @app.route('/bayonetta')
# def get_bayonetta():
#     return UltimateFrameData.UltimateFrameData('Bayonetta').get_character_data()

# @app.route('/bowser')
# def get_bowser():
#     return UltimateFrameData.UltimateFrameData('Bowser').get_character_data()

# @app.route('/bowser_jr')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Bowser Jr').get_character_data()

# @app.route('/byleth')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Byleth').get_character_data()

# @app.route('/captain_falcon')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Captain Falcon').get_character_data()

# @app.route('/chrom')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Chrom').get_character_data()

# @app.route('/cloud')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Cloud').get_character_data()

# @app.route('/corrin')
# def get_ken():
#     return UltimateFrameData.UltimateFrameData('Corrin').get_character_data()

# @app.route('/daisy')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Daisy').get_character_data()

# @app.route('/dark_pit')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Dark Pit').get_character_data()

# @app.route('/dark_samus')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Dark Samus').get_character_data()

# @app.route('/diddy_kong')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Diddy Kong').get_character_data()

# @app.route('/donkey_kong')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Donkey Kong').get_character_data()

# @app.route('/dr_mario')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Dr.Mario').get_character_data()

# @app.route('/duck_hunt')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Duck Hunt').get_character_data()

# @app.route('/falco')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Falco').get_character_data()

# @app.route('/fox')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Fox').get_character_data()

# @app.route('/ganondorf')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Ganondorf').get_character_data()

# @app.route('/greninja')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Greninja').get_character_data()

# @app.route('/Hero')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Hero').get_character_data()

# @app.route('/ice_climbers')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Ice Climbers').get_character_data()

# @app.route('/ike')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Ike').get_character_data()

# @app.route('/incineroar')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Incineroar').get_character_data()

# @app.route('/inkling')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Inkling').get_character_data()

# @app.route('/isabelle')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('isabelle').get_character_data()

# @app.route('/jigglypuff')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Jigglypuff').get_character_data()

#     @app.route('/joker')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Joker').get_character_data()

#     @app.route('/ken')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Ken').get_character_data()

# @app.route('/king_dedede')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('King Dedede').get_character_data()

# @app.route('/king_k_rool')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('King K. Rool').get_character_data()

# @app.route('/kirby')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Kirby').get_character_data()

# @app.route('/link')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Link').get_character_data()

# @app.route('/little_mac')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Little mac').get_character_data()

# @app.route('/lucario')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Lucario').get_character_data()

#     @app.route('/lucas')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Lucas').get_character_data()

# @app.route('/lucina')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Lucina').get_character_data()

# @app.route('/luigi')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('luigi').get_character_data()

#     @app.route('/mario')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Mario').get_character_data()

# @app.route('/marth')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Marth').get_character_data()

# @app.route('/mega_man')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Mega Man').get_character_data()

# @app.route('/meta_knight')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Meta Knight').get_character_data()

# @app.route('/mewtwo')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Mewtwo').get_character_data()

# @app.route('/mii_brawler')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Mii Brawler').get_character_data()

# @app.route('/mii_gunner')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Mii Gunner').get_character_data()

# @app.route('/mii_swordfighter')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Mii Swordfighter').get_character_data()

# @app.route('/mr_game_and_watch')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Mr.Game & Watch').get_character_data()

# @app.route('/ness')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Ness').get_character_data()

# @app.route('/olimar')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Olimar').get_character_data()

# @app.route('/pac_man')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Pac Man').get_character_data()

# @app.route('/palutena')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Palutena').get_character_data()

# @app.route('/peach')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Peach').get_character_data()

# @app.route('/pichu')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Pichu').get_character_data()

# @app.route('/pikachu')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Pikachu').get_character_data()

# @app.route('/piranha_plant')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Piranha Plant').get_character_data()

# @app.route('/pit')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Pit').get_character_data()

# @app.route('/squirtle')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Squirtle').get_character_data()

# @app.route('/ivysaur')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Ivysaur').get_character_data()

# @app.route('/charizrd')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Charizard').get_character_data()

# @app.route('/richter')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Richter').get_character_data()

# @app.route('/ridley')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Ridley').get_character_data()

# @app.route('/rob')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('R.O.B').get_character_data()

# @app.route('/robin')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Robin').get_character_data()

# @app.route('/rosalina_and_luma')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Rosalina_and_Luma').get_character_data()

# @app.route('/roy')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Roy').get_character_data()

# @app.route('/ryu')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Ryu').get_character_data()

# @app.route('/samus')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Samus').get_character_data()

# @app.route('/sheik')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Sheik').get_character_data()

# @app.route('/shulk')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Shulk').get_character_data()

# @app.route('/simon')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Simon').get_character_data()

# @app.route('/snake')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Snake').get_character_data()

# @app.route('/terry')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Terry').get_character_data()

# @app.route('/toon_link')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Toon_Link').get_character_data()

# @app.route('/villager')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Villager').get_character_data()

# @app.route('/wario')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Wario').get_character_data()

# @app.route('/wii_fit_trainer')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Wii_Fit_Trainer').get_character_data()

# @app.route('/wolf')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Wolf').get_character_data()

# @app.route('/yoshi')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Yoshi').get_character_data()

# @app.route('/young_link')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Young_Link').get_character_data()

# @app.route('/zelda')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Zelda').get_character_data()

# @app.route('/zero_suit_samus')
# def get_character_data():
#     return UltimateFrameData.UltimateFrameData('Zero_Suit_Samus').get_character_data()


if __name__ == "__main__":
    app.run('0.0.0.0', port='5000')