def is_comment(item):
    return isinstance(item, str) and item.startswith("#")


def execute(program):
    # skipping the comment
    while program:
        item = program.pop()
        if not is_comment(item):
            program.append(item)
            break  # bypass while-else
    else:  # no break
        print "Empty program"
        return

    pending = []
    while program:
        item = program.pop()
        if callable(item):
            try:
                result = item(*pending)
            except Exception as e:
                print "Error: ", e
                break  # bypass while-else
            program.append(result)
            pending = []
        else:
            pending.append(item)
    else:
        print "Program successful."
        print "Result", pending


if __name__ == "__main__":
    import operator

    program = list(reversed((
        "# A short stack program to add",
        "# add multiply some constants",
        5,
        2,
        operator.add,
        3,
        operator.mul)))

    execute(program)
