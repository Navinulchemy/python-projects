MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":30,
            "coffee": 18,
        },
        "cost": 40,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 60,
    }
}

profit = 0
resources = {
    "water": 1000,
    "milk": 750,
    "coffee": 100,
}
logo='''
              _____  _____              
  ____  _____/ ____\/ ____\____   ____  
_/ ___\/  _ \   __\\   __\/ __ \_/ __ \ 
\  \__(  <_> )  |   |  | \  ___/\  ___/ 
 \___  >____/|__|   |__|  \___  >\___  >
     \/                       \/     \/ 
'''
water_capacity=resources["water"]
milk_capacity=resources["milk"]
coffee_capacity=resources["coffee"]
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
def report():
   for i in resources:
       print(f"THE AVAILABLE {i} is {resources[i]}")
def refill():

      if resources["water"] < 250:
        resources["water"] = (water_capacity-resources["water"]) + resources["water"]
      if resources["milk"] < 200:
        resources["milk"] = (milk_capacity-resources["milk"]) + resources["milk"]
      if resources["coffee"] < 30:
        resources["coffee"] = (coffee_capacity-resources["coffee"]) + resources["coffee"]
      report()






def is_resource_sufficient():
    if resources["water"] > MENU[choice]["ingredients"]["water"]:
        if resources["milk"] > MENU[choice]["ingredients"]["milk"]:
            if resources["coffee"] > MENU[choice]["ingredients"]["coffee"]:
               return True


def payment():
    global cost
    global bal
    cost = MENU[choice]["cost"]
    bal = pay - cost
    if pay > cost:
        print("PAYMENT SUCCESS")
        print(f"PLEASE TAKE YOUR BALANCE AMOUNT {bal}")
        return True
    elif pay == MENU[choice]["cost"]:
        print("payment success")
        return True
    else:
        print("your money is too low to process the order")
        return False
def make_coffee():
    if is_resource_sufficient():
        if payment():
            print("YOUR COFFEE IS MADE FRESHLY PLEASE WAIT........ ")
            print("THANKS FOR PATIENCE")
            print("PLEASE TAKE YOUR COFFEE")
            print(f"your bill :  COFFEE NAME : {choice}   cost:{cost}   paid:{pay}   balance:{bal}")
            global profit
            profit += cost

            resources["water"]-= MENU[choice]["ingredients"]["water"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            report()

    else:
        print("please wait while we fill our ingredients")
        refill()



flag=True
while flag:
 print(logo)
 flav=["1. espresso[COST = 40]","2. latte[COST = 50]","3. cappuccino[COST = 60]","4. ENTER Q TO QUIT"]
 for flavours in flav:
    print(flavours)
 choice=input("ENTER YOUR FLAVOUR : ").lower()

 if "report" in choice:
     report()
     quit()

 if "q" in choice:
     print(f"the profit is {profit}")
     quit()
 pay = int(input("ENTER THE COST AMOUNT YOU WANT TO PAY : "))
 make_coffee()

