largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try :
        x = int(num)
        if x < smallest or smallest is None:
            smallest = x
        if x > largest :
            largest = x
    except :
        print "Invalid input"
    #print num

print "Maximum is", largest
print "Minimum is",smallest