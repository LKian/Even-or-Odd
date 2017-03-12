def evenorodd(x):
	if x%2==0:
		print "Your number is an even number.  It's divisible by 2."
	else:
		print "That's an odd number."
xyz = input("Enter a number to determine if it is even or odd: ")
print evenorodd(xyz)