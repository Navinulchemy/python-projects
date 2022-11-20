def addition(n1, n2):
    return n1 + n2


def subtraction(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1/n2
operation={
    "+":addition,
    "-":subtraction,
    "*":multiply,
    "/":division
}
def calculator():

 flag=True
 while flag == True:
     num1 = float(input("Enter the first number : "))
     for symbols in operation:
         print(symbols)
     operation_method = input("Enter any of the operation symbol listed above : ")
     num2 = float(input("Enter the second number : "))
     call_func = operation[operation_method]
     res=call_func(num1, num2)
     print(f"The result of {num1} {operation_method} {num2}  =  {res}")
     choice = input("TO PROCESS ANOTHER CALCULATION WITH SAME RESULT TYPE YES ELSE TYPE NO TO START NEW ONE : ").upper()
     another_calc = True
     if "NO" in choice:
       another_calc=False
       print("calculation finished")

     while another_calc==True:
      if "YES" in choice:
       num1 = res

       operation_method = input("Enter the operation symbol")
       num2 = float(input("Enter the second number : "))
       calc_func = operation[operation_method]
       output=calc_func(num1,num2)
      print(f"The result {num1} {operation_method} {num2} = {(output)}")
      choice2=int(input("to proceed another calculation type 1 else type 0 :" ))
      if choice2==0:
          another_calc=False
     start_new=int(input("To start a new calculation type 1 and to exit type 0 : "))

     if start_new==0:
       flag==False
       quit()

calculator()