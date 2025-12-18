print("Shipping Address Information\n")

civic_number = input("Enter Civic Number: ")
while civic_number == "" or not civic_number.isnumeric():
  if civic_number == "":
    print("Mandatory Field\n")
    civic_number = input("Enter Civic Number: ")
  else:
    print("Return a Valid Civic Number\n") 
    civic_number = input("Enter Civic Number: ")

street_name = input("\nEnter Street Name: ")
while street_name == "" or not street_name.replace(" ", "").isalpha():
  if street_name == "":
    print("Mandatory Field\n")
    street_name = input("Enter Street Name: ")
  else:
    print("Enter a Valid Street Name\n")
    street_name = input("Enter Street Name: ")

city_name = input("\nEnter City Name: ")
while city_name == "" or not city_name.replace(" ", "").isalpha():
  if city_name == "":
    print("Mandatory Field\n")
    city_name = input("Enter City Name: ")
  else:
    print("Enter a Valid City Name\n")
    city_name = input("Enter City Name: ")

province_code = input("\nEnter Province Code: ").upper()
while province_code == "" or len(province_code) != 2 or not province_code.isalpha():
  if province_code == "":
    print("Mandatory Field\n")
    province_code = input("Enter Province Code: ").upper()
  else:
    print("Enter a Valid 2-Letter Province Code\n")
    province_code = input("Enter Province Code: ").upper()

postal_code = input("\nEnter Postal Code (with space): ").upper()
while postal_code == "" or len(postal_code) !=7 or not (postal_code[0].isalpha() and postal_code[1].isnumeric() and postal_code[2].isalpha() and postal_code[3] == " " and postal_code[4].isnumeric() and postal_code[5].isalpha() and postal_code[6].isnumeric()):
  if postal_code == "":
    print("Mandatory Field\n")
    postal_code = input("Enter Postal Code: ").upper()
  else:
    print("Enter a Valid Postal Code\n")
    postal_code = input("Enter Postal Code: ").upper()

customer_name = input("\nEnter Customer Name: ")
while customer_name == "" or not customer_name.replace(" ", "").isalpha():
  if customer_name == "":
    print("Mandatory Field\n")
    customer_name = input("Enter Customer Name: ")
  else:
    print("Enter a Valid Customer Name\n")
    customer_name = input("Enter Customer Name: ")

customer_name = customer_name.title()
street_name = street_name.title()
city_name = city_name.title()

print("\nShip to:")
print(f"{customer_name}\n{civic_number} {street_name}\n{city_name} {province_code} {postal_code}")

