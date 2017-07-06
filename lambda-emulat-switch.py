def play():
    position = (0, 0)
    alive = True

    while position:
        if position == (0, 0):
            print "You are in maze of twisty passages, all alike"
        if position == (1, 0):
            print "You on a road in a dark forest. To the north you can see a tower"
        if position == (1, 1):
            print "There is a tall tower here, with no obvious door. A path leas east."
        else:
            print "There is nothing here"

        command = raw_input()
        i, j = position
        if command == "n":
            position = (i, j + 1)
        elif command == "e":
            position = (i + 1, j)
        elif command == "s":
            position = (i, j - 1)
        elif command == "w":
            position = (i - 1, j)
        elif command == "l":
            pass
        elif command == "q":
            position = None
        else:
            print "I don't understand"

    print "Game over"


from __future__ import print_function


def play_labda():
    position = (0, 0)
    alive = True

    locations = {
        (0, 0): lambda: print("You are in maze of twisty passages, all alike"),
        (1, 0): lambda: print("You on a road in a dark forest. To the north you can see a tower"),
        (1, 1): lambda: print("There is a tall tower here, with no obvious door. A path leas east.")
    }
    try:
        locations[position]()
    except KeyError:
        print("There is nothing here.")

    command = raw_input()

    i, j = position
    if command == "n":
        position = (i, j + 1)
    elif command == "e":
        position = (i + 1, j)
    elif command == "s":
        position = (i, j - 1)
    elif command == "w":
        position = (i - 1, j)
    elif command == "l":
        pass
    elif command == "q":
        position = None
    else:
        print
        "I don't understand"


print
"Game over"

if __name__ == "__main__":
    play()
