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

# 형식화 처리: 클론과 점을 이용해서 부동소수점에서 소수점 2자리까지를 표시함. 그리고 형식함수를 사용한다
# 반올림을 사용하는 대신 "{:.2f}" 형식을 사용해서 문자열을 만든 뒤에
# 형식함수 .format 에 bill_per_people를 전달하면 된다.
final_amount = "{:.2f}".format(bill_per_people)

print(f"each person should pay: {final_amount}$")
