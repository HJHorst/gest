def computepay(hrs,rate):
    if hrs > 40:
      pay = (hrs-40)*rate*1.5 + 40*rate
    else:
      pay = hrs*rate
    return pay
    
hrs = int(raw_input('Enter hours: '))
rate = int(raw_input('Enter Rate: '))
print ("Pay: "+str(computepay(hrs,rate)))  
