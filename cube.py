import numpy as np

class Cube: 
    def __init__(self):
        self.faces = {
            "up": np.array([
                ["w", "w", "w"],
                ["w", "w", "w"],
                ["w", "w", "w"],
            ]),
            "left": np.array([
                ["o", "o", "o"],
                ["o", "o", "o"],
                ["o", "o", "o"],
            ]),
            "front": np.array([
                ["g", "g", "g"],
                ["g", "g", "g"],
                ["g", "g", "g"],
            ]),
            # "right": np.array([
            #     ["0", "1", "2"],
            #     ["3", "4", "5"],
            #     ["6", "7", "8"],
            # ]),
            "right": np.array([
                ["r", "r", "r"],
                ["r", "r", "r"],
                ["r", "r", "r"],
            ]),
            "back": np.array([
                ["b", "b", "b"],
                ["b", "b", "b"],
                ["b", "b", "b"],
            ]),
            "down": np.array([
                ["y", "y", "y"],
                ["y", "y", "y"],
                ["y", "y", "y"],
            ]),
        }

    def display(self):
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
        up, down = self.faces["up"], self.faces["down"]
        left, right = self.faces["left"], self.faces["right"]
        front, back = self.faces["front"], self.faces["back"]
        formatted_cube = (
            f"\t{" "*7} - - - - -\n"
            f"\t{" "*7} | {" ".join(up[0])} |\n"
            f"\t{" "*7} | {" ".join(up[1])} |\n"
            f"\t{" "*7} | {" ".join(up[2])} |\n"
            "\t- - - - - - - - - - - - - - - - -\n"
            f"\t| {" ".join(left[0])} | {" ".join(front[0])} | {" ".join(right[0])} | {" ".join(back[0])} |\n"
            f"\t| {" ".join(left[1])} | {" ".join(front[1])} | {" ".join(right[1])} | {" ".join(back[1])} |\n"
            f"\t| {" ".join(left[2])} | {" ".join(front[2])} | {" ".join(right[2])} | {" ".join(back[2])} |\n"
            "\t- - - - - - - - - - - - - - - - -\n"
            f"\t{" "*7} | {" ".join(down[0])} |\n"
            f"\t{" "*7} | {" ".join(down[1])} |\n"
            f"\t{" "*7} | {" ".join(down[2])} |\n"
            f"\t{" "*7} - - - - -"
        )
        print(formatted_cube)

