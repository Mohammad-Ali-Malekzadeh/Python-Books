select_ex = "n_" + input("Please Select one of the Exercises (1 - 7, not be 4): ")

def ex1():
    print("Welcome to First Exercise.")
    num1 = int(input("Please Enter First Num: "))
    num2 = int(input("Please Enter Second Num: "))
    num3 = int(input("Please Enter Third Num: "))
    print("Total entries:", num1 + num2 + num3)

def ex2():
    print("Welcome to Sexond Exercise.")
    num1 = int(input("Please Enter First Num: "))
    num2 = int(input("Please Enter Second Num: "))
    print("Average entries:", (num1 + num2) / 2)

def ex3():
    print("Welcome to Third Exercise.")
    num = float(input("Please Enter Num: "))
    result = round(num) % 3
    print("Output:", result)

def ex5():
    print("Welcome to Fourth Exercise.")
    a = int(input("Please Enter a Num: "))
    b = int(input("Please Enter b Num: "))
    c = b > 3
    print("Output:", c and a < 2)

def ex6():
    print('result of 7^10:', 7^10)
    print('result of 8&9:', 8&9)
    print('result of 66|2:', 66|2)
    print('result of 17>>2', 17>>2)

def ex7():
    print(7)

def ex8():
    print(8)

exercises = {
    "n_1": ex1,
    "n_2": ex2,
    "n_3": ex3,
    "n_5": ex5,
    "n_6": ex6,
    "n_7": ex7,
    "n_8": ex8,
}

if not (select_ex in exercises):
    print("Please Enter a Valid input!!!")
    quit()
else:
    exercises[select_ex]()