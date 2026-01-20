def Prod(x, y):
	prod = x * y
	Print(prod)

def Dif(x, y):
	dif = x - y
	Print(dif)

def Sum(x, y):
	sum = x + y 
	Print(sum)

def Print(x):
	print(x)
	print("Type:", type(x))

def main():
	a = 3.5
	b = 2.1
	c = 1
	d = 2

	Sum(a,b)
	Dif(c,d)
	Prod(b, d)

if __name__=="__main__":
	main()