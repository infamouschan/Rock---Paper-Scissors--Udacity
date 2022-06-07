import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input(moves)
            if move in moves:
                return move
            else:
                print("Try Again")


class ReflectPlayer(Player):
    nextMove = None

    def move(self):
        if self.nextMove is None:
            return random.choice(moves)
        else:
            return self.nextMove

    def learn(self, my_move, their_move):
        self.nextMove = their_move


class CyclePlayer(Player):
    lastMove = None

    def move(self):
        if self.lastMove is None:
            return random.choice(moves)
        else:
            position = moves.index(self.lastMove)
            if position == 2:
                return moves[0]
            else:
                return moves[position+1]

    def learn(self, my_move, their_move):
        self.lastMove = my_move


def beats(one, two):
    if one == two:
        return "Tie"
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1Wins = 0
        self.p2Wins = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        didP1Win = beats(move1, move2)
        if didP1Win == "Tie":
            print("> This round is a Tie!")
        elif didP1Win:
            self.p1Wins += 1
            print("> Player 1 won this round!")
        else:
            self.p2Wins += 1
            print("> Player 2 won this round!")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Player 1: {self.p1Wins}\nPlayer 2: {self.p2Wins}")

    def play_game(self):
        print("Game start!")
        self.rounds = 3
        for round in range(self.rounds):
            print(f"\nRound {round}:")
            self.play_round()
        if self.p1Wins == self.p2Wins:
            print("\nThis game is a tie")
        elif self.p1Wins > self.p2Wins:
            print("\nPlayer 1 Won")
        else:
            print("\nPlayer 2 Won")
        print(f"Final scores:\nP1: {self.p1Wins} \nP2: {self.p2Wins}")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), CyclePlayer())
    game.play_game()