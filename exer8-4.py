fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
#    print line.rstrip()
    woorden = line.rstrip().split()
    for woord in woorden:
#        print woord
        if not woord in lst:
            lst.append(woord)
lst.sort()
print lst