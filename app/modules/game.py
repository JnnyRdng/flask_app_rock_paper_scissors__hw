from random import choice


class Game:
    def __init__(self):
        self.choices = {}
        self.valid_choices = ["rock", "paper", "scissors"]

    def play_round(self, player1, player2):
        p1_choice = player1.choice.lower()
        p2_choice = player2.choice.lower()
        if p1_choice in self.valid_choices and p2_choice in self.valid_choices:
            if p1_choice == p2_choice:
                return None
            if p1_choice == "paper":
                if p2_choice == "rock":
                    return player1
                else:
                    return player2
            if p1_choice == "rock":
                if p2_choice == "paper":
                    return player2
                else:
                    return player1
            if p1_choice == "scissors":
                if p2_choice == "paper":
                    return player1
                else:
                    return player2
        else:
            return False

    def decide_cpu_move(self, cpu):
        move = choice(self.valid_choices)
        cpu.choice = move
        return cpu
