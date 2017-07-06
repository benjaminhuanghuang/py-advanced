def do_something():
    print "do something"


def handle_value_error():
    print "handle_value_error"


def do_something_else():
    print "do_something_else"


def always_do_something():
    print "always_do_something"


try:
    do_something()
except ValueError:
    handle_value_error()
else:
    # No exception was raised
    # We know that do_something() succeeded
    do_something_else()
finally:
    always_do_something()

# out put
#    do something
#    do_something_else
#    always_do_something