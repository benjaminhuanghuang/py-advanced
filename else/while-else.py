def execute_condition_is_true():
    print "... condition is true"


def execute_condition_is_false():
    print "### condition is false"


i = 10
while i > 0:
    execute_condition_is_true()
    i -= 1
else:
    execute_condition_is_false()


# bad version should be avoided
condition = True

while condition:
    flag = execute_condition_is_true()
    if flag:
        break

if not condition:
    execute_condition_is_false()

#
while condition:
    flag = execute_condition_is_true()
    if flag:
        break   # # bypass while-else clause (skipping execute_condition_is_false())
else:
    execute_condition_is_false()
