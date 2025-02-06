import numpy as np
import random

class Inspect:


    def __init__(self, buffer_pieces, max_sequence_len, special_cases):
        self.buffer_pieces = buffer_pieces
        self.max_sequence_len = max_sequence_len
        self.special_cases = special_cases

        self.unexplored_pieces = []
        self.pieces_sequence = []
        self.letters_sequence = []
        self.is_parity = False


    def inspect(self, start_piece, enable_parity=False):
        self.getUnsolvedPieces()
        print(self.unsolved_pieces.keys())
        self.appendPiecesSequence(start_piece)
        self.appendLettersSequence()
        if enable_parity:
            self.checkIfParity()
        self.getSolution()


    def getUnsolvedPieces(self):
        self.unsolved_pieces = {}
        for piece in self.original_pieces.keys():
            solved_piece_colors = self.original_pieces[piece]
            scrambled_piece_colors = self.scrambled_pieces[piece]
            if (not np.array_equiv(scrambled_piece_colors, solved_piece_colors)) or (piece in self.buffer_pieces):
                self.unsolved_pieces[piece] = scrambled_piece_colors


    def appendPiecesSequence(self, piece):
        if piece == None:
            return
        elif self.max_sequence_len == len(self.pieces_sequence):
            self.pieces_sequence.pop()
            return
        
        self._updateUnexploredPieces()
        unsolved_piece_colors = self._getUnsolvedPieceColors(piece)
        piece = self._getCorrespondingSolvedPiece(unsolved_piece_colors)
        # select other piece
        piece = self._selectUnexploredPieceIfCurrentPieceIsBuffer(piece)
        piece = self._selectUnexploredPieceIfCurrentPieceIsExplored(piece)        

        if piece == None:
            return 
        self.pieces_sequence.append(piece)
        self.appendPiecesSequence(piece)


    def _updateUnexploredPieces(self):
        pass

    def _getUnsolvedPieceColors(self, piece):
        for unsolved_piece, unsolved_piece_colors in self.unsolved_pieces.items():
            if piece == unsolved_piece:
                return unsolved_piece_colors


    def _getCorrespondingSolvedPiece(self, unsolved_piece_colors):
        for solved_piece, solved_piece_colors in self.original_pieces.items():
            if np.array_equal(unsolved_piece_colors, solved_piece_colors):
                return solved_piece 


    def _selectUnexploredPieceIfCurrentPieceIsBuffer(self, piece):
        if (piece in self.buffer_pieces):

            if (len(self.unexplored_pieces) == 0):
                return None
            piece = random.choice(self.unexplored_pieces)

        return piece


    def _selectUnexploredPieceIfCurrentPieceIsExplored(self, piece):
        if piece == None:
            return piece
         
        elif (piece in self.pieces_sequence) or (piece[::-1] in self.pieces_sequence):
            self.pieces_sequence.append(piece)

            if len(self.unexplored_pieces) == 0:
                return None
            piece = random.choice(self.unexplored_pieces)

        return piece


    def appendLettersSequence(self):
        for i, piece in enumerate(self.pieces_sequence):
            if (i % 2 != 0) and (piece[0] in self.special_cases.keys()):
                letter = self.special_cases[piece[0]]
            else: 
                letter = piece[0]
            self.letters_sequence.append(letter)


    def checkIfParity(self): 
        if len(self.letters_sequence) % 2 != 0:
            self.is_parity = True


    def getSolution(self):
        self.solution = []
        for letter in self.letters_sequence:
            algorithm = self.swapping_algorithms[letter]
            self.solution.append(algorithm)
        
        if self.is_parity:
            algorithm = self.parity_algorithm
            self.solution.append(algorithm)


    def displaySolution(self, label):
        for i, algorithm in enumerate(self.solution):
            if i == 0:
                print(f"\t{label:>8} {algorithm}")
                continue
            print(f"\t{"":>8} {algorithm}")