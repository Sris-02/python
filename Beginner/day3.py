# conditional statements
# water_level = 50
# if water_level > 80:
#   print("Drain water")
# else:
#   print("Continue")

print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster! ")
else:
  print("Sorry, you have to grow taller before you can ride. ")

# Odd or Even exercise
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print("This is an even number. ")
else:
  print("This is an odd number. ")

# Nested if statements and elif statements
print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))
if height >= 120:
  print("You can ride the rollercoaster! ")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5. ")
  elif age <= 18:
    print("Please pay $7. ")
  else:
    print("Please pay $12. ")
else:
  print("Sorry, you have to grow taller beforre you can ride. ")

# BMI 2.0 exercise using nested if statements
height = float(input("enter your height in m: "))
weight = float(input("enter you weight in kg: "))
bmi = round(weight / height**2)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight. ")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight. ")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight. ")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese. ")
else:
  print(f"Your BMI is {bmi}, you are clinically obese. ")

# Leap year exercise
year = int(input("Which year do you want to check? "))
if year % 4 ==0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year. ")
    else :
      print("Not a leap year. ")
  else:
    print("Not a leap year. ")
else:
  print("Leap year. ")

# Multiple if statements in succession.
print("Welcome to the rollercoaster! ")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster! ")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5. ")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7. ")
  else:
    bill = 12
    print("Adult tickets are $12. ")
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    print(f"Your final bill is ${bill + 3}.")
else:
  print("Sorry, you have to grow taller beforre you can ride. ")

# Pizza order exercise :
print("Welcome to Python Pizza Deliveries! ")
size = input("What size pizza do you want? S, M, or L.")
add_pepperoni = input("Do you want pepperoni? Y or N. ")
