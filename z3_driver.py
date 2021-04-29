from z3 import *

def main():

	x = Int("x")
	y = Int("y")
	a1 = Int("a1")
	a2 = Int("a2")
	a3 = Int("a3")
	a4 = Int("a4")
	a5 = Int("a5")
	a6 = Int("a6")
	e1 = -50 * a1 + y * a2 + a3 == -l
	e2 = -50 * a4 + y * a5 + a6
	e = [e1, e2]
	l1 = Int("l1")
	l2 = Int("l2")
	l = Int("l")
	lambdas = [l1, l2]
	for i in range(len(e)):
		e[i] = -e[i] - 1
	b = Bool( == -l)
	#Exists(lambdas, ForAll([x,y], Bool(l1 * e1 + l2 * e2 == -l)))
	print(b)


if __name__ == "__main__":
    main()