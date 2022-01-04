programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

print(programming_dictionary)
print(programming_dictionary["Function"])
# adding new 
programming_dictionary["loop"] = "repating a code"

print(programming_dictionary)

# replacing the existing one
programming_dictionary["Bug"] = "changed value"
print(programming_dictionary)