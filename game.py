import re
from spellchecker import SpellChecker

class Game:
    def __init__(self) -> None:
        return

    def check_valid_chars(self, word):
        checker = re.compile('[^a-zA-Z\s\-\']')
        if not checker.match(word) == None:
            return False
        else:
            return True
        
    def check_valid_word(self, word):
        dictionary = SpellChecker()
        return dictionary[word]
    
    def guess(self, winner, guess):
        guess_composition = []
        if winner == guess:
             return True
        if not self.check_valid_chars(guess):
             return False
        if not self.check_valid_word(guess):
             return False
        for x in range(0, 5):
                    current_letter = guess[x]
                    if current_letter == winner[x]:
                        guess_composition.append("\u2713") #sympolizes correct
                    elif guess[x] in self.winner:
                        guess_composition.append("\u229A") #wrong location
                    else:
                        guess_composition.append("X") #not in the word

        return guess_composition
    
