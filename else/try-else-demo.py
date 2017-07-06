try:
    f = open("test.txt", 'r')
except IOError:
    print "File could not be opend"
else:
    print "Number of lines ", sum(1 for line in f)
    f.close()
