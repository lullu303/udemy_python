# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)

years_remain = 90 - age_as_int
days_remain = years_remain * 365
weeks_remain = years_remain * 52
months_remain = years_remain *12

# print(type(age)) str
# you have x days, y weeks, and z months left
message = (f"you have {days_remain} days, {weeks_remain} weeks, and {months_remain} months left")

print(message)


# score = 0
# height = 1.8
# isWinning = True
# #f-String 
# print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

