print("Welcome to my computer quiz"  )

playing = input("do you wanna play? ")

if playing.lower()  != "yes":
    quit()
    
print("Okay! let's play: ")

score = 0


answer = input("What does cpu stands for? ")
if answer.lower() =="central processing unit":
    print("correct!!")
    score += 1
    
else:
    print("Incorrect!..")


answer = input("What does gpu stands for? ")
if answer.lower() =="graphics processing unit":
    print("correct!!")
    score += 1
    
else:
    print("Incorrect!..")


answer = input("What does ram stands for? ")
if answer.lower() ==" random access memory":
    print("correct!!")
    score += 1
    
else:
    print("Incorrect!..")
    
answer = input("What does rom stands for? ")
if answer.lower() =="read only memory":
    print("correct!!")
    score += 1
    
else:
    print("Incorrect!..")
    
answer = input(" What does PSU stands for? ")
if answer.lower() ==" power supply unit":
    print("correct!!")
    score += 1
    
else:
    print("Incorrect!..")


print("You got " + str(score) + " questions correct")
print("You got " + str((score / 5) * 100) + "%.")
          
