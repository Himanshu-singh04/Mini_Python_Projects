import random
import operator

for i in range (10):
    random_num1 = random.randint(1,99)
    random_num2 = random.randint(1,99)

    operators = {'+':operator.add,      #'*':operator.mul,'/':operator.truediv
             '-':operator.sub,}

    random_operators = random.choice(list(operators.keys()))
    value = operators.get(random_operators)(random_num1,random_num2)

# for i in range (10):
    print (f"Evaluate {random_num1} {random_operators} {random_num2} ?")
    answer = int(input("enter your answer"))


    score = 0

    if (answer == value):
        print ("your answer is correct")
        # score += 1
    else :
        print("wrong answer")
        

# print (f"you got{score} out of 5")

