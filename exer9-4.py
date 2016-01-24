fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

map = dict()

for line in fh:
    if line.startswith('From') and not line.startswith('From:'):
        woorden = line.split()
#        print woorden[1]
        count = count+1
        if woorden[1] in map:
            map[woorden[1]]=map[woorden[1]]+1
        else:
            map[woorden[1]]=1
        
#print "There were", count, "lines in the file with From as the first word"
#print map

maxi = 0
maxinaam = 'niet gevonden...'
for naam in map:
    if map[naam] > maxi:
        maxi = map[naam]
        maxinaam = naam
        
print maxinaam+' '+str(maxi)
    