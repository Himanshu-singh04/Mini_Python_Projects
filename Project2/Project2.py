import random
randomNumber = random.randint(1,100)

user = None
guesses = 0

while (user!=randomNumber):
    user = int(input("enter your guess\n"))
    guesses += 1
    if(user==randomNumber):
        print ("you guessed it right!!!")
    else:
        print ("you guessed it wrong")
        if (user > randomNumber):
            print ("you surpassed the number")
        elif (user < randomNumber ):
            print ("your number is less than guess ")
        

print (f"you took {guesses} chances to guess")


with open("C:\CODES\Python codes\project\hiscore_p2.txt","r") as a:
    hiscore = int(a.read())

if (guesses<hiscore):
    with open ("C:\CODES\Python codes\project\hiscore_p2.txt","w") as p:
        p.write(str(guesses))
    print ("you just broke the hiscore")

else:
    print (f"the hiscore is {hiscore}")





