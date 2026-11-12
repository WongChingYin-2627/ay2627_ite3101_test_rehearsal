def main():
    while True:
        try:
            num = int(input("Type an integer:"))
            break
        except ValueError:
            print('Please enter an integer.')

    if num % 10 == 0 and num % 3 != 0:
        print(f'{num} is divisible by 10 and hot
if __name__ == "__main__":
    # execute only if run as a script
    main()
