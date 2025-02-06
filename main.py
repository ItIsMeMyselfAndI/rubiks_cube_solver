import cube
import movement
import scramble
import edges
import corners

def main():
    my_cube = cube.Cube()
    move = movement.Move()
    
    # generate scramble
    new_scramble = scramble.Scramble()
    new_scramble.generateAlgorithm()
    # scramble_algorithm = " ".join(new_scramble.algorithm)
    scramble_algorithm = "L2 F B L F' B2 L' R' F' L U' B2 R' F D2 R' F' B2 R2 D2 B F D2 U2 R2 D' B2 L F' B'"
    
    # execute scramble
    move.executeAlgorithm(scramble_algorithm, my_cube.faces)
    my_cube.display()
    
    my_edges = edges.Edges(my_cube.faces, ["uk", "ku"], 22)
    my_corners = corners.Corners(my_cube.faces, ["aer", "era", "rae"], 21)
    my_cube.display()
    print()

    my_edges.inspect("uk", enable_parity=True)
    my_corners.inspect("era", enable_parity=True)
    
    print(my_edges.pieces_sequence)
    print(my_corners.pieces_sequence)
    
    edges_sequence = my_edges.getLettersSequence()
    corners_sequence = my_corners.getLettersSequence()
    
    print(" ".join(edges_sequence))
    print(" ".join(corners_sequence))
    edge_solution = my_edges.getSolution(edges_sequence)
    corner_solution = my_corners.getSolution(corners_sequence)
    print(my_edges.is_parity)
    print(my_corners.is_parity)
    print()
    
    for algorithm in edge_solution:
        print(algorithm)
        move.executeAlgorithm(algorithm, my_cube.faces)
    print()
    my_cube.display()
    for algorithm in corner_solution:
        print(algorithm)
        move.executeAlgorithm(algorithm, my_cube.faces)
    print()
    my_cube.display()


    # # scramble_algorithm = "B' F' R2 U2 B F' U2 L' F' D2 U' L2 R' F2 D B F' D L2 B R' L2 D2 U B' R2 L' B2 R2 L'"
    # # scramble the cube
    # move.executeAlgorithm(scramble_algorithm, my_cube.faces)

    # # inspect edges 
    # my_edges = edges.Edges(my_cube.faces, ["uk", "ku"], 22)
    # my_edges.inspect("uk", enable_parity=True)
    # edges_sequence = my_edges.getLettersSequence()
    # edge_solution = my_edges.getSolution(edges_sequence)
    # # inspect corners
    # my_corners = corners.Corners(my_cube.faces, ["aer", "era", "rae"], 21)
    # my_corners.inspect("era", enable_parity=False)
    # corners_sequence = my_corners.getLettersSequence()
    # corner_solution = my_corners.getSolution(corners_sequence)


    # print("[Scrambled Cube]")
    # print()
    # my_cube.display()
    # print()
    # print(f"\tScramble: {scramble_algorithm}")
    # print()
    # print("[Solution Sequence]")
    # print()
    # print(my_edges.pieces_sequence)
    # print(f"\tEdges: {" ".join(edges_sequence)}")
    # print(f"\tParity: {my_edges.is_parity}")
    # print(my_edges.pieces_sequence)
    # print(f"\tCorners: {" ".join(corners_sequence)}")
    # print()
    # print("[Solved Cube]")
    # print()
    # for algorithm in edge_solution:
    #     move.executeAlgorithm(algorithm, my_cube.faces)
    # my_cube.display()
    # print()
    # for algorithm in corner_solution:
    #     move.executeAlgorithm(algorithm, my_cube.faces)
    # my_cube.display()
    # print()
    # print(f"\tEdges: {my_edges.solved_pieces}")
    # print(f"\tCorners: {my_corners.solved_pieces}")



if __name__ == "__main__":
    main()