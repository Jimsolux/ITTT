from html.parser import HTMLParser
import time
from html.parser import HTMLParser
from html.entities import name2codepoint

class ChessdotcomParser(HTMLParser):
    def __init__(self):
        super(ChessdotcomParser, self).__init__()
        self.game_over = False
        self.find_winner = False
        self.has_won = False
        self.find_move_score = False  # directive: go and find a move score
        self.found_move_score = False # process data: used to parse the move score data
        self.move_scores = []
        print("parser set up!")

    def handle_starttag(self, tag, attrs):
        if (tag == "div" and len(attrs) > 0):
            self.handle_div(tag, attrs)
        if (tag == "a" and len(attrs) > 0):
            self.handle_a(tag, attrs)

    def handle_data(self, data: str):
        if self.find_winner:
            self.parse_winner(data)
        elif self.found_move_score and self.find_move_score:
            print(f"found move feedback: {data}")
            self.move_scores.append(float(data))
            self.found_move_score = False
            self.find_move_score = False

    def parse_winner(self, data):
        if data == " You Beat ":
            self.has_won = True
        elif data == "Fighter Won":
            self.has_won = False
        else:
            self.has_won = False
        self.find_winner = False
        print(f'has won: {self.has_won}')

    def handle_div(self, tag, args):
        for arg in args:
            if arg[0] == "class" and arg[1] == 'modal-game-over-header-title modal-game-over-header-show-title':
                if self.game_over == False: 
                    print("GAME OVER")
                    self.game_over = True
                    self.find_winner = True

    def handle_a(self, tag, args):
        for arg in args:
            if arg[0] == "class" and (arg[1] == 'score-text-score move-feedback-row-score' or arg[1] == 'score-text-score score-text-negative move-feedback-row-score'):
                self.found_move_score = True