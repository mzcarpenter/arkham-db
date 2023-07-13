from arkham_db_rest_client import ArkhamDbRestClient

import json

class Cards:
    def __init__(self):
        self.arkham_db_client = ArkhamDbRestClient()

    def map_card_code_to_card_name(self, card_code):
        card_object = json.loads(self.arkham_db_client.get_card(card_code).text)
        return card_object['name'].upper()
