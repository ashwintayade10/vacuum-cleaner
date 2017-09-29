#ASHWIN TAYADE 2015A7PS0058P

from random import randint

def gencoordinates(m, n):
    seen = set()

    x, y = randint(m, n), randint(m, n)

    while True:
        seen.add((x, y))
        yield (x, y)
        x, y = randint(m, n), randint(m, n)
        while (x, y) in seen:
            x, y = randint(m, n), randint(m, n)

def dirt(percent):
	number = percent
	coordinates=[]
	g=gencoordinates(0,9)
	while number>0:
		coordinates.append(g.next())
		number = number-1
	return coordinates

#def main():
#	c = dirt(10)
#	print c

#if __name__=="__main__":
#	main()