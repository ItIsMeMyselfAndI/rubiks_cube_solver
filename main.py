import cube
import movement
import scramble
import edges
import corners

def main():
    my_cube = cube.Cube()
    move = movement.Move()
    new_scramble = scramble.Scramble()
    
    # generate scramble
    new_scramble.generateAlgorithm()
    # scramble_algorithm = " ".join(new_scramble.algorithm)
    scramble_algorithm = "B' F' R2 U2 B F' U2 L' F' D2 U' L2 R' F2 D B F' D L2 B R' L2 D2 U B' R2 L' B2 R2 L'"
    # scramble the cube
    move.executeAlgorithm(scramble_algorithm, my_cube.faces)

    # inspect edges 
    special_cases = {
        "i":"s", "s":"i",
        "c":"w", "w":"c"
    }
    my_edges = edges.Edges(my_cube.faces, ["uk", "ku"], 24, special_cases)
    my_edges.inspect("uk", enable_parity=True)
    edges_sequence = my_edges.letters_sequence
    edge_solution = my_edges.solution
    # inspect corners
    my_corners = corners.Corners(my_cube.faces, ["aer", "era", "rae"], 16)
    my_corners.inspect("era", enable_parity=False)
    corners_sequence = my_corners.letters_sequence
    corner_solution = my_corners.solution


    print("[Unsolved Cube]")
    my_cube.display()
    print()
    print(f"\tScramble: {scramble_algorithm}")
    print()
    print("[Sequences]")
    print(f"\t{my_edges.pieces_sequence}")
    print(f"\tEdges: {" ".join(edges_sequence)}")
    print(f"\tParity: {my_edges.is_parity}")
    print(f"\t{my_corners.pieces_sequence}")
    print(f"\tCorners: {" ".join(corners_sequence)}")
    print()
    print("[Solutions]")
    my_edges.displaySolution("Edges:")
    my_corners.displaySolution("Corners:")
    print()
    print("[Solved Cube]")
    move.executeAlgorithm(" ".join(edge_solution), my_cube.faces)
    my_cube.display()
    move.executeAlgorithm(" ".join(corner_solution), my_cube.faces)
    my_cube.display()
    # print()


    # solution_algorithm = input("Enter solution: ").strip()
    # move.executeAlgorithm(solution_algorithm, cube.faces)
    # cube.display()
    # print()
    
if __name__ == "__main__":
    main()