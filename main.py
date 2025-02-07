import cube
import movement
import scramble
import edges
import corners

def main():
    my_cube = cube.Cube()
    my_cube.display()
    move = movement.Move()
    
    # generate scramble
    new_scramble = scramble.Scramble()
    new_scramble.generateAlgorithm()
    scramble_algorithm = " ".join(new_scramble.algorithm)
    # scramble_algorithm = "L' R U' D' R2 B D F U' B2 D L U R L2 U F2 B' L2 D2 B' R U L2 F R' D U2 B2 D2"
    # scramble_algorithm = "L2 F B L F' B2 L' R' F' L U' B2 R' F D2 R' F' B2 R2 D2 B F D2 U2 R2 D' B2 L F' B'"
    # scramble_algorithm = "U' B2 U L2 D L2 R2 D' B' R D' L R' B2 U2 F' L' U'"
    # scramble_algorithm = "U R2 F B R B2 R U2 L B2 R U' D' R2 F R' L B2 U2 F2"
    # scramble_algorithm = "R L B R F' B' D' F2 L2 U2 R' F2 U' B' F L R2 B F' R' B' L2 U2 R2 B' L2 U' F' L U"
    # scramble_algorithm = "R2 U2 R2 U2 R2 U2"
    print(scramble_algorithm)
    move.executeAlgorithm(scramble_algorithm, my_cube.faces)
    my_cube.display()

    
    # inspect edges 
    my_edges = edges.Edges(my_cube.faces, ["uk", "ku"], 22)
    my_edges.inspect("uk", enable_parity=True)
    edges_sequence = my_edges.getLettersSequence()
    edge_solution = my_edges.getSolution(edges_sequence)
    # inspect corners 
    my_corners = corners.Corners(my_cube.faces, ["aer", "era", "rae"], 21)
    my_corners.inspect("era", enable_parity=False)
    corners_sequence = my_corners.getLettersSequence()
    corner_solution = my_corners.getSolution(corners_sequence)

    # execute solutions
    move.executeAlgorithm(" ".join(edge_solution), my_cube.faces)
    my_cube.display()
    move.executeAlgorithm(" ".join(corner_solution), my_cube.faces)
    my_cube.display()



if __name__ == "__main__":
    main()