#QUESTION:Each new term in the Fibonacci sequence is generated by adding the previous two terms.By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
a=0
b=1
sum=0
while True:
    c=a+b
    a=b
    b=c
    if c%2==0:
        sum+=c
    if c>=4000000:
        break
print(sum)