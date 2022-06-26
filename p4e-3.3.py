score = input("Enter Score: ")
sc =  float(score)
i = 'Error'
if sc >= 0.9:
	i = 'A'
elif sc >=0.8:
	i ='B'
elif sc >=0.7:
	i ='C'
elif sc >= 0.6:
	i ='D'
elif sc < .6:
	i ='F'
else:
	i ="Out of Range"
print (i)
