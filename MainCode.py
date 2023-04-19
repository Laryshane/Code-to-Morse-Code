# Creates Morse Code Converter for numbers 0 - 9. All morse ends with a / so that 
# if user wants to use a 3rd party morse code converter to see if my converter 
# actual works, it'll read correctly. / = space in morse code.
def convert_to_morse(code):
  code = code.replace("1", ".----/")
  code = code.replace("2", "..---/")
  code = code.replace("3", "...--/")
  code = code.replace("4", "....-/")
  code = code.replace("5", "...../")
  code = code.replace("6", "-..../")
  code = code.replace("7", "--.../")
  code = code.replace("8", "---../")
  code = code.replace("9", "----./")
  code = code.replace("0", "-----/")
  return code

# Puts parameter around the users input so that they can not enter anything else
# other than numbers.
while True:
  try:
    print("Code must be numbers only and be between 1 and 7 characters\n")
    your_code = str(input("What would you like your code to be?: "))
    break
  except (ZeroDivisionError, ValueError, TypeError, AttributeError,
          SyntaxError):
    print("\nPlease use Numbers for your code, Try Again!\n")

# The if statement checks to make sure that only numbers were used
# and that the user used no letters.
while True:
  if your_code.isupper() or your_code.islower():
    print("\nPlease use only numbers. Try Again!")
    break
  else:
    morse = convert_to_morse(str(your_code))
    print(f"Morse code: {morse}")
    break
