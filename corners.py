import cube
import inspection
import movement

import numpy as np

class Corners(cube.Cube, inspection.Inspect):
    
    
    def __init__(self, scrambled_faces, buffer_pieces, max_letters_count):
        cube.Cube.__init__(self)
        inspection.Inspect.__init__(self, buffer_pieces, max_letters_count)

        self.special_cases = {None:None} 
        self.scrambled_faces = scrambled_faces
        
        self.getSwappingAndParityAlgorithms()
        
        self.getCorrectPieces()
        self.getCorrectFirstMirrorPieces()
        self.getCorrectSecondMirrorPieces()
        
        self.getScrambledPieces()
        self.getScrambledFirstMirrorPieces()
        self.getScrambledSecondMirrorPieces()
        
        
    def getSwappingAndParityAlgorithms(self):
        self.swapping_algorithms = {
            "a":None,
            "b":"R2' R U' R' U' R U R' F' R U R' U' R' F R R2",
            "c":"F2 D R U' R' U' R U R' F' R U R' U' R' F R D' F2",
            "d":"F2 R U' R' U' R U R' F' R U R' U' R' F R F2",
            "e":None,
            "f":"F' D R U' R' U' R U R' F' R U R' U' R' F R D' F",
            "g":"F' R U' R' U' R U R' F' R U R' U' R' F R F",
            "h":"D' R R U' R' U' R U R' F' R U R' U' R' F R R' D",
            "i":"F R' R U' R' U' R U R' F' R U R' U' R' F R R F'",
            "j":"R' R U' R' U' R U R' F' R U R' U' R' F R R",
            "k":"R' D' R U' R' U' R U R' F' R U R' U' R' F R D R",
            "l":"F2 R R U' R' U' R U R' F' R U R' U' R' F R R' F2",
            "m":"F R U' R' U' R U R' F' R U R' U' R' F R F'",
            "n":"R' F R U' R' U' R U R' F' R U R' U' R' F R F' R",
            "o":"R2' F R U' R' U' R U R' F' R U R' U' R' F R F' R2",
            "p":"F D R U' R' U' R U R' F' R U R' U' R' F R D' F'",
            "q":"R D' R U' R' U' R U R' F' R U R' U' R' F R D R'",
            "r":None,
            "s":"D F' R U' R' U' R U R' F' R U R' U' R' F R F D'",
            "t":"R R U' R' U' R U R' F' R U R' U' R' F R R'",
            "u":"D R U' R' U' R U R' F' R U R' U' R' F R D'",
            "v":"R U' R' U' R U R' F' R U R' U' R' F R",
            "w":"D' R U' R' U' R U R' F' R U R' U' R' F R D",
            "x":"D2 R U' R' U' R U R' F' R U R' U' R' F R D2",
        }
        self.parity_algorithm = None 


    def getCorrectPieces(self):
        self.correct_pieces = {
            "aer":(self.faces["up"][0][0], self.faces["left"][0][0], self.faces["back"][0][2]),
            "bqn":(self.faces["up"][0][2], self.faces["back"][0][0], self.faces["right"][0][2]),
            "cmj":(self.faces["up"][2][2], self.faces["right"][0][0], self.faces["front"][0][2]),
            "dif":(self.faces["up"][2][0], self.faces["front"][0][0], self.faces["left"][0][2]),
        
            "ugl":(self.faces["down"][0][0], self.faces["left"][2][2], self.faces["front"][2][0]),
            "vkp":(self.faces["down"][0][2], self.faces["front"][2][2], self.faces["right"][2][0]),
            "wot":(self.faces["down"][2][2], self.faces["right"][2][2], self.faces["back"][2][0]),
            "xsh":(self.faces["down"][2][0], self.faces["back"][2][2], self.faces["left"][2][0]),
        }
            

    def getCorrectFirstMirrorPieces(self):
        self.correct_pieces["era"] = self.correct_pieces["aer"][1:] + self.correct_pieces["aer"][0:1]
        self.correct_pieces["qnb"] = self.correct_pieces["bqn"][1:] + self.correct_pieces["bqn"][0:1]
        self.correct_pieces["mjc"] = self.correct_pieces["cmj"][1:] + self.correct_pieces["cmj"][0:1]
        self.correct_pieces["ifd"] = self.correct_pieces["dif"][1:] + self.correct_pieces["dif"][0:1]
            
        self.correct_pieces["glu"] = self.correct_pieces["ugl"][1:] + self.correct_pieces["ugl"][0:1]
        self.correct_pieces["kpv"] = self.correct_pieces["vkp"][1:] + self.correct_pieces["vkp"][0:1]
        self.correct_pieces["otw"] = self.correct_pieces["wot"][1:] + self.correct_pieces["wot"][0:1]
        self.correct_pieces["shx"] = self.correct_pieces["xsh"][1:] + self.correct_pieces["xsh"][0:1]


    def getCorrectSecondMirrorPieces(self):
        self.correct_pieces["rae"] = self.correct_pieces["era"][1:] + self.correct_pieces["era"][0:1]
        self.correct_pieces["nbq"] = self.correct_pieces["qnb"][1:] + self.correct_pieces["qnb"][0:1]
        self.correct_pieces["jcm"] = self.correct_pieces["mjc"][1:] + self.correct_pieces["mjc"][0:1]
        self.correct_pieces["fdi"] = self.correct_pieces["ifd"][1:] + self.correct_pieces["ifd"][0:1]
            
        self.correct_pieces["lug"] = self.correct_pieces["glu"][1:] + self.correct_pieces["glu"][0:1]
        self.correct_pieces["pvk"] = self.correct_pieces["kpv"][1:] + self.correct_pieces["kpv"][0:1]
        self.correct_pieces["two"] = self.correct_pieces["otw"][1:] + self.correct_pieces["otw"][0:1]
        self.correct_pieces["hxs"] = self.correct_pieces["shx"][1:] + self.correct_pieces["shx"][0:1]


    def getScrambledPieces(self):
        self.scrambled_pieces = {
            "aer":(self.scrambled_faces["up"][0][0], self.scrambled_faces["left"][0][0], self.scrambled_faces["back"][0][2]),
            "bqn":(self.scrambled_faces["up"][0][2], self.scrambled_faces["back"][0][0], self.scrambled_faces["right"][0][2]),
            "cmj":(self.scrambled_faces["up"][2][2], self.scrambled_faces["right"][0][0], self.scrambled_faces["front"][0][2]),
            "dif":(self.scrambled_faces["up"][2][0], self.scrambled_faces["front"][0][0], self.scrambled_faces["left"][0][2]),
        
            "ugl":(self.scrambled_faces["down"][0][0], self.scrambled_faces["left"][2][2], self.scrambled_faces["front"][2][0]),
            "vkp":(self.scrambled_faces["down"][0][2], self.scrambled_faces["front"][2][2], self.scrambled_faces["right"][2][0]),
            "wot":(self.scrambled_faces["down"][2][2], self.scrambled_faces["right"][2][2], self.scrambled_faces["back"][2][0]),
            "xsh":(self.scrambled_faces["down"][2][0], self.scrambled_faces["back"][2][2], self.scrambled_faces["left"][2][0]),
        }
    

    def getScrambledFirstMirrorPieces(self):
        self.scrambled_pieces["era"] = self.scrambled_pieces["aer"][1:] + self.scrambled_pieces["aer"][0:1]
        self.scrambled_pieces["qnb"] = self.scrambled_pieces["bqn"][1:] + self.scrambled_pieces["bqn"][0:1]
        self.scrambled_pieces["mjc"] = self.scrambled_pieces["cmj"][1:] + self.scrambled_pieces["cmj"][0:1]
        self.scrambled_pieces["ifd"] = self.scrambled_pieces["dif"][1:] + self.scrambled_pieces["dif"][0:1]
            
        self.scrambled_pieces["glu"] = self.scrambled_pieces["ugl"][1:] + self.scrambled_pieces["ugl"][0:1]
        self.scrambled_pieces["kpv"] = self.scrambled_pieces["vkp"][1:] + self.scrambled_pieces["vkp"][0:1]
        self.scrambled_pieces["otw"] = self.scrambled_pieces["wot"][1:] + self.scrambled_pieces["wot"][0:1]
        self.scrambled_pieces["shx"] = self.scrambled_pieces["xsh"][1:] + self.scrambled_pieces["xsh"][0:1]


    def getScrambledSecondMirrorPieces(self):
        self.scrambled_pieces["rae"] = self.scrambled_pieces["era"][1:] + self.scrambled_pieces["era"][0:1]
        self.scrambled_pieces["nbq"] = self.scrambled_pieces["qnb"][1:] + self.scrambled_pieces["qnb"][0:1]
        self.scrambled_pieces["jcm"] = self.scrambled_pieces["mjc"][1:] + self.scrambled_pieces["mjc"][0:1]
        self.scrambled_pieces["fdi"] = self.scrambled_pieces["ifd"][1:] + self.scrambled_pieces["ifd"][0:1]
            
        self.scrambled_pieces["lug"] = self.scrambled_pieces["glu"][1:] + self.scrambled_pieces["glu"][0:1]
        self.scrambled_pieces["pvk"] = self.scrambled_pieces["kpv"][1:] + self.scrambled_pieces["kpv"][0:1]
        self.scrambled_pieces["two"] = self.scrambled_pieces["otw"][1:] + self.scrambled_pieces["otw"][0:1]
        self.scrambled_pieces["hxs"] = self.scrambled_pieces["shx"][1:] + self.scrambled_pieces["shx"][0:1]


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

    corners = Corners(my_cube.faces, ["aer", "era", "rae"], 21)
    corners.display()
    print()

    my_cube.display()
    corners.inspect("era", enable_parity=False)
    print(corners.pieces_sequence)
    letters_sequence = corners.getLettersSequence()
    print(" ".join(letters_sequence))
    solution = corners.getSolution(letters_sequence)
    print(corners.is_parity)
    print()
    move.executeAlgorithm(" ".join(solution), my_cube.faces)
    print()
    my_cube.display()
    print()