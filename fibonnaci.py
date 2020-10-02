while True :

    a = int(input('Enter the terms show Fibonacci numbers upto:'))
    print()
    b, c = 0, 1
    d = 0
    if a <= 0 :
        print('Enter a non negative number greater than zero *Fibonacci numbers are only for positve integers gretaer than 0*')
        print()
    elif a ==1 :
        print('Fibonacci series for' ,a ,'terms is:')
        print(b)
    else:
        print('Fibonacci series for' ,a ,'terms is:')
        print()
        while d < a:
            
            
            print(b)
            e = b + c
            b = c
            c = e
            print()
            d += 1
