#QUESTION: If we list all the natural numbers below that are multiples of 3 or 5 , we get 3,5,6,9 .Find the sum of all the multiples of 3 or 5 below 1000.
sum=0
for i in range(1000):
    if i%3==0 or i%5==0:
        sum+=i
    else:
        pass
print("The sum of the multiples of 3 and 5 below 1000 is ",sum)
