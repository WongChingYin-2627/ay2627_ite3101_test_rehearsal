def main():
    while True:
        try:
            num = int(input("Type an integer:"))
            break
        except ValueError:
            print('Please enter an integer.')
if __name__ == "__main__":
    # execute only if run as a script
    main()
