# import library
import math, random
#input takes number of digits in OTP
nd=int(input("Enter number of digits in OTP :"))
# function to generate OTP
def generateOTP(n) :

	# Declare a digits variable
	digits = "0123456789"
	OTP = ""

# length of password can be chaged

	for i in range(n) :
		OTP += digits[int(random.random() * 10)]

	return OTP

	
print("OTP of ",nd, "digits:", generateOTP(nd))

