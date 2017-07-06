#
# For-else Clauses and Handling Search Failure
#
# items = [2, 36, 25, 9]
items = [2, 25, 9]
divisor = 12

for item in items:
    if item % divisor == 0:
        found = item
        break
else:  # nobreak
    items.append(divisor)
    found = divisor

print "{items} constains {found} which is a multiple of {divisor}".format(**locals())
