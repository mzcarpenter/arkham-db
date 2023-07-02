from arkham_db_rest_client import ArkhamDbRestClient

import json

class Decks:
    def __init__(self):
        self.arkham_db_client = ArkhamDbRestClient()

    def deck_exists(self, deck_id):
        return self.arkham_db_client.get_deck(deck_id).headers['content-type'] == 'application/json'
    
    def check_deck_for_card_codes(self, deck_id, taboo_card_codes_arr):
        card_codes_from_deck = list(json.loads(self.arkham_db_client.get_deck(deck_id).text)['slots'].keys())
        return list(set(taboo_card_codes_arr).intersection(card_codes_from_deck))