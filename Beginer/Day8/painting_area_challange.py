from math import ceil


def paint_area(h, w, c):
    cans = ceil((h * w) / c)
    print(f"You'll need {cans} of paint.")


height = int(input("Height of wall: "))
width = int(input("Width of wall: "))
coverage = 5


paint_area(height, width, coverage)

