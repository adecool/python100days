from art import logo
# calculator
def add(a,b):
  '''sum up two values a and b'''
  return a + b
def subtract(a,b):
  return a - b
def multiply(a,b):
  return a * b
def divide(a,b):
  return a / b

#dictionaries
operations = {
  "+": add,
  "-":subtract,
  "*":multiply, 
  "/": divide
}
def calculator():
  print(logo)
  num1 = float(input("What is the first number?: "))
  
  for symbol in operations:
    print(symbol)
  should_continue = True
  while should_continue:
    operation_symbol = input("pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1,num2)
    print(f"{num1} {operation_symbol} {num2}  =  {answer}")
    request = input(f"type 'y' to continue calculating with {answer}, or type 'n' to start a new calculaton.: ")
    if request == 'y':
      num1 = answer
    else:  
      should_continue= False
      calculator()

calculator()
      
    
    
