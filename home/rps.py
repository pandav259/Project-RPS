#!/usr/bin/env python3
import random

RED = '\033[31m'
GREEN = '\033[32m'
BLUE = '\033[34m'
RESET = '\033[0m'

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        pass

    def learn(self, amove, bmove):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'

    def learn(self, amove, bmove):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, amove, bmove):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Please select Rock, paper or scissors: ")
            if move.lower() in moves:
                return move.lower()

    def learn(self, amove, bmove):
        pass


class ReflectPlayer(Player):
    def __init__(self):
        self.prev_move = random.choice(moves)

    def move(self):
        return self.prev_move

    def learn(self, amove, bmove):
        self.prev_move = amove


class CyclePlayer(Player):
    def __init__(self):
        self.prev_move = random.choice(moves)

    def move(self):
        if self.prev_move == 'rock':
            return 'paper'
        elif self.prev_move == 'paper':
            return 'scissors'
        else:
            return 'rock'

    def learn(self, amove, bmove):
        self.prev_move = amove


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def beats(one, two):
        if one == two:
            return 'tie'
        elif one == 'rock' and two == 'scissors':
            return 'p1'
        elif one == 'paper' and two == 'rock':
            return 'p1'
        elif one == 'scissors' and two == 'paper':
            return 'p1'
        else:
            return 'p2'

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move1, move2)

        winner = Game.beats(move1, move2)
        if winner == 'p1':
            self.score1 += 1
            print("Player 1 wins the round!")
        elif winner == 'p2':
            self.score2 += 1
            print("Player 2 wins the round!")
        else:
            print("Round tied!")

    def play_game(self):
        self.score1 = 0
        self.score2 = 0
        print("\n‼️ Game start! ‼️")

        for round in range(3):
            print(f"\n📢 ROUND {round+1} 📢")
            self.play_round()

        print(f"\n💪 {BLUE}Total scores: {self.score1} : {self.score2}{RESET}")
        if self.score1 > self.score2:
            print(f"\n{GREEN}🎊 Player 1 wins the game!{RESET} 🎊")
        elif self.score2 > self.score1:
            print(f"\n🎊{GREEN} Player 2 wins the game! {RESET}🎊")
        else:
            print(f"{GREEN}\n🤝 Game Tied!{RESET} 🤝")

        print(f"\n{BLUE}Game over! {RESET}\n")


if __name__ == '__main__':
    print(f"\n{GREEN}Welcome to Rock, Paper and Scissors!!!{RESET} 🗿 📃 ✂️\n")
    while True:
        while True:
            print(f"\n{BLUE}Type Starter 😉, Easy 😇, Medium 🤭"
                  f"or Hard 😰 to begin.{RESET}")
            print(f"{RED}Type Exit to quit.{RESET}")
            mode = input("Please select a game mode...\n").lower()
            if mode == 'starter':
                game = Game(HumanPlayer(), RockPlayer())
                break
            elif mode == 'easy':
                game = Game(HumanPlayer(), RandomPlayer())
                break
            elif mode == 'medium':
                game = Game(HumanPlayer(), ReflectPlayer())
                break
            elif mode == 'hard':
                game = Game(HumanPlayer(), CyclePlayer())
                break
            elif mode == 'exit':
                quit()

        game.play_game()

        while True:
            play_again = input(f"{BLUE}Do you wish to play again?"
                               f"Type 'Yes' 👍 or 'No' {RESET}👎\n").lower()
            if 'yes' in play_again:
                break
            elif 'no' in play_again:
                print(f"{GREEN}Thanks for playing! {RESET}🤩")
                quit()
