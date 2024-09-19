#Question: Find the sum of all the primes below two million.
sum=0
for i in range(2,2000000):
    for j in range(2,i):
        if(i%j==0):
            pass
    else:
        sum=sum+i
print(sum)