import requests
from bs4 import BeautifulSoup
from bs4.element import Tag

class UltimateFrameData():

    def __init__(self, character):
        self.request = 'https://ultimateframedata.com/' + character + '.php'

    def get_character_data(self):
        response = requests.get(self.request)
        soup = BeautifulSoup(response.content, 'html.parser')
        character_data = {}

        ground_attacks = soup.find(id='groundattacks').find_next('div')
        for elem in ground_attacks:
            if type(elem) == Tag:
                my_image = None
                if elem.find('a') is not None:
                    my_image = elem.find('a')['data-featherlight']
                character_data[elem.find('div', class_='movename').get_text().strip()] = {
                    "active_frames": elem.find('div', class_='activeframes').get_text().strip(),
                    "on_shield": elem.find('div', class_='advantage').get_text().strip(),
                    "total_frames": elem.find('div', class_='totalframes').get_text().strip(),
                    "sheild_lag": elem.find('div', class_='shieldlag').get_text().strip(),
                    "shield_stun": elem.find('div', class_='shieldstun').get_text().strip(),
                    "image": my_image
                }

        aerial_attacks = soup.find(id='aerialattacks').find_next('div')
        for elem in aerial_attacks:
            if type(elem) == Tag:
                my_image = None
                if elem.find('a') is not None:
                    my_image = elem.find('a')['data-featherlight']
                character_data[elem.find('div', class_='movename').get_text().strip()] = {
                    "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                    "on_shield": elem.find('div', class_='advantage').get_text().strip(),
                    "total_frames": elem.find('div', class_='totalframes').get_text().strip(),
                    "landing_lag": elem.find('div', class_='landinglag').get_text().strip(),
                    "notes": elem.find('div', class_='notes').get_text().strip(),
                    "sheild_lag": elem.find('div', class_='shieldlag').get_text().strip(),
                    "shield_stun": elem.find('div', class_='shieldstun').get_text().strip(),
                    "image": my_image
                }

        special_attacks = soup.find(id='specialattacks').find_next('div')
        for elem in special_attacks:
            if type(elem) == Tag:
                my_image = None
                if elem.find('a') is not None:
                    my_image = elem.find('a')['data-featherlight']
                character_data[elem.find('div', class_='movename').get_text().strip()] = {
                    "activeFrames": elem.find('div', class_='activeframes').get_text().strip(),
                    "on_shield": elem.find('div', class_='advantage').get_text().strip(),
                    "total_frames": elem.find('div', class_='totalframes').get_text().strip(),
                    "landing_lag": elem.find('div', class_='landinglag').get_text().strip(),
                    "notes": elem.find('div', class_='notes').get_text().strip(),
                    "sheild_lag": elem.find('div', class_='shieldlag').get_text().strip(),
                    "shield_stun": elem.find('div', class_='shieldstun').get_text().strip(),
                    "image": my_image
                }

        grabs_throws = soup.find(id='grabs').find_next('div')
        for elem in grabs_throws:
            if type(elem) == Tag:
                my_image = None
                if elem.find('a') is not None:
                    my_image = elem.find('a')['data-featherlight']
                # might need to revisit to get active frames instead of startup frames 
                character_data[elem.find('div', class_='movename').get_text().strip()] = {
                    "startup": elem.find('div', class_='startup').get_text().strip(),
                    "total_frames": elem.find('div', class_='totalframes').get_text().strip(),
                    "notes": elem.find('div', class_='notes').get_text().strip(),
                    "image": my_image
                }

        dodges = soup.find(id='dodges').find_next('div')
        for elem in dodges:
            if type(elem) == Tag:
                my_image = None
                if elem.find('a') is not None:
                    my_image = elem.find('a')['data-featherlight']
                    character_data[elem.find('div', class_='movename').get_text().strip()] = {
                    "total_frames": elem.find('div', class_='totalframes').get_text().strip(),
                    "landing_lag": elem.find('div', class_='landinglag').get_text().strip(),
                    "notes": elem.find('div', class_='notes').get_text().strip(),
                    "image": my_image
                }

        return character_data
