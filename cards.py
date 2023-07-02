from arkham_db_rest_client import ArkhamDbRestClient

import json

class Cards:
    def __init__(self):
        self.arkham_db_client = ArkhamDbRestClient()

    def map_card_codes_to_card_names(self, card_codes):
        card_objects = list(map(lambda card_code: json.loads(self.arkham_db_client.get_card(card_code).text), card_codes))
        return list(map(lambda card: card['name'], card_objects))
