email=input("Enter your Email= ")
d=0
j=0
k=0
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):     # ^XOR operator (If either is true) if we take or operator than it can be true in every statement
                for i in email:
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1     #d denotes the other sign from -, ., @ like #, <, > 
                if k==1 or j==1 or d==1:
                    print("There should be no space in email address and it should be in lowercase")
            else:
                print("Wrong network companies")
        else:
            print("@ should be comes once")
    else:
        print("First word should be alphabet")
else:
    print("Email address should be greater than 6 words")