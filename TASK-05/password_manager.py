def length(password): #this function is used to check the length of the password
    if len(password) == 8:
        return True #the password is accepted only if it has a length of 8 characters
    else:
        return False
def not_allowed(password): # This function 
    notallowed=[ "A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd","M!n3r4L^", "T7r$eN8f" ]
    if password not in notallowed:
        return True
    else:
        return False
def special(password):
    spe = ["$", "@", "#", "%", "!", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "<", ">", ",", ".", "?", "/", "|", "\\", "~", "`"]
    for i in password:
        if i in spe:
            return True
        
    return False
def num_char(password):
    x=["$", "@", "#", "%", "!", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", ";", ":", "<", ">", ",", ".", "?", "/", "|", "\\", "~", "`"]
    if password[0].isdigit() or password[0] in x:
        return False
    else:
        return True
    
def capital_small(password):
    upper=False
    lower=False
    for i in password:
        if i.isupper():
            upper=True
        if i.islower():
            lower=True
        if upper and lower:
            return True
    else:
        return False

def validity(password):
    # a,b,c,d,e=0,0,0,0,0
    a=length(password)
    b=not_allowed(password)
    c=special(password)
    d=num_char(password)
    e=capital_small(password)

    if a and b and c and d and e:
        print("password is accepted")
    else:
        print("sorry your password is not accepted")
#MAIN PROGRAM
while True:
    password=input("Enter your password: ")
    validity(password)
    x=input("do you want to retry (yes/no): ")
    if x.lower()=="yes":
        pass
    elif x.lower()=="no":
        print("thank you\n")
        break
