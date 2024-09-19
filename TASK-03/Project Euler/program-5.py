#QUESTION: There exists exactly one Pythagorean triplet for which a+b+c=1000. Find the product abc.
a,b,c=0,0,0
for a in range(1,1001):
    for b in range(a,1001-a):
        c=1000-a-b 
        if  (a**2)+(b**2)==(c**2):
            print(a*b*c)
            break
    else:
        continue
   
