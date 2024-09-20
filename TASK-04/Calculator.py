class Calculator:
    def __init__(self, expression):
        self.expression = expression.replace(" ", "")  #this line is used to remove the spaces in the expressions
        self.result = 0  
        self.num = 0  
        self.sign = "+"  
        self.i = 0  

    def parsing(self): #we use this function to go through each character of the given expression and process it
        while self.i < len(self.expression):
            char = self.expression[self.i]
            if char.isdigit(): #this condition checks if the current character is a number and processes it 
                self.num = self.num * 10 + int(char)
            if char in "+-*/" or self.i == len(self.expression) - 1: #this condition checks if the character is an operator. if it is an operator , another function is used to process them.
                self.operator()  
                self.sign = char
                self.num = 0
            self.i += 1

        return self.result
    def operator(self): #this function is used to process the operators and return the obtained result to be printed in the main program
        if self.sign == "+":
            self.result += self.num
        elif self.sign == "-":
            self.result -= self.num
        elif self.sign == "*":
            self.result *= self.num
        elif self.sign == "/":
            
            if self.num == 0:
                raise ValueError("Oops, looks like you tried to divide by zero! That's not allowed.")
            self.result //= self.num

# MAIN Program
while True:
    print("Welcome to the calculator")
    print("The expression can contain the following things only:")
    print("Integers\noperators (+,-,*,/)") 
    expression = input(" enter your expression: ")
    calc = Calculator(expression)
    try:
        result = calc.parsing()
        print(f"Entered expression: {expression}")
        print(f"Result: {result}")
    except ValueError as e:
        print(f"error: {e}")
    ch=input("Do you want to continue? (yes/no)")
    if ch.lower()=="yes":
        pass
    elif ch.lower()=="no":
        break
