age = int(input("What's your age: "))
age = 90 - age

days, weeks, months = age * 365, age * 52, age * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")