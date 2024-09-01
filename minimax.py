"""
structure:
    choices: (bundle of these two)
        moving position
        move at position
        each turn consists of these two choices, but each moving position may have multiple moves at position
    scoring of choices:
        1) we dont want to lose - ie. there should be available moves left after move action
        2) maybe choose the path that leads to the most available moves?
        3) two game outcomes - either win or lose (1 left, or more than one left)
            3a) can choose to display as multiple game outcomes (1 left, 2 left, 3 left, aiming for lower values)

"""
