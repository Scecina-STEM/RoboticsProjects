class Casino : 
    class Table :
        def __init__ (self, dealer:str, players:list[str]):
            """...

            Args:
            dealer:str - just a guy
            players:list[str] - suspect

            """
            self.dealer = dealer
            self.players = players
        def search(self, name : str)->bool:
            for player in self.players:
                if player == name:
                    return True
            return False