from itertools import combinations, permutations

class MyNumber:

    def __init__(self):
        self.possible_numbers = ['1', '4', '6', '7', '8', '9']
        # self.numbers.append()
        self.combo = list(permutations(self.possible_numbers, 3))
    
    def showNumbers(self):
        print(self.combo)

    def getNumbers(self):
        return self.combo
