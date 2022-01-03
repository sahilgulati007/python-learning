def greet():
  print("hello")
  print("how's you?")
  print("have a great day")

greet()

def greet_with_name(nm):
  print(f"hello {nm}")
  print("how's are you?")
  print(f"have a great day, {nm}")

greet_with_name("sahil")
greet_with_name(123)

def greet_with_name_loc(nm,loc):
  print(f"hello {nm}")
  print("how's are you?")
  print(f"have a great time in {loc}")

greet_with_name_loc("sahil","surat")
greet_with_name_loc(loc="surat",nm="sahil")