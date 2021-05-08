import random


def main():
    i = 0
    while i < 3:
        num1 = random.randint(10, 99)
        num2 = random.randint(10, 99)
        result = int(num1 + num2)
        print("What is " + str(num1) + " + " + str(num2) + "?")
        user_input = int(input("Your answer: "))
        if result == int(user_input):
            i += 1
            print("Correct! You've gotten ", i, " correct in a row.")
        else:
            i = 0
            print("Incorrect. The expected answer is " + str(result))

    print("Congratulations! You mastered addition.")


if __name__ == '__main__':
    main()
