#Largest prime factor
#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143?




#Steps to solving
#1: Calcualte prime number, 1 and itself
#1a:  Modules, if it is divisable by 2,3,5
#2: Find the largest prime



#variables
largestPrime=5
maxNumb= 30

i=5

#first loop to check for the largest prime
while (i <=maxNumb):
    if (i%2>0):
        if(i%3>0):
            if(i%5>0 or i==5):
                if(i%7>0 or i==7):
                    if(i%11>0 or i==11):
                        if(i >=largestPrime):
                            largestPrime=i
                            print(largestPrime)

#REFRACTORING: once you find the prime, that needs to be the divisor
#for the modulus, by appending to array


#array


    i=i+1
        #second loop to check if it is prime
    #FIRST TRY
    #y=2
    #while (y<=5):
       # if(i%y!=0 and y!=2):
            #if(i/i==0):
                #largestPrime=y
        #elif(i%y==0 and (y==1 or y==2 or y==5)):
           #largestPrime=y
    #end of whileloop2
    #SECOND TRY
    #if(i%2!=0 and i!=2):
       # if(i%3!=0 and i!=3):
           # if(i%5!=0 and i!=5):
               # if(i%1==0 and i%i==0):
                    #largestPrime=i
                #else:
                    #largestPrime=5
            #else:
                #largestPrime=3
        #else:
            #largestPrime=2
    #else:
        #largestPrime=1
    #print (largestPrime)