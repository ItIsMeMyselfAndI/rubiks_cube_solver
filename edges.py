import cube
import inspection
import movement

import numpy as np


class Edges(cube.Cube, inspection.Inspect):
    
    
    def __init__(self, scrambled_faces, buffer_pieces, max_letters_count):
        cube.Cube.__init__(self)
        inspection.Inspect.__init__(self, buffer_pieces, max_letters_count)
        
        self.special_cases = {
            "i":"s", "s":"i",
            "c":"w", "w":"c"
        }
        self.scrambled_faces = scrambled_faces
        
        self.getSwappingAndParityAlgorithms()
        
        self.getCorrectPieces()
        self.getCorrectMirrorPieces()
        
        self.getScrambledPieces()
        self.getScrambledMirrorPieces()

        
    def getSwappingAndParityAlgorithms(self):
        self.swapping_algorithms = {
            "a":"M2'", 
            "b":"R U R' U' M2' U R U' R'", 
            "c":"U2 M' U2 M'", # special
            "d":"L' U' L U M2' U' L' U L",
            "e":"B L' B' M2' B L B'", 
            "f":"B L2 B' M2' B L2 B'",
            "g":"B L B' M2' B L' B'", 
            "h":"L B L' B' M2' B L B' L'",

            "i":"D M' U R2 U' M U R2 U' D' M2'", # special 
            "j":"U R U' M2' U R' U'",
            "k":None, 
            "l":"U' L' U M2' U' L U",
            "m":"B' R B M2' B' R' B", 
            "n":"R' B' R B M2' B' R' B R",
            "o":"B' R' B M2' B' R B", 
            "p":"B' R2 B M2' B' R2 B",
            "q":"U B' R U' B M2' B' U R' B U'", 
            "r":"U' L U M2' U' L' U",
            "s":"M2' D U R2 U' M' U R2 U' M D'", # special 
            "t":"U R' U' M2' U R U'",
            "u":None, 
            "v":"U R2 U' M2' U R2 U'",
            "w":"M U2 M U2", # special 
            "x":"U' L2 U M2' U' L2 U",
        }
        self.parity_algorithm = "D' L2 D M2' D' L2 D"
    

    def getCorrectPieces(self):
        self.correct_pieces = {
            "aq":(self.faces["up"][0][1], self.faces["back"][0][1]), 
            "bm":(self.faces["up"][1][2], self.faces["right"][0][1]), 
            "ci":(self.faces["up"][2][1], self.faces["front"][0][1]), 
            "de":(self.faces["up"][1][0], self.faces["left"][0][1]),
            
            "fl":(self.faces["left"][1][2], self.faces["front"][1][0]), 
            "hr":(self.faces["left"][1][0], self.faces["back"][1][2]),
            
            "nt":(self.faces["right"][1][2], self.faces["back"][1][0]), 
            "pj":(self.faces["right"][1][0], self.faces["front"][1][2]),
            
            "uk":(self.faces["down"][0][1], self.faces["front"][2][1]), 
            "vo":(self.faces["down"][1][2], self.faces["right"][2][1]), 
            "ws":(self.faces["down"][2][1], self.faces["back"][2][1]), 
            "xg":(self.faces["down"][1][0], self.faces["left"][2][1]),
        }
            

    def getCorrectMirrorPieces(self):
        self.correct_pieces["qa"] = self.correct_pieces["aq"][::-1]
        self.correct_pieces["mb"] = self.correct_pieces["bm"][::-1]
        self.correct_pieces["ic"] = self.correct_pieces["ci"][::-1]
        self.correct_pieces["ed"] = self.correct_pieces["de"][::-1]
            
        self.correct_pieces["lf"] = self.correct_pieces["fl"][::-1]
        self.correct_pieces["rh"] = self.correct_pieces["hr"][::-1]
            
        self.correct_pieces["tn"] = self.correct_pieces["nt"][::-1]
        self.correct_pieces["jp"] = self.correct_pieces["pj"][::-1]
            
        self.correct_pieces["ku"] = self.correct_pieces["uk"][::-1]
        self.correct_pieces["ov"] = self.correct_pieces["vo"][::-1]
        self.correct_pieces["sw"] = self.correct_pieces["ws"][::-1]
        self.correct_pieces["gx"] = self.correct_pieces["xg"][::-1]


    def getScrambledPieces(self):
        self.scrambled_pieces = {
            "aq":(self.scrambled_faces["up"][0][1], self.scrambled_faces["back"][0][1]), 
            "bm":(self.scrambled_faces["up"][1][2], self.scrambled_faces["right"][0][1]), 
            "ci":(self.scrambled_faces["up"][2][1], self.scrambled_faces["front"][0][1]), 
            "de":(self.scrambled_faces["up"][1][0], self.scrambled_faces["left"][0][1]),
            
            "fl":(self.scrambled_faces["left"][1][2], self.scrambled_faces["front"][1][0]), 
            "hr":(self.scrambled_faces["left"][1][0], self.scrambled_faces["back"][1][2]),
            
            "nt":(self.scrambled_faces["right"][1][2], self.scrambled_faces["back"][1][0]), 
            "pj":(self.scrambled_faces["right"][1][0], self.scrambled_faces["front"][1][2]),
            
            "uk":(self.scrambled_faces["down"][0][1], self.scrambled_faces["front"][2][1]), 
            "vo":(self.scrambled_faces["down"][1][2], self.scrambled_faces["right"][2][1]), 
            "ws":(self.scrambled_faces["down"][2][1], self.scrambled_faces["back"][2][1]), 
            "xg":(self.scrambled_faces["down"][1][0], self.scrambled_faces["left"][2][1]),
        }
    

    def getScrambledMirrorPieces(self):
        self.scrambled_pieces["qa"] = self.scrambled_pieces["aq"][::-1]
        self.scrambled_pieces["mb"] = self.scrambled_pieces["bm"][::-1]
        self.scrambled_pieces["ic"] = self.scrambled_pieces["ci"][::-1]
        self.scrambled_pieces["ed"] = self.scrambled_pieces["de"][::-1]
            
        self.scrambled_pieces["lf"] = self.scrambled_pieces["fl"][::-1]
        self.scrambled_pieces["rh"] = self.scrambled_pieces["hr"][::-1]
            
        self.scrambled_pieces["tn"] = self.scrambled_pieces["nt"][::-1]
        self.scrambled_pieces["jp"] = self.scrambled_pieces["pj"][::-1]
            
        self.scrambled_pieces["ku"] = self.scrambled_pieces["uk"][::-1]
        self.scrambled_pieces["ov"] = self.scrambled_pieces["vo"][::-1]
        self.scrambled_pieces["sw"] = self.scrambled_pieces["ws"][::-1]
        self.scrambled_pieces["gx"] = self.scrambled_pieces["xg"][::-1]


if __name__ == "__main__":
    my_cube = cube.Cube()
    move = movement.Move()

    scramble_algorithm = "L2 F B L F' B2 L' R' F' L U' B2 R' F D2 R' F' B2 R2 D2 B F D2 U2 R2 D' B2 L F' B'"
    # scramble_algorithm = "U' B2 U L2 D L2 R2 D' B' R D' L R' B2 U2 F' L' U'"
    # scramble_algorithm = "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2"
    # scramble_algorithm = "R L B R F' B' D' F2 L2 U2 R' F2 U' B' F L R2 B F' R' B' L2 U2 R2 B' L2 U' F' L U"
    # scramble_algorithm = "R2 U2 R2 U2 R2 U2"
    print(scramble_algorithm)
    move.executeAlgorithm(scramble_algorithm, my_cube.faces)

    edges = Edges(my_cube.faces, ["uk", "ku"], 22)
    edges.display()
    print()

    my_cube.display()
    edges.inspect("uk", enable_parity=True)
    print(edges.pieces_sequence)
    letters_sequence = edges.getLettersSequence()
    print(" ".join(letters_sequence))
    solution = edges.getSolution(letters_sequence)
    print(edges.is_parity)
    print()
    move.executeAlgorithm(" ".join(solution), my_cube.faces)
    print()
    my_cube.display()
    print()
