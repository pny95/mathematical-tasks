n = int(input("How many Fibonacci numbers would you like? Please type a number and Fibonacci numbers will be printed."))
n1 = 0
n2 = 1
if n <=0:
    print("Please type a positive and bigger than 0 number")
else:
    print(n1, end=" ")
    for x in range(n):
        print(n2, end=" ")
        nextNumber = n1 + n2
        n1 = n2
        n2 = nextNumber



