
def CheckLeap(Year):  
  # Checking if the given year is leap year  
  if((Year % 400 == 0) or  
     (Year % 100 != 0) and  
     (Year % 4 == 0)):   
    print("Given Year is a leap Year");
    return True
  # Else it is not a leap year  
  else:  
    print ("Given Year is not a leap Year")
    return False

def getUserInput():
  userinput = input("Enter the number: ")
  if userinput.isdigit():
    Year = int(userinput)
    return Year
  else:
    return "error"

if __name__ == '__main__':
  # Taking an input year from user  
  # Printing result  
  CheckLeap(getUserInput())