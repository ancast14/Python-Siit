a = 0

while True:
    try:
        age = int(input("Age: "))

    except ValueError:

        if ValueError:
            a += 1

        if a > 2:
            print("Out of tries!")
            break
        else:
            print("Invalid value. Try again.")
            continue

    if age >= 18:
        print("You are a grown up!")
    else:
        print("You are a child!")

    break