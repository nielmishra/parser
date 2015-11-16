import matplotlib.pyplot as plt
try:
	#b = open('parsed_0.txt')
	a=[]
	b=[]
	c=[]
	d=[]
	e=[]
	f=[]
	for something in open('parsed_1.txt'):
		column = something.split("	")
		 
		a.append(float(column[1]))
		b.append(float(column[2].split(",")[0]))
		c.append(float(column[3]))
	
	for someotherthing in open('parsed_0.txt'):
		othercolumn = someotherthing.split("	")
		
		d.append(float(othercolumn[2].split(",")[0]))
		e.append(float(othercolumn[3]))
		f.append(float(othercolumn[1]))
		
	
except IndexError, ValueError:
	pass
	

plt.plot(a,(zip(b,c)))
plt.plot(f, (zip(d,e)))
plt.show()


#b = open('parsed_1.txt').read()

#c = b.split("	")
#i =  2
#j = 3
#for something in c:
#	print something [i]
#	i +=2
#	j +=3
