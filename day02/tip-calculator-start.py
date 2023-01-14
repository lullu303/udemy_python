#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("welcom to the tip calculator!")

bill = input("what was the total bill? $")
bill_to_float = float(bill)

tip = float(
    input("what percentage tip would you like to give? 10, 12, or 15? "))

# should_pay = round((bill_to_float / people_to_int) + (tip / 100 * bill_to_float), 2)
bill_with_tip = tip / 100 * bill_to_float + bill_to_float

people = input("how many people to split the bill? ")
people_to_int = int(people)

bill_per_people = bill_with_tip / people_to_int

final_amount = round(bill_per_people, 2)
print(f"each person should pay: {final_amount}$")
