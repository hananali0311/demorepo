txt = "Hello world!"

print("slic (0:5)" , txt[0:5])
print("slice (-6:-1)", txt[-6:-1])
print("slice (7:)", txt[7:])
print("slice(-7)", txt[:-7])


# Modify strings

print(txt.upper())
print(txt.lower())
modified = txt.replace("Hello","Python")
print(modified)

name="Alice"
age="25"
formated = f"Her name is {name}, and age is {age}"
print(formated)

escaped = "This is string in \"double-quote\" string" 
print(escaped)

escaped = "This is a backlaash : \\"
print(escaped)

sample = "   Python Programming   "
print(sample.strip().startswith("Python"))
print(sample.strip())

print(bool("Hello")) # non empty string is true
print(bool(23)) # zero is false and non zero is true