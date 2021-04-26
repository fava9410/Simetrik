import random
import json

class Player():

    def __init__(self, name, limit):
    
        self.amount_of_rounds = 0
        self.name = name
        self.limit = limit
    
    def get_total_games(self):
        return {self.name: self.amount_of_rounds}
    
    def add_round(self):
        self.amount_of_rounds += 1


class Game():

    def __init__(self):
        self.round = 1
        self.history = {}
    
    def set_history(self, round, winner):
        self.history[self.round] = {'players':round.get_round(), 'winner': winner}
    
    def get_history(self):
        return self.history
    
    def add_round(self):
        self.round += 1

    def lets_play(self, ana, juan, jose):        
        players = [ana, juan, jose]

        active_players = random.sample(players,2)
        players.remove(active_players[0])
        players.remove(active_players[1])
        player_rest = players[0]

        while(ana.amount_of_rounds < ana.limit):
            rnd = Round(active_players)

            winner = rnd.get_winner()
            self.set_history(rnd, winner.name)

            active_players.remove(winner)
            loser = active_players[0]
            active_players = [winner, player_rest]
            player_rest = loser
            self.add_round()


class Round():

    def __init__(self, players):
        self.player1 = players[0]
        self.player2 = players[1]

        self.player1.add_round()
        self.player2.add_round()

    def get_round(self):
        return [self.player1.name, self.player2.name]
    
    def get_winner(self):
        return random.choice([self.player1, self.player2])


def main():
    """
        Fuerza bruta para encontrar el juego que cumpla las condiciones, que tristeza :(
    """

    while True:
        ana = Player('ana', 17)
        juan = Player('juan', 10)
        jose = Player('jose', 15)

        pingpong = Game()
        pingpong.lets_play(ana, juan, jose)

        if ana.amount_of_rounds == ana.limit \
            and juan.amount_of_rounds == juan.limit \
            and jose.amount_of_rounds == jose.limit:

            with open('game.json', 'w') as f:
                json.dump(pingpong.get_history(), f, indent=4)
            break

if __name__ == "__main__":
    main()