# Use the file name mbox-short.txt as the file name
def pulk_getal(text):
    semi = text.find(":")
    getal = float((text[semi+1:len(text)]).strip())
    return getal


fname = raw_input("Enter file name: ")
fh = open(fname)
som = 0.0
aantal = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
#    print line
    getal = pulk_getal(line)
#    print getal
    som = som + getal
    aantal = aantal + 1
# print "Done"
# print (som,aantal)
print "Average spam confidence: "+str(som/aantal)
