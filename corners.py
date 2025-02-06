import cube
import inspection
import movement

import numpy as np

class Corners(cube.Cube, inspection.Inspect):
    
    
    def __init__(self, scrambled_faces, buffer_pieces, max_sequence_len, special_cases={None:None}):
        cube.Cube.__init__(self)
        inspection.Inspect.__init__(self, buffer_pieces, max_sequence_len, special_cases)
        
        self.scrambled_faces = scrambled_faces
        
        self.getSwappingAndParityAlgorithms()
        
        self.getSolvedPieces()
        self.getSolvedFirstMirrorPieces()
        self.getSolvedSecondMirrorPieces()
        
        self.getScrambledPieces()
        self.getScrambledFirstMirrorPieces()
        self.getScrambledSecondMirrorPieces()
        
        
    def _updateUnexploredPieces(self):
        super()._updateUnexploredPieces()

        self.unexplored_pieces.clear()
        for piece in self.unsolved_pieces.keys():
            mirror_piece1 = piece[1:] + piece[0:1]
            mirror_piece2 = mirror_piece1[1:] + mirror_piece1[0:1]
            
            first = ((piece in self.pieces_sequence) and (mirror_piece1 in self.pieces_sequence))
            second = ((mirror_piece1 in self.pieces_sequence) and (mirror_piece2 in self.pieces_sequence))
            third = ((piece in self.pieces_sequence) and (mirror_piece2 in self.pieces_sequence))
            fourth = piece not in self.buffer_pieces
            
            if not (first and second and third) and fourth:
                self.unexplored_pieces.append(piece)

        
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


    def getSolvedPieces(self):
        self.original_pieces = {
            "aer":(self.faces["up"][0][0], self.faces["left"][0][0], self.faces["back"][0][2]),
            "bqn":(self.faces["up"][0][2], self.faces["back"][0][0], self.faces["right"][0][2]),
            "cmj":(self.faces["up"][2][2], self.faces["right"][0][0], self.faces["front"][0][2]),
            "dif":(self.faces["up"][2][0], self.faces["front"][0][0], self.faces["left"][0][2]),
        
            "ugl":(self.faces["down"][0][0], self.faces["left"][2][2], self.faces["front"][2][0]),
            "vkp":(self.faces["down"][0][2], self.faces["front"][2][2], self.faces["right"][2][0]),
            "wot":(self.faces["down"][2][2], self.faces["right"][2][2], self.faces["back"][2][0]),
            "xsh":(self.faces["down"][2][0], self.faces["back"][2][2], self.faces["left"][2][0]),
        }
            

    def getSolvedFirstMirrorPieces(self):
        self.original_pieces["era"] = self.original_pieces["aer"][1:] + self.original_pieces["aer"][0:1]
        self.original_pieces["qnb"] = self.original_pieces["bqn"][1:] + self.original_pieces["bqn"][0:1]
        self.original_pieces["mjc"] = self.original_pieces["cmj"][1:] + self.original_pieces["cmj"][0:1]
        self.original_pieces["ifd"] = self.original_pieces["dif"][1:] + self.original_pieces["dif"][0:1]
            
        self.original_pieces["glu"] = self.original_pieces["ugl"][1:] + self.original_pieces["ugl"][0:1]
        self.original_pieces["kpv"] = self.original_pieces["vkp"][1:] + self.original_pieces["vkp"][0:1]
        self.original_pieces["otw"] = self.original_pieces["wot"][1:] + self.original_pieces["wot"][0:1]
        self.original_pieces["shx"] = self.original_pieces["xsh"][1:] + self.original_pieces["xsh"][0:1]


    def getSolvedSecondMirrorPieces(self):
        self.original_pieces["rae"] = self.original_pieces["era"][1:] + self.original_pieces["era"][0:1]
        self.original_pieces["nbq"] = self.original_pieces["qnb"][1:] + self.original_pieces["qnb"][0:1]
        self.original_pieces["jcm"] = self.original_pieces["mjc"][1:] + self.original_pieces["mjc"][0:1]
        self.original_pieces["fdi"] = self.original_pieces["ifd"][1:] + self.original_pieces["ifd"][0:1]
            
        self.original_pieces["lug"] = self.original_pieces["glu"][1:] + self.original_pieces["glu"][0:1]
        self.original_pieces["pvk"] = self.original_pieces["kpv"][1:] + self.original_pieces["kpv"][0:1]
        self.original_pieces["two"] = self.original_pieces["otw"][1:] + self.original_pieces["otw"][0:1]
        self.original_pieces["hxs"] = self.original_pieces["shx"][1:] + self.original_pieces["shx"][0:1]


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
    scrambled_cube = cube.Cube()
    movement = movement.Move()

    scramble_algorithm = "F U D R2 F2 U' B U B U R2 B' U L2 U B2 U2 F2 L2 U'"
    # scramble_algorithm = "R L B R F' B' D' F2 L2 U2 R' F2 U' B' F L R2 B F' R' B' L2 U2 R2 B' L2 U' F' L U"
    print(scramble_algorithm)
    movement.executeAlgorithm(scramble_algorithm, scrambled_cube.faces)

    corners = Corners(scrambled_cube.faces, ["aer", "era", "rae"], 14)
    corners.display()
    print(corners.original_pieces["era"])
    print(corners.original_pieces["rae"])
    print()

    scrambled_cube.display()
    print(corners.scrambled_pieces["era"])
    print(corners.scrambled_pieces["rae"])
    corners.inspect("era", enable_parity=False)
    print()
    print(corners.pieces_sequence)
    print(corners.letters_sequence)
    print(corners.is_parity)
    movement.executeAlgorithm(" ".join(corners.solution), scrambled_cube.faces)
    corners.display()
    print(" ".join(corners.solution))
    print()
