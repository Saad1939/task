def Q1(units):
    if units <= 100 :
        print("your bill 0 RS")
    elif 200 >= units > 100 :
        cost= 5*(units-100)
        print(f"your bill is {cost} RS")
    else :
        cost = (10*(units-100))-500
        print(f"your bill is {cost} RS")
# Q1(int(input("entre your units : ")))

# ################################################################

def Q2(percentage) :
    if percentage > 90 :
        print("your grade is A")
    elif percentage > 80 :
        print("your grade is B")
    elif percentage > 60 :
        print("your grade is C")
    else :
        print("your grade is D")
#Q2(int(input("enter your mark : ")))

# ###################################################################

def Q3(num1,num2) :
    larges_num = num2 if num2 > num1 else num1
    print(f"the bigest number is {larges_num}")
#Q3(int(input("enter your first number : ")) ,int(input("enter your second number : ")))

# ###################################################################

def Q4(num):
    number = "Positive" if num > 0 else "Negative"
    print(f"your number is {number}")
# Q4(int(input("enter your number : ")))

# ##########################################################

def Q5(num):
    number = "even" if num%2==0 else "odd"
    print(f"your number is {number}")

# Q5(int(input("enter your number : ")))

# ##########################################################

def Q6 (num1,num2,num3) :
    if num1 > num2 and num1 > num3 :
        print(num1)
    elif  num2> num1 and num2 > num3 :
        print(num2)
    else :
        print(num3)
#Q6(int(input("enter your first number : ")) , int(input("enter your second number : ")) , int(input("enter your third number : ")) )

# #########################################################

def Q7 (working_days,days_absent):
    class_attend= (1-(days_absent/working_days))*100
    print(class_attend)
    if class_attend < 75 :
        print("student will not be able to sit in exam")
# Q7(int(input("total number of working days : ")) , int(input("total number of days absent : "))) 

##########################################################

def Q8 (percentage):
    if percentage > 80 :
        print("your grade is A+")
    elif percentage > 60 :
        print("your grade is A")
    elif percentage > 50 :
        print("your grade is B+")
    elif percentage > 45 :
        print("your grade is B")
    elif percentage > 25 :
        print("your grade is C")
    else :
        print("your grade is D")
# Q8(int(input("enter your mark : ")))

#######################################################################