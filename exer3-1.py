hrs = int(raw_input('Enter hours: '))
rate = float(raw_input('Enter Rate: '))
if hrs > 40:
  pay = (hrs-40)*rate*1.5 + 40*rate
else:
  pay = hrs*rate
print ("Pay: "+str(pay))  
