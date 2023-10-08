import sys


### Template code. Not subject for change. ###
def countdown(n: int) -> None:
  if n <= 0:
    print("Blastoff!")
  else:
    print(n)
    countdown(n-1)
### Template code. Not subject for change. ###


# Define countup recursive function
def countup(n: int) -> None:
  if n >= 0: # Base case
    print("Blastoff!")
  else:
    print(n) # Show number
    countup(n+1) # Recursive case


# Check for Python version
if sys.version_info[0] < 3:
  num = int(raw_input("Enter a number: "))
else:
  num = int(input("Enter a number: "))

if num > 0: # Positive number
  countdown(num)
elif num < 0: # Negative number
  countup(num)
else: # Zero
  raise ValueError("Not supported.")