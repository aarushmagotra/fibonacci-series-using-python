def main():
    while True :
        print ()
        a = int(input('Enter the terms show Fibonacci numbers upto:'))
        print()
        b, c = 0, 1
        d = 0
        if a <= 0 :
            print('Enter a non negative number greater than zero *Fibonacci numbers are only for positve integers gretaer than 0*')
            print()
        elif a ==1:
            print()
            print('Fibonacci series for' ,a ,'terms is:')
            print()
            print(b)
        else:
            print()
            print('Fibonacci series for' ,a ,'terms is:')
            print()
            while d < a:
                print(b)
                e = b + c
                b = c
                c = e
                print()
                d += 1
        fchoice()
def fchoice():
    print()
    choice = input('Would you like to print another fibonacci series(y/n): ')
    if choice == 'y':
        main()
    elif choice == 'n':
        print()
        print('Bye!!')
        quit()
    else:
        print()
        print('Invalid input!!')
        print()
        print('Try aggain')
        fchoice()
if __name__ == '__main__':
    main()
