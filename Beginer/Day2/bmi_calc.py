import math
heith = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

bmi = float(weight / math.pow(heith, 2))

print(f"you bmi is: {bmi:.1f}")

#
# result = 4 / 2
# print(result)
# #this means (result = result / 2)
# result /= 2
# print(result)
#
# scores = 0
# scores += 1
# print(scores)