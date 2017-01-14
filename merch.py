import re

def incr_mer(addi,id):

	f=open('mer.dat','r')

	lis=[]
	for line in f:
		lis=line.split()
		if id==lis[3]:
			lis[2]=str(int(lis[2])+int(addi))
	print lis


	f.close()
	f=open('mer.dat','w')

	for i in lis:
		f.write(i)
		f.write('\t')
	f.close()
	return lis[0]

