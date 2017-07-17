N1=[]
N2=[]
N3=[]
M1 = [1,-2,3,-6,4,2,1,3,-7,-9]
M2 = [1.2,-2.2,3,-6.89,4.24,2.0,1,0.3,-7.0,-9.5]

for i in map(abs, M1):
	
	N1.append(i)
print("List")
print(M1)
print("Is now changed after \"abs\" function into:")
print(N1)
print("\n\n\n")
for i in map(int,M2):
	N2.append(i)
print("List")
print(M2)
print("Is now changed after \"int\" function into:")
print(N2)
print("\n\n\n")
L1 = [1,8,6,3,5,9,7,45,6,21,3]
L2 = [5,6,3,2,7,99,50,66,85,3,12]

for i in map(min,L1,L2):
	N3.append(i)
print("Lists")
print(L1)
print("and")
print(L2)
print("are converted into following list after applying \"min\" function..")
print(N3)
