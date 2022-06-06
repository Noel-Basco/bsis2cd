# Math_Tutor_v2.0

# Partners:
# Noel Francis Marie F. Basco (Owner)
# Thea Jazmine G. Dizon (Collaborator)

import random

def add(x, y):
    return x + y

def subtrct(x, y):
    return x - y

def multiply(x, y):
    return x * y

def dividiby(x, y):
    return x / y

count = 0
correct = 0

while True:
    choice = input("Enter your choice (1 - Add, 2 - Sub, 3 - mult, 4 - divi): ")
    if choice in ('1', '2', '3', '4'):

        prob_count = int(input("How many problems?: "))
        print("")
        while count < prob_count:
            if choice == '1':
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = add(num1, num2)
                print("What is the sum of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    print("")
                    correct+=1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("")
                count+=1
            
            elif choice == '2':
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = subtrct(num1, num2)
                print("What is the difference of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    print("")
                    correct+=1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("")
                count+=1
            
            elif choice == '3':
                num1 = float(random.randint(0, 9))
                num2 = float(random.randrange(2, 10, 2))
                num3 = multiply(num1, num2)
                print("What is the product of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    print("")
                    correct+=1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("")
                count+=1
            
            elif choice == '4':
                num1 = round(float(random.randint(0, 9)), 2)
                num2 = round(float(random.randrange(2, 10, 2)),2)
                num3 = dividiby(num1, num2)
                print("What is the quotient of " + str(num1) + " and " + str(num2))
                answer = float(input("Enter your answer: "))
                if num3 == answer:
                    print("Correct")
                    print("")
                    correct+=1
                else:
                    print("Wrong! the correct answer is", num3)
                    print("")
                count+=1
    
    print("Score:", correct)
    try_again = input("Want to try again? (yes/no): ")
    if try_again == "no":
        break
else:
    print("Invalid Input")