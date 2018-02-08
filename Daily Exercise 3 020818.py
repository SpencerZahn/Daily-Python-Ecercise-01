#Spencer Zahn - Python Daily Exercise 3 - 020818

#3 Write a program that prints out the numbers from 1 to 20. 
# For multiples of three, print "usb" instead of the number and for the mulitiples of five, print "device". 
# For numbers which are multiples of both three and five, print "usb device".
# Print a new line after each string or number.
for num in range(21):
        if num == 0:
                print("")
        elif num == 3:
                print ("usb")
        elif num == 5:
                print ("device")
        elif num == 6:
                print ("usb")
        elif num == 9:
        	print ("usb")
        elif num == 10:
        	print ("device")
        elif num == 12:
        	print ("usb")
        elif num == 15:
        	print ("usb device")
        elif num == 18:
        	print ("usb")
        elif num == 20:
        	print ("device")
        else:
        	print(num)                
