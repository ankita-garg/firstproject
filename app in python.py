import random
count=1
i=random.randrange(1,20)
##print(i)
while(count):
    j=int(input("Enter a no that u want to guess"))
    if(i!=j):
        count+=1
        diff=j-i
        if(diff<0):
            print("Your no is too low")
        else:
            print("Your no is too high")
    else:
        print("Your guess is true")
        break
         
