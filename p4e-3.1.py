hrs = input("Enter Hours:")
h = float(hrs)
i = input("Enter the Rate:")
x = float(i)
if h <= 40:
 	print( h  * x)
elif h > 40:
	print(40* x + (h-40)*1.5*x)
