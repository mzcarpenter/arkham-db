from arkham_db_rest_client import ArkhamDbRestClient
from taboos import Taboos
from decks import Decks
from cards import Cards

class TabooCardChecker:
    def __init__(self):
        self.taboos = Taboos()
        self.decks = Decks()
        self.cards = Cards()

    def run_checker(self):
        deck_id = input("Enter your deck ID: ")
        if self.decks.deck_exists(deck_id):
            common_card_codes = self.decks.check_deck_for_card_codes(deck_id, self.taboos.retrieve_taboo_card_codes())
            if common_card_codes:
                for card_code in common_card_codes:
                    print(f'\n*******  {self.cards.map_card_code_to_card_name(card_code)}  *******\n')
                    taboo_text = self.taboos.retrieve_text(card_code)
                    taboo_xp = self.taboos.retrieve_xp(card_code)
                    taboo_deck_limit = self.taboos.retrieve_deck_limit(card_code)
                    if taboo_text is not None:
                        print(f'Text: {taboo_text}')
                    if taboo_xp is not None:
                        print(f'XP: {taboo_xp}')
                    if taboo_deck_limit is not None:
                        print(f'Deck limit: {taboo_deck_limit}')
                    if common_card_codes[-1] == card_code:
                        print('\n')
            else: 
                print("No taboo cards in deck.")
        else:
            print("A deck with such ID does not exist!")


if __name__ == '__main__':
    taboo_card_checker = TabooCardChecker()
    taboo_card_checker.run_checker()