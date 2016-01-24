name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"

fh = open(name)
count = 0

map = dict()

for line in fh:
    if line.startswith('From ') and not line.startswith('From:'):
        woorden = line.split()
        tijd = woorden[5]
        uur = tijd.split(':')[0]
 #       print (tijd,uur)
        count = count+1
        map[uur] = map.get(uur,0)+1
        
#print map

lijst = map.items()
lijst.sort()
#print lijst
for uur,aantal in lijst:
    print uur+' '+str(aantal)