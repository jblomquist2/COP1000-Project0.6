def save_vehicles():
  with open("AllowedVehiclesList.txt", "w") as db:
    for truck in AllowedVehiclesList:
      db.write(truck + "\n")

def print_all_vehicles():
  print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
  for truck in AllowedVehiclesList:
    print(truck)

def search_vehicle():
  response = input("Please enter the full Vehicle name: ")
  if response in AllowedVehiclesList:
    print(f'{response} is an authorized vehicle')
  else:
    print(f'{response} is not an authorized vehicle, if you received this in error please check the spelling and try again')

def add_vehicle():
  with open("AllowedVehiclesList.txt", "a"):
    response = input("Please enter the full Vehicle name you would like to add: ")
    AllowedVehiclesList.append(response)
    save_vehicles()
    print(f'You have added "{response}" as an authorized vehicle')

def delete_vehicle():
  response = input("Please Enter the full Vehicle name you would like to REMOVE: ")
  if response in AllowedVehiclesList:
    answer = input(f'Are you sure you want to remove "{response}" from the Authorized Vehicles list? ')
    if answer == "yes":
      AllowedVehiclesList.remove(response)
      save_vehicles()
      print(f'You have REMOVED "{response}" as an authorized vehicle')

AllowedVehiclesList = ["Ford F-150", "Chevrolet Silverado", "Tesla Cybertruck", "Toyota Tundra", "Nissan Titan", "Rivian R1T", "Ram 1500"]
save_vehicles()

print("********************************")
print("AutoCountry Vehicle Finder v1.0")
print("********************************")
print("Please Enter the following number below from the following menu:")
print("")
print("1. PRINT all Authorized Vehicles")
print("2. SEARCH for Authorized Vehicle")
print("3. ADD Authorized Vehicle")
print("4. DELETE Authorized Vehicle")
print("5. Exit")
print("********************************")

while True:
  number = int(input())
  if number == 1:
    print_all_vehicles()

  elif number == 2:
    search_vehicle()

  elif number == 3:
    add_vehicle()

  elif number == 4:
    delete_vehicle()

  elif number == 5:
    print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
    break