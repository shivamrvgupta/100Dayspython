# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# If else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height > 120:
  print("Can Ride")
  age = int(input("What is your age? "))
  if age >= 18:
    print("Pay 12$")
  else:
    print("Pay 7$")
else:    
  print("Cannot Ride")
    

# ELIF

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
value = weight / (height * height)
bmi = round(value)

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25 : 
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30 : 
        print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35 : 
            print(f"Your BMI is {bmi}, you are obese.")
else:
        print(f"Your BMI is {bmi}, you are clinically obese.")      

# ///// leap year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


# PIzzaaaaaa

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else: 
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3  

if extra_cheese == "Y":
    bill += 1


print(f"Your final bill is: ${bill}")