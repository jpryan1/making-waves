from __future__ import print_function
import numpy as np
MESHSIZE=64
DELTAX = 1
DELTAT = 0.2
V = 1
ALPHA =( V*DELTAT)/DELTAX
prefix = """ply
format ascii 1.0
element vertex """+str(MESHSIZE*MESHSIZE)+"""
property float x
property float y
property float z
element face """+str((MESHSIZE-1)*(MESHSIZE-1))+"""
property list uchar int vertex_index
end_header\n"""

first = np.empty([MESHSIZE,MESHSIZE])
second = np.empty([MESHSIZE,MESHSIZE])
third = np.empty([MESHSIZE,MESHSIZE])
def mesh_print(mymesh, myfile):
	global prefix
	myfile.write(prefix)
	for i in range(MESHSIZE):
		for j in range(MESHSIZE):
			myfile.write(str(i-(MESHSIZE/2.0))+ " "+str(j-(MESHSIZE/2.0))+" "+str(mymesh[i][j])+"\n")
	for i in range(MESHSIZE-1):
		for j in range(MESHSIZE-1):
			myfile.write("4 "+str(i+j*MESHSIZE)+ " "+ str(i+j*MESHSIZE+1)+ " "+str(i+1+(j+1)*MESHSIZE)+ " "+ str(i+(j+1)*MESHSIZE)+"\n")


def initialize(mesh):
	bound = int(MESHSIZE/5.0)
	for i in range(MESHSIZE):
		for j in range(MESHSIZE):
			mesh[i][j] = np.exp(-(pow(i-(MESHSIZE/4.0),2)/20.0)-(pow(j-(MESHSIZE/2.0),2)/20.0))*15

		#	if(i>bound and i<4*bound and j>bound and j<4*bound):
		#		mesh[i][j] = 5
		#	else:
		#		mesh[i][j] = 0
initialize(first)
initialize(second)
def step(first, second, third):
	for i in range(MESHSIZE):
		for j in range(MESHSIZE):
			if(i==0 or i==(MESHSIZE-1) or j==0 or j==(MESHSIZE-1)):
				continue
			else:
				third[i][j] = pow(ALPHA,2)*(second[(i+1)%MESHSIZE][j]
				+second[(i-1)%MESHSIZE][j]
				+second[i][(j+1)%MESHSIZE]
				+second[i][(j-1)%MESHSIZE]
				) + 2*second[i][j]*(
				1-2*pow(ALPHA,2)) - first[i][j]
	for i in range(1,63):
		third[i][0] = third[i][1]
		third[i][MESHSIZE-1] = third[i][MESHSIZE-2]
		third[0][i] = third[1][i]
		third[MESHSIZE-1][i] = third[MESHSIZE-2][i]
	third[0][0] = third[1][1]
	third[MESHSIZE-1][MESHSIZE-1] = third[MESHSIZE-2][MESHSIZE-2]
	third[0][MESHSIZE-1] = third[1][MESHSIZE-2]
	third[MESHSIZE-1][0] = third[MESHSIZE-2][1]

for time in range(2048):
	

	step(first,second,third)
	out = open(str(time)+".ply", "w")
	mesh_print(third, out)
	out.close()
	first = np.copy(second)
	second = np.copy(third)


