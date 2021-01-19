
#resources dictionary
resources = { "Water": 500,
  "Milk": 200,
  "Coffee": 76,
  "Money": 2.5
}

menu = {
  "espresso" : (50, 0, 10, 1.5),
  "latte": (200,50,15,2.5),
  "cappuccino": (150,30,20,4)
}

def printReport():
  for x in resources:
    print(f"{x}: {resources[x]}")
  print("\n")

def processOrder(menuItem):
  if checkResources(menuItem):
    if processPayment(menuItem):
      makeCoffee(menuItem)

def checkResources(menuItem):
  if (menu.get(menuItem)[0] > resources["Water"]):
    print("Not enough water")
    return False
  if (menu.get(menuItem)[1] > resources["Milk"]):
    print("Not enough milk")
    return False    
  if (menu.get(menuItem)[2] > resources["Coffee"]):
    print("Not enough coffee")
    return False
  return True

def updateResources(menuItem):
  print("Updating resources")
  resources["Water"] = resources["Water"] - menu.get(menuItem)[0]
  resources["Milk"] = resources["Milk"] - menu.get(menuItem)[1]
  resources["Coffee"] = resources["Coffee"] - menu.get(menuItem)[2]

  print(f"{resources}")

def processPayment(menuItem):
  amountDue = menu.get(menuItem)[3];
  amountEntered = 0
  while amountEntered < amountDue:
    print(f"Amount due is {amountDue - amountEntered}")
    coinType = input("Enter coin type (p,n,d,q): ").lower()
    numOfCoin = input("Enter number of coins: ")
    if coinType == "p":
      amountEntered += int(numOfCoin) * .01
    if coinType == "n":
      amountEntered += int(numOfCoin) * .05 
    if coinType == "d":
      amountEntered += int(numOfCoin) * .10
    if coinType == "q":
      amountEntered += int(numOfCoin) * .25 

  resources["Money"] += amountEntered           
  return True

def makeCoffee(menuItem):
  updateResources(menuItem)
  print(f"Here is your {menuItem}!  Enjoy!\n")
  return True

done = False
while not done:

  response = input("What would you like? (espresso/latte/cappuccino): ")

  if response.lower() == "exit":
    break
  elif response.lower() == "report":
    printReport()
  elif response.lower() in menu.keys():
    processOrder(response.lower())
  else:
    print(f"No comprendo {response}\n")