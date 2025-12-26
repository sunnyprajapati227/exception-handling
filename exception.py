try:
    n=int(input("Enter n:"))
    if n<0:
    	raise ValueError("-ve value not allowed")
    else:
    	fact=1   
    for i in range (1,n+1):
        fact=fact*i
        print("factorial of {}={}".format(n,fact))

except  ValueError as e:
	print(e)
except:
	print("Something went wrong")
	




