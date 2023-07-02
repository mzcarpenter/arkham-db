from rest_client import RestClient

class ArkhamDbRestClient:
    __API_PUBLIC_ENDPOINT_PATH = 'api/public'

    def __init__(self):
        self.rest_client = RestClient()

    def get_taboos(self):
        return self.rest_client.get(f'{ArkhamDbRestClient.__API_PUBLIC_ENDPOINT_PATH}/taboos')
    
    def get_deck(self, deck_id):
        return self.rest_client.get(f'{ArkhamDbRestClient.__API_PUBLIC_ENDPOINT_PATH}/deck/{deck_id}.json')
    
    def get_card(self, card_id):
        return self.rest_client.get(f'{ArkhamDbRestClient.__API_PUBLIC_ENDPOINT_PATH}/card/{card_id}.json')