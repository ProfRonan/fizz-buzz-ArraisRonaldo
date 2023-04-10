abc = int(input("Digite um número: "))

if abc % 3 == 0 and abc % 5 == 0:
    print("FizzBuzz")
else:
        if abc % 3 == 0:
         print("Fizz")
        else:
           if abc % 5 == 0:
            print("Buzz")
           else:
            print(abc)