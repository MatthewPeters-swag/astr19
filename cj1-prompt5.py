import math

def main():
	dx = 2/999
	
	for i in range(1000):

		x = i * dx
		print(f"{x:.6f}\t{math.sin(x):.6f}")

if __name__=="__main__":
	main()