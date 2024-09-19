        #QUESTION: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.



def sumofsquares():
    sum=0
    for i in range(1,101):
        sum=sum+(i**2)
    return sum
def squareofsum():
    sum=0
    square=0
    for i in range(1,101):
        sum=sum+i
    square=(sum**2)
    return square
#MAIN PROGRAM
a=sumofsquares()
b=squareofsum()
c=(b-a)
print("the required result is",c)
