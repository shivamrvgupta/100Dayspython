# Function With outputs
def format_name(f_name, l_name):
	formated_f_name = f_name.title()
	formated_l_name = l_name.title()
	return f"{formated_f_name} {formated_l_name}"


formated_string = format_name("shivam", "gupta")

print(formated_string)

# LEap Year 
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) and month == 2:
        return 29
    return month_days[month -1]  

  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)



# Calculator

from art import logo

print(logo)



# add 
def add(a,b):
  return a + b

# add 
def subtract(a,b):
  return a - b

# add 
def multiply(a,b):
  return a * b

# add 
def divide(a,b):
  return a / b


operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

num1 = int(input("Enter the first Number : "))
num2 = int(input("Enter the second Number : "))

for symbol in operations:
  print(symbol)
operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)


print(f"{num1} {operation_symbol} {num2} = {answer}")


