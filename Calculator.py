#calculator

print("Welcome to Calculator. Just input the two numbers and choose the required basic operation to perform on them.\n\n")

num_1 = float(input("Enter Number 1: "))
num_2 = float(input("Enter Number 2: "))

def add():
    res = num_1 + num_2
    print(num_1," + ",num_2," = ",res)

def subt():
    res = num_1 - num_2
    print(num_1," - ",num_2," = ",res)

def mult():
    res = num_1*num_2
    print(num_1," * ",num_2," = ",res)

def div():
    if num_2 == 0:
        print("Can't Divide by Zero")
    else:
        res = num_1/num_2
        res_o = round(res,3)
        print(num_1," / ",num_2," = ",res_o)

while True:
    chc = int(input("\nSelect the operation to be performed. Enter: \n1 for Addition\n2 for Subtraction\n3 for Product\n4 for Division\n"))

    if chc in range(1,5):
        if chc == 1:
            print("\nOperation Chosen = Addition")
            add()
        elif chc == 2:
            print("\nOperation Chosen = Subtraction")
            subt()
        elif chc == 3:
            print("\nOperation Chosen = Product")
            mult()
        elif chc == 4:
            print("\nOperation Chosen = Division")
            div()

        break
    else:
        print("Enter a Valid Choice.")
