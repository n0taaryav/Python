#Palindrome Checker
input2 = input("Enter A String: ")

reversed = input2[::-1]
if reversed == input2:
  print("It is a palindrome!")
else:
  print("It is not a palindrome")