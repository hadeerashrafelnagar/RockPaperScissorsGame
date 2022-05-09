#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random
moves = ['rock', 'paper', 'scissors']
n_round = int(input("\u001b[1m\u001b[35mNumber of Rounds From 1 To 5 --->"))
"""The Player class is the parent class for all of the Players
in this game"""


class Player:

    my_move = None
    their_move = None

    def move(self):
        pass

    def learn(self, my_move, their_move):
        pass

    def choose(self):
        # A method for the human player
        choice = input( u"\u001b[31mIn Lower Case{rock,paper,scissors}")
        while choice not in moves:
            if choice == 'quit':
                print("\u001b[35;1m'BYE BYE!'")
                return exit()
            print("\u001b[35;1m' Invalid Input.Please Try Again'")
            choice = input("'\u001b[34;1mIn\' Lower Case{rock,paper,scissors}")
        else:
            return (choice)


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


def final_score(Hscore, Cscore):
    # A function for the final score.
    if Hscore > Cscore:
        return ("\u001b[32m'Congratulations! You Won'")
    elif Hscore < Cscore:
        print("\u001b[31mGAME OVER!")
        return ("\u001b[31m'Oh , You Lose'")
    else:
        return ("\u001b[33m'No Winner Today'")


class RandomPlayer(Player):
    # A player that chooses its moves randomly.
    def move(self):
        return (random.choice(moves))


class ReflectPlayer(Player):
    '''A player that remembers and imitates what
    the human player did in the previous round.'''
    def move(self):
        if self.my_move is None:
            return (random.choice(moves))
        if self.my_move == "rock":
            return ("rock")
        elif self.my_move == "paper":
            return ("paper")
        else:
            return ("scissors")

    def learn(self, my_move, their_move):
        self.my_move = my_move


class RockPlayer(Player):
    # A player that always plays 'rock'.
    def move(self):
        return ("rock")


class HumanPlayer(Player):
    # The human player.
    def choose(self):
        return (Player.choose)


class CyclePlayer(Player):
    # A player that cycles through the three moves.
    def move(self):
        if self.their_move is None:
            return (random.choice(moves))
        if self.their_move == "rock":
            return ("paper")
        elif self.their_move == "paper":
            return ("scissors")
        else:
            return ("rock")

    def learn(self, my_move, their_move):
        self.their_move = their_move


class Game:

    def __init__(self, p1, p2):
        super().__init__()
        self.p1 = p1
        self.p2 = p2
        self.p1.Hscore = 0
        self.p2.Cscore = 0

    def rounds(self):
        # A method for th number of rounds.
        if n_round == 1:
            self.play_round
        else:
            self.play_game

    def play_round(self):
        move1 = self.p1.choose()
        move2 = self.p2.move()
        self.p2.learn(move1, move2)
        print(f"\u001b[35;1mHumanPlayer:{move1}  ComputerPlayer: {move2}")
        if beats(move1, move2):
            print("\u001b[37m'You Win This Round'")
            self.p1.Hscore += 1
        elif beats(move2, move1):
            self.p2.Cscore += 1
            print("\u001b[37m'You Lose This Round'")
        else:
            print("\u001b[37m'It Is A Tie!!!'")

    def play_game(self):
        print("\u001b[36mGame Start!")
        for round in range(n_round):
            print(f"\u001b[36;1mRound {round}:")
            self.play_round()
        print("\u001b[34;1mFinal scores:")
        print(f"\u001b[36;1m You: { self.p1.Hscore}")
        print(f"\u001b[36;1m Computer: { self.p2.Cscore}")
        print(final_score(self.p1.Hscore,  self.p2.Cscore))


if __name__ == '__main__':
    players = [RockPlayer(), RandomPlayer(), ReflectPlayer(), CyclePlayer()]
    player = random.choice(players)
    game = Game(Player(), player)
    game.play_game()
