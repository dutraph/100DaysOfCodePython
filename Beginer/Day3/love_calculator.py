def love_calc():
    name1 = input("enter 1st name: ").lower()
    name2 = input("enter 2nd name: ").lower()
    concat_name = name1 + name2
    t = concat_name.count("t")
    r = concat_name.count("r")
    u = concat_name.count("u")
    e = concat_name.count("e")
    true = t + r + u + e
    l = concat_name.count("l")
    o = concat_name.count("o")
    v = concat_name.count("v")
    ee = concat_name.count("e")
    love = l + o + v + ee

    love_score = int(str(true) + str(love))

    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, you go together like coke and mentos.")
    elif 40 <= love_score <= 50:
        print(f"Your score is {love_score}, you're alright together")
    else:
        print(f"Your score is {love_score}.")

    tries = input("Do you wanna try again? [y/n]: ")
    while True:
        if tries == "y":
            love_calc()
        else:
            break


love_calc()
