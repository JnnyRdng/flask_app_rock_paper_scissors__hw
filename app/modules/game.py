class Game:
    def __init__(self):
        self.choices = {}
        self.valid_choices = ["rock", "paper", "scissors"]

    def play_round(self, player1, player2):
        if player1.choice == player2.choice:
            return None
        if player1.choice == "paper":
            if player2.choice == "rock":
                return player1
            else:
                return player2
        if player1.choice == "rock":
            if player2.choice == "paper":
                return player2
            else:
                return player1
        if player1.choice == "scissors":
            if player2.choice == "paper":
                return player1
            else:
                return player2

