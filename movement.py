import numpy as np


class Move:
    

    def executeAlgorithm(self, algorithm, faces):
        algorithm = algorithm.split(" ")
        algorithm = self._removeBlanks(algorithm)
        for move in algorithm:
            symbol, repetition, direction = self._getMoveInfo(move)
            for i in range(repetition):
                self._moveFace(symbol, faces, direction)
                if direction == 1:
                    self._moveAffectedFacesClockwise(symbol, faces)
                else:
                    self._moveAffectedFacesCounter(symbol, faces)


    def _removeBlanks(self, algorithm):
        new_algorithm = []
        for move in algorithm:
            if not (move == " " or move == "" or move == None):
                new_algorithm.append(move.strip())
        return new_algorithm


    def _getMoveInfo(self, move):
        symbol = move[0]
        repetition = 1  # default
        direction = 1   # default
        
        length = len(move)
        if (length == 3):
            repetition = move[1]
            direction = -1
        
        elif (length == 2):
            if (move[1] == "'"):
                direction = -1
            else:
                repetition = move[1]
        
        return symbol, int(repetition), direction


    def _moveFace(self, symbol, faces, direction):
        if symbol == "U": word = "up"
        elif symbol == "D": word = "down"
        elif symbol == "L": word = "left"
        elif symbol == "R": word = "right"
        elif symbol == "F": word = "front"
        elif symbol == "B": word = "back"
        elif symbol == "M":
            return

        face = faces[word]
        if direction == 1:
            faces[word] = self.__twist_clockwise(face)
        else:
            faces[word] = self.__twist_counter(face)


    def __twist_clockwise(self, face):
        # 0 1 2     6 3 0
        # 3 4 5     7 4 1
        # 6 7 8     8 5 2
        new_face = np.array([
            face[:, 0][::-1],
            face[:, 1][::-1],
            face[:, 2][::-1],
        ])
        return new_face


    def __twist_counter(self, face):
        # 0 1 2     2 5 8
        # 3 4 5     1 4 7  
        # 6 7 8     0 3 6
        new_face = np.array([
            face[:, 2],
            face[:, 1],
            face[:, 0],
        ])
        return new_face


    def _moveAffectedFacesClockwise(self, symbol, faces):
        # - - - - - - - - - - - - - - - - -
        # | $ $ $ | w w w | $ $ $ | $ $ $ |
        # | $ $ $ | w w w | $ $ $ | $ $ $ |
        # | $ $ $ | w w w | $ $ $ | $ $ $ |
        # - - - - - - - - - - - - - - - - -
        # | o o o | g g g | r r r | b b b |
        # | o o o | g g g | r r r | b b b |
        # | o o o | g g g | r r r | b b b |
        # - - - - - - - - - - - - - - - - -
        # | $ $ $ | y y y | $ $ $ | $ $ $ |
        # | $ $ $ | y y y | $ $ $ | $ $ $ |
        # | $ $ $ | y y y | $ $ $ | $ $ $ |
        # - - - - - - - - - - - - - - - - -
        if symbol == "U":
            left_top = faces["left"][0].copy()
            faces["left"][0] = faces["front"][0]
            faces["front"][0] = faces["right"][0]
            faces["right"][0] = faces["back"][0]
            faces["back"][0] = left_top
        elif symbol == "D":
            right_bot = faces["right"][2].copy()
            faces["right"][2] = faces["front"][2]
            faces["front"][2] = faces["left"][2]
            faces["left"][2] = faces["back"][2] 
            faces["back"][2] = right_bot

        elif symbol == "L":
            down_left = faces["down"][:, 0].copy()
            faces["down"][:, 0] = faces["front"][:, 0]
            faces["front"][:, 0] = faces["up"][:, 0]
            faces["up"][:, 0] = faces["back"][:, 2][::-1]
            faces["back"][:, 2] = down_left[::-1]
        elif symbol == "R":
            up_right = faces["up"][:, 2].copy()
            faces["up"][:, 2] = faces["front"][:, 2]
            faces["front"][:, 2] = faces["down"][:, 2]
            faces["down"][:, 2] = faces["back"][:, 0][::-1]
            faces["back"][:, 0] = up_right[::-1]
        
        elif symbol == "F":
            up_bot = faces["up"][2].copy()
            faces["up"][2] = faces["left"][:, 2][::-1]
            faces["left"][:, 2] = faces["down"][0]
            faces["down"][0] = faces["right"][:, 0][::-1]
            faces["right"][:, 0] = up_bot
        elif symbol == "B":
            down_bot = faces["down"][2].copy()
            faces["down"][2] = faces["left"][:, 0]
            faces["left"][:, 0] = faces["up"][0][::-1]
            faces["up"][0] = faces["right"][:, 2]
            faces["right"][:, 2] = down_bot[::-1]

        elif symbol == "M":
            down_mid = faces["down"][:, 1].copy()
            faces["down"][:, 1] = faces["front"][:, 1]
            faces["front"][:, 1] = faces["up"][:, 1]
            faces["up"][:, 1] = faces["back"][:, 1][::-1]
            faces["back"][:, 1] = down_mid[::-1]


    def _moveAffectedFacesCounter(self, symbol, faces):
        # - - - - - - - - - - - - - - - - -
        # | $ $ $ | w w w | $ $ $ | $ $ $ |
        # | $ $ $ | w w w | $ $ $ | $ $ $ |
        # | $ $ $ | w w w | $ $ $ | $ $ $ |
        # - - - - - - - - - - - - - - - - -
        # | o o o | g g g | r r r | b b b |
        # | o o o | g g g | r r r | b b b |
        # | o o o | g g g | r r r | b b b |
        # - - - - - - - - - - - - - - - - -
        # | $ $ $ | y y y | $ $ $ | $ $ $ |
        # | $ $ $ | y y y | $ $ $ | $ $ $ |
        # | $ $ $ | y y y | $ $ $ | $ $ $ |
        # - - - - - - - - - - - - - - - - -
        if symbol == "U":
            right_top = faces["right"][0].copy()
            faces["right"][0] = faces["front"][0]
            faces["front"][0] = faces["left"][0]
            faces["left"][0] = faces["back"][0] 
            faces["back"][0] = right_top
        elif symbol == "D":
            left_bot = faces["left"][2].copy()
            faces["left"][2] = faces["front"][2]
            faces["front"][2] = faces["right"][2]
            faces["right"][2] = faces["back"][2]
            faces["back"][2] = left_bot

        elif symbol == "L":
            up_left = faces["up"][:, 0].copy()
            faces["up"][:, 0] = faces["front"][:, 0]
            faces["front"][:, 0] = faces["down"][:, 0]
            faces["down"][:, 0] = faces["back"][:, 2][::-1]
            faces["back"][:, 2] = up_left[::-1]
        elif symbol == "R":
            down_right = faces["down"][:, 2].copy()
            faces["down"][:, 2] = faces["front"][:, 2]
            faces["front"][:, 2] = faces["up"][:, 2]
            faces["up"][:, 2] = faces["back"][:, 0][::-1]
            faces["back"][:, 0] = down_right[::-1]
        
        elif symbol == "F":
            down_top = faces["down"][0].copy()
            faces["down"][0] = faces["left"][:, 2]
            faces["left"][:, 2] = faces["up"][2][::-1]
            faces["up"][2] = faces["right"][:, 0]
            faces["right"][:, 0] = down_top [::-1]
        elif symbol == "B":
            up_top = faces["up"][0].copy()
            faces["up"][0] = faces["left"][:, 0][::-1]
            faces["left"][:, 0] = faces["down"][2]
            faces["down"][2] = faces["right"][:, 2][::-1]
            faces["right"][:, 2] = up_top

        elif symbol == "M":
            up_mid = faces["up"][:, 1].copy()
            faces["up"][:, 1] = faces["front"][:, 1]
            faces["front"][:, 1] = faces["down"][:, 1]
            faces["down"][:, 1] = faces["back"][:, 1][::-1]
            faces["back"][:, 1] = up_mid[::-1]

