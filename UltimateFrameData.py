import requests
import re
from bs4 import BeautifulSoup
from bs4.element import Tag

class UltimateFrameData():
    
    def __init__(self, character):
        self.request = 'https://ultimateframedata.com/' + character + '.php'

    def get_character_data(self):
        response = requests.get(self.request)
        soup = BeautifulSoup(response.content, 'html.parser')
        character_data = {}
        ground_move_array = []
        if soup.find(id='groundattacks') is None:
            print('kazuya')
        else:
            ground_attacks = soup.find(id='groundattacks').find_next('div')
            for elem in ground_attacks:
                if type(elem) == Tag:
                    my_image = None
                    if elem.find('a') is not None:
                        my_image = elem.find('a')['data-featherlight']
                    if elem.find('div', class_='activeframes') is None:
                        # Luigi down taunt is dumb
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "image": my_image
                        })
                    else:
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                            "onShield": elem.find('div', class_='advantage').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                            "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                            "image": my_image
                        })
        # kazuya
        if soup.find(id='jabattacks') is None:
            print('kazuya')
        else:
            jab_attacks = soup.find(id='jabattacks').find_next('div')
            for elem in jab_attacks:
                if type(elem) == Tag:
                    my_image = None
                    if elem.find('a') is not None:
                        my_image = elem.find('a')['data-featherlight']
                    if elem.find('div', class_='activeframes') is None:
                        # Luigi down taunt is dumb
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "image": my_image
                        })
                    else:
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                            "onShield": elem.find('div', class_='advantage').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                            "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                            "image": my_image
                        })

        if soup.find(id='tiltattacks') is None:
            print('kazuya')
        else:       
            tilt_attacks = soup.find(id='tiltattacks').find_next('div')
            for elem in tilt_attacks:
                if type(elem) == Tag:
                    my_image = None
                    if elem.find('a') is not None:
                        my_image = elem.find('a')['data-featherlight']
                    if elem.find('div', class_='activeframes') is None:
                        # Luigi down taunt is dumb
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "image": my_image
                        })
                    else:
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                            "onShield": elem.find('div', class_='advantage').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                            "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                            "image": my_image
                        })
        if soup.find(id='crouchingattacks') is None:
            print('kazuya')
        else:                       
            crouching_attacks = soup.find(id='crouchingattacks').find_next('div')
            for elem in crouching_attacks:
                if type(elem) == Tag:
                    my_image = None
                    if elem.find('a') is not None:
                        my_image = elem.find('a')['data-featherlight']
                    if elem.find('div', class_='activeframes') is None:
                        # Luigi down taunt is dumb
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "image": my_image
                        })
                    else:
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                            "onShield": elem.find('div', class_='advantage').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                            "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                            "image": my_image
                        })
        if soup.find(id='dashattacks') is None:
            print('kazuya')
        else:
            dash_attacks = soup.find(id='dashattacks').find_next('div')
            for elem in dash_attacks:
                if type(elem) == Tag:
                    my_image = None
                    if elem.find('a') is not None:
                        my_image = elem.find('a')['data-featherlight']
                    if elem.find('div', class_='activeframes') is None:
                        # Luigi down taunt is dumb
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "image": my_image
                        })
                    else:
                        ground_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                            "onShield": elem.find('div', class_='advantage').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                            "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                            "image": my_image
                        })
        character_data['groundMoves'] = ground_move_array

        aerial_attacks = soup.find(id='aerialattacks').find_next('div')
        aerial_move_array = []
        for elem in aerial_attacks:
            if type(elem) == Tag:
                my_image = None
                if elem.find('a') is not None:
                    my_image = elem.find('a')['data-featherlight']
                aerial_move_array.append({
                    "name": elem.find('div', class_='movename').get_text().strip(),
                    "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                    "onShield": elem.find('div', class_='advantage').get_text().strip(),
                    "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                    "landingLag": elem.find('div', class_='landinglag').get_text().strip(),
                    "notes": elem.find('div', class_='notes').get_text().strip(),
                    "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                    "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                    "image": my_image
                })
        character_data['aerialMoves'] = aerial_move_array

        special_attacks = soup.find(id='specialattacks').find_next('div')
        special_move_array = []
        for elem in special_attacks:       
            if type(elem) == Tag:
                my_image = None
                if elem.find('a') is not None:
                    try:
                        my_image = elem.find('a')['data-featherlight']
                    except:
                        print(elem.find('a'))
                if elem.find('div', class_='activeframes') is None:
                    # rosalina is dumb and isabelle is dumb
                    special_move_array.append({
                        "name": elem.find('div', class_='movename').get_text().strip(),
                        "onShield": elem.find('div', class_='advantage').get_text().strip(),
                        "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                        "landingLag": elem.find('div', class_='landinglag').get_text().strip(),
                        "notes": elem.find('div', class_='notes').get_text().strip(),
                        "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                        "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                        "image": my_image
                    })
                else:
                    special_move_array.append({
                        "name": elem.find('div', class_='movename').get_text().strip(),
                        "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                        "onShield": elem.find('div', class_='advantage').get_text().strip(),
                        "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                        "landingLag": elem.find('div', class_='landinglag').get_text().strip(),
                        "notes": elem.find('div', class_='notes').get_text().strip(),
                        "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                        "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                        "image": my_image
                    })
        if soup.find(id='inputattacks') is None:
            print('kazuya')
        else:
            input_attacks = soup.find(id='inputattacks').find_next('div')
            for elem in input_attacks:       
                if type(elem) == Tag:
                    my_image = None
                    if elem.find('a') is not None:
                        try:
                            my_image = elem.find('a')['data-featherlight']
                        except:
                            print(elem.find('a'))
                    if elem.find('div', class_='activeframes') is None:
                        # rosalina is dumb and isabelle is dumb
                        special_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "onShield": elem.find('div', class_='advantage').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "landingLag": elem.find('div', class_='landinglag').get_text().strip(),
                            "notes": elem.find('div', class_='notes').get_text().strip(),
                            "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                            "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                            "image": my_image
                        })
                    else:
                        special_move_array.append({
                            "name": elem.find('div', class_='movename').get_text().strip(),
                            "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                            "onShield": elem.find('div', class_='advantage').get_text().strip(),
                            "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                            "landingLag": elem.find('div', class_='landinglag').get_text().strip(),
                            "notes": elem.find('div', class_='notes').get_text().strip(),
                            "shieldLag": elem.find('div', class_='shieldlag').get_text().strip(),
                            "shieldStun": elem.find('div', class_='shieldstun').get_text().strip(),
                            "image": my_image
                        })                   
        character_data['specialMoves'] = special_move_array

        grabs_throws = soup.find(id='grabs').find_next('div')
        grab_throws_array = []
        for elem in grabs_throws:
            if type(elem) == Tag:
                my_image = None
                if elem.find('a') is not None:
                    my_image = elem.find('a')['data-featherlight']
                # might need to revisit to get active frames instead of startup frames
                grab_throws_array.append({ 
                    "name": elem.find('div', class_='movename').get_text().strip(),
                    "startup": elem.find('div', class_='startup').get_text().strip(),
                    "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                    "notes": elem.find('div', class_='notes').get_text().strip(),
                    "image": my_image
                })
        character_data['grabs'] = grab_throws_array

        dodges = soup.find(id='dodges').find_next('div')
        dodges_array = []
        for elem in dodges:
            if type(elem) == Tag:
                my_image = None
                if elem.find('a') is not None:
                    my_image = elem.find('a')['data-featherlight']
                dodges_array.append({
                    "name": elem.find('div', class_='movename').get_text().strip(),
                    "totalFrames": elem.find('div', class_='totalframes').get_text().strip(),
                    "landingLag": elem.find('div', class_='landinglag').get_text().strip(),
                    "notes": elem.find('div', class_='notes').get_text().strip(),
                    "image": my_image
                })
        character_data['dodges'] = dodges_array

        return character_data