import numpy as np
import random


class Inspect:


    def __init__(self, buffer_pieces, max_letters_count):
        self.buffer_pieces = buffer_pieces
        self.max_letters_count = max_letters_count

        self.solved_pieces = []
        self.unexplored_pieces = []
        self.pieces_sequence = []
        self.is_parity = False


    def inspect(self, buffer_piece, enable_parity=False):
        self._getAlreadySolvedPieces()       
        self._updateUnexploredPieces()
        
        piece = buffer_piece
        letters_count = len(self.solved_pieces)
        while letters_count < self.max_letters_count:
            self._updateUnexploredPieces()
            piece = self._getCorrespondingCorrectPiece(piece)
            piece = self._selectAnotherUnexploredPieceIfBuffer(piece)
            self.pieces_sequence.append(piece)
            
            letters_count = len(self.solved_pieces)
        
        if enable_parity:
            self._checkIfParity()


    def _getAlreadySolvedPieces(self):
        for piece, piece_colors in self.scrambled_pieces.items():
            correct_piece_colors = self.correct_pieces[piece]
            if np.array_equal(piece_colors, correct_piece_colors) and (piece not in self.buffer_pieces):
                self.solved_pieces.append(piece)


    def _updateUnexploredPieces(self):
        self.unexplored_pieces.clear()
        for piece in self.scrambled_pieces.keys():
            if (piece not in self.solved_pieces) and (piece not in self.buffer_pieces):
                self.unexplored_pieces.append(piece)


    def _getCorrespondingCorrectPiece(self, piece):
        piece_colors = self.scrambled_pieces[piece]
        for correct_piece, correct_piece_colors in self.correct_pieces.items():
            if np.array_equal(piece_colors, correct_piece_colors):
                return correct_piece


    def _selectAnotherUnexploredPieceIfBuffer(self, piece):
        had_reselected = False
        if (piece in self.buffer_pieces) or (piece in self.solved_pieces):
            piece = random.choice(self.unexplored_pieces)
            had_reselected = True

        if not had_reselected:
            self.__updateSolvedPieces(piece)

        return piece


    def __updateSolvedPieces(self, piece):
        mirror_piece_1 = piece[1:] + piece[0:1]
        mirror_piece_2 = mirror_piece_1[1:] + mirror_piece_1[0:1]

        pieces = [piece, mirror_piece_1, mirror_piece_2]

        for piece in pieces:
            if piece not in self.solved_pieces:
                self.solved_pieces.append(piece)


    def _checkIfParity(self):
        if len(self.pieces_sequence) % 2 != 0:
            self.is_parity = True


    def getLettersSequence(self):
        letters_sequence = []
        for i, piece in enumerate(self.pieces_sequence):
            
            if (i % 2 != 0) and (piece[0] in self.special_cases.keys()):
                special_case = self.special_cases[piece[0]]
                letters_sequence.append(special_case)
            else:
                letters_sequence.append(piece[0])

        return letters_sequence


    def getSolution(self, letters_sequence):
        solution = []
        for letter in letters_sequence:
            algorithm = self.swapping_algorithms[letter]
            solution.append(algorithm)

        if self.is_parity:
            solution.append(self.parity_algorithm)

        return solution