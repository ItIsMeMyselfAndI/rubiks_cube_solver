import random

class Scramble:


    def __init__(self):
        self.move_set = [
            "U", "U'", "U2", 
            "D", "D'", "D2",
            "F", "F'", "F2",
            "B", "B'", "B2",
            "L", "L'", "L2",
            "R", "R'", "R2",
        ]
        self.algorithm = []


    def generateAlgorithm(self):
        for i in range(30):
            try:
                last_move = self.algorithm[i-1][0]
            except IndexError:
                last_move = None
            try:
                last_last_move = self.algorithm[i-2][0]
            except IndexError:
                last_last_move = None

            move_set = [move for move in self.move_set if move[0] not in [last_move, last_last_move]]
            move = random.choice(move_set)
            self.algorithm.append(move)


if __name__ == "__main__":
    scramble = Scramble()
    scramble.generateAlgorithm()
    print(" ".join(scramble.algorithm))