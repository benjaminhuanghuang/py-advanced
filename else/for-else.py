def match(item):
    return item == "one"


for item in list:
    if match(item):
        result = item
        break
else:
    # No match found
    result = None
