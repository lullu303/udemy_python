#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.πͺ

#Write your code below this line π

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

# νμν μ²λ¦¬: ν΄λ‘ κ³Ό μ μ μ΄μ©ν΄μ λΆλμμμ μμ μμμ  2μλ¦¬κΉμ§λ₯Ό νμν¨. κ·Έλ¦¬κ³  νμν¨μλ₯Ό μ¬μ©νλ€
# λ°μ¬λ¦Όμ μ¬μ©νλ λμ  "{:.2f}" νμμ μ¬μ©ν΄μ λ¬Έμμ΄μ λ§λ  λ€μ
# νμν¨μ .format μ bill_per_peopleλ₯Ό μ λ¬νλ©΄ λλ€.
final_amount = "{:.2f}".format(bill_per_people)

print(f"each person should pay: {final_amount}$")
