mealCost= float(input())
tip = int(input())
tax= int(input())


tipAmount=mealCost*tip/100
taxAmount=mealCost*tax/100
totalCost= int(round(mealCost+tipAmount+taxAmount))
print("The total meal cost is "+str(totalCost)+ " dollars.")