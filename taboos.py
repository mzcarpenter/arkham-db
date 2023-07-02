from arkham_db_rest_client import ArkhamDbRestClient

import json

class Taboos:
    def __init__(self):
        self.arkham_db_client = ArkhamDbRestClient()

    def retrieve_taboo_card_codes(self):
        taboo_card_codes = []
        cards_objects = list(map(lambda taboo_object: taboo_object['cards'], json.loads(self.arkham_db_client.get_taboos().text)))
        for nested_card_objects in cards_objects:
            for nested_card_object in json.loads(nested_card_objects):
                taboo_card_codes.append(nested_card_object['code'])
        return taboo_card_codes