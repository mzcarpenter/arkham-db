from arkham_db_rest_client import ArkhamDbRestClient
from taboos import Taboos
from decks import Decks
from cards import Cards

class Main:
    def __init__(self):
        self.arkham_db_client = ArkhamDbRestClient()
    """
    Harrigan deck ID: 2870665
    Stella deck ID: 2809440
    """
    def main(self):
        deck_id = input("Enter your deck ID: ")
        if Decks.deck_exists(self, deck_id):
            common_card_codes = Decks.check_deck_for_card_codes(self, deck_id, Taboos.retrieve_taboo_card_codes(self))
            print("\n" + "\n".join(Cards.map_card_codes_to_card_names(self, common_card_codes)) + "\n") if common_card_codes \
                  else print("No taboo cards in deck.")
        else:
            print("A deck with such ID does not exist!")


if __name__ == '__main__':
    main = Main()
    main.main()