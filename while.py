while True:
    age = input('>>>: ')
    try:
        age = int(age)
        if age >= 18:
            print("acess allowed")
            break
        else:
            print("access denied")
            break
    except ValueError:
        print(f'{age} is not a number. Please enter the number')
