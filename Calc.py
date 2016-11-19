def add(num1, num2):
	return(num1 + num2)
def sub(num1, num2):
	return(num1 - num2)
def mul(num1, num2):
	return(num1 * num2)
def div(num1, num2):
	return(num1 / num2)

def Main():
        try:
                a = int(input("Type first number: "))
                b = int(input("Type second number: "))
                c = input("Type +, -, *, or /: ")
                if c == "+":
                        print(add(a, b))
                elif c == "-":
                        print(sub(a, b))
                elif c == "*":
                        print(mul(a, b))
                elif c == "/":
                        print(div(a, b))
                else:
                        print("Error: please type a valid opperation")
        except:
                print("Error: please type a vaild intager")
        print()
		
while True:
        Main()