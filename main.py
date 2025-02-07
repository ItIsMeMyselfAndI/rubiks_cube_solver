import cube, movement, scramble, edges, corners

import os, sys, time


def getScrambleAlgorithm(available_moves):
    choice = _getUserChoice()
    if choice == "Y":
        scramble_algorithm = _getUserScramble(available_moves)
    else:
        new_scramble = scramble.Scramble()
        new_scramble.generateAlgorithm()
        scramble_algorithm = " ".join(new_scramble.algorithm)
    return scramble_algorithm


def _getUserChoice():
    lines = (
        f"\n[Scramble]\n\n"
        f"\tY - Create own scramble\n"
        f"\tN - Generate random scramble\n"
    )
    while True:
        os.system("cls")
        print(lines)
        choice = input("Enter valid option (Y/N)? ").upper()
        if choice in ["Y", "N"]:
            print("\nplease wait ...\n")
            time.sleep(2)
            return choice


def _getUserScramble(moves):
    lines = ["[Available Moves]\n\n"]
    length = len(moves)
    for i in range(0, length, 4):
        lines.append(f"\t- {moves[i]} or {moves[i+1]} or {moves[i+2]} or {moves[i+3]}\n")
    lines = "".join(lines)
    while True:
        os.system("cls")
        print(lines)
        print("Enter valid scramble algorithm (separate with spaces):")
        scramble_algorithm = input("\t- ")
        for move in scramble_algorithm.split():
            if move in moves:
                print("\nplease wait ...\n")
                time.sleep(2)
                return scramble_algorithm.strip()


def getEdgesInspectionInfo(my_cube):
    my_edges = edges.Edges(my_cube.faces, ["uk", "ku"], 22)
    my_edges.inspect("uk", enable_parity=True)
    edges_sequence = my_edges.getLettersSequence()
    edge_solution = my_edges.getSolution(edges_sequence)
    edge_solution_display = my_edges.formatSolutionDisplay("Edges:", edge_solution)
    edge_move_count = my_edges.getMoveCount(edge_solution)
    parity = my_edges.is_parity 
    info = [
        edges_sequence, edge_solution,
        edge_solution_display, edge_move_count, parity
    ]
    return info


def getCornersInspectionInfo(my_cube):
    my_corners = corners.Corners(my_cube.faces, ["aer", "era", "rae"], 21)
    my_corners.inspect("era", enable_parity=False)
    corners_sequence = my_corners.getLettersSequence()
    corner_solution = my_corners.getSolution(corners_sequence)
    corner_solution_display = my_corners.formatSolutionDisplay("Corners:", corner_solution)
    corner_move_count = my_corners.getMoveCount(corner_solution)
    info = [
        corners_sequence, corner_solution, 
        corner_solution_display, corner_move_count

    ]
    return info


def getUserMenuChoice():
    lines = (
        f"[Menu]\n\n"
        f"\t1 - Display scrambled cube\n"
        f"\t2 - Display solved cube\n"
        f"\t3 - Display solution sequence\n"
        f"\t4 - Display solution algorithm\n"
        f"\t5 - Display solution move count\n"
        f"\t6 - Create new scramble\n"
        f"\t7 - Exit\n"
    )
    print(lines)
    while True:
        os.system("cls")
        print(lines)
        choice = input("Enter valid option (1-7): ")
        if choice in [str(x) for x in range(1, 8)]:
            print("\nplease wait ...\n")
            time.sleep(2)
            return int(choice)


def displayScrambledState(scrambled_cube_display, scramble_algorithm):
    print("\n[Scrambled State]\n")
    print(scrambled_cube_display)
    print(f"\n\t{"Scramble:":<10} {scramble_algorithm}\n")


def displaySolvedState(solved_cube_display):
    print("[Solved State]\n")
    print(solved_cube_display)


def displaySolutionSequence(edges_info, corners_info):
    print("\n[Solution Sequence]\n")
    print(f"\t{"Edges:":<10} {" ".join(edges_info[0])}")
    print(f"\t{"Parity:":<10} {edges_info[4]}")
    print(f"\t{"Corners:":<10} {" ".join(corners_info[0])}\n")


def displaySolutionAlgorithm(edges_info, corners_info):
    print("[Solution Algorithms]\n")
    print(edges_info[2])
    print(corners_info[2])


def displayMoveCount(edges_info, corners_info):
    print("[Move Count]\n")
    print(f"\t{"Edges:":<10} {edges_info[3]}")
    print(f"\t{"Corners:":<10} {corners_info[3]}")
    print(f"\t{"Total:":<10} {edges_info[3] + corners_info[3]}\n")


def main():
    available_moves = [
        "U", "U'", "U2", "U2'",
        "L", "L'", "L2", "L2'",
        "F", "F'", "F2", "F2'",
        "R", "R'", "R2", "R2'",
        "B", "B'", "B2", "B2'",
        "D", "D'", "D2", "D2'",
    ]

    # create new cube
    my_cube = cube.Cube()
    move = movement.Move()
    # generate scramble
    scramble_algorithm = getScrambleAlgorithm(available_moves)
    # execute scramble
    move.executeAlgorithm(scramble_algorithm, my_cube.faces)
    scrambled_cube_display = my_cube.formatDisplay()
    # inspect edges and corners
    edges_info = getEdgesInspectionInfo(my_cube)
    corners_info = getCornersInspectionInfo(my_cube)
    # execute solutions
    move.executeAlgorithm(" ".join(edges_info[1]), my_cube.faces)
    move.executeAlgorithm(" ".join(corners_info[1]), my_cube.faces)
    solved_cube_display = my_cube.formatDisplay()

    while True:
        choice = getUserMenuChoice()
        os.system("cls")
        if choice == 1:
            displayScrambledState(scrambled_cube_display, scramble_algorithm),
        elif choice == 2:
            displaySolvedState(solved_cube_display),
        elif choice == 3:
            displaySolutionSequence(edges_info, corners_info),
        elif choice == 4:
            displaySolutionAlgorithm(edges_info, corners_info),
        elif choice == 5:
            displayMoveCount(edges_info, corners_info),
        elif choice == 6:
            main()
        elif choice == 7:
            sys.exit()
        input("\n...enter anything to go back to [Menu]\n")


if __name__ == "__main__":
    main()