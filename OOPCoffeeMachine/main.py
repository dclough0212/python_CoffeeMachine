from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

done = False

menu = Menu()
cm = CoffeeMaker()
moneyMachine = MoneyMachine()
  

while not done:

  response = input("What would you like? (espresso/latte/cappuccino): ")

  if response.lower() == "exit":
    break
  elif response.lower() == "report":
    cm.report()
  elif response.lower() in menu.get_items():
    myOrder = menu.find_drink(response)

    if (cm.is_resource_sufficient(myOrder)):     
      print(f"That will be ${myOrder.cost} (cough it up):") 
      if (moneyMachine.make_payment(myOrder.cost)):
        cm.make_coffee(myOrder)
  else:
    print(f"No comprendo {response}\n")