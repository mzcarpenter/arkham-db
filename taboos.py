from arkham_db_rest_client import ArkhamDbRestClient

import json

class Taboos:
    def __init__(self):
        self.arkham_db_client = ArkhamDbRestClient()
        self.cards = json.loads(json.loads(self.arkham_db_client.get_taboos().text)[0]['cards'])

    def retrieve_taboo_card_codes(self):
        taboo_card_codes = []
        for card in self.cards:
            taboo_card_codes.append(card['code'])
        return taboo_card_codes

    def retrieve_text(self, card_code):
        return self.retrieve_taboo_characteristic(card_code, 'text')
    
    def retrieve_xp(self, card_code):
        return self.retrieve_taboo_characteristic(card_code, 'xp')
    
    def retrieve_deck_limit(self, card_code):
        return self.retrieve_taboo_characteristic(card_code, 'deck_limit')
    
    def retrieve_taboo_characteristic(self, card_code, char_name):
        char_value = None
        card = next(filter(lambda card: card['code'] == card_code, self.cards))
        if char_name in card:
            char_value = card[char_name]
        return char_value