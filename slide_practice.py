# String - A group of characters

x = 10
s = "compsci click"

# Indexing of string s
# compsci cl i  c  k
# 0123456789 10 11 12

print(s[0])
print(s[4])
print(s[12])
# print(s[13]) Error

print()
print("==== Slicing ====")
print(s[0:7])
print(s[0:4])
# Includes first number (start)
# Does not include last number (stop)
print(s[-1])
print(s[8:-1])

print()
print("==== String Methods ====")
# Length
# len() function
print(len(s))
print(s[len(s) - 1])  # 12

# .find - Finds the location of a specific character
print(s.find("p"))
print(s.find("x"))  # Returns -1 since it can't find it

# .rfind - Finds the location of a specific character
# But from the reverse direction (right to left)
print(s.find("c"))  # Left to right, should be 0
print(s.rfind("c"))  # Right to left, shoud be 11

# Concatenation

t = "comparison"
u = "chunking"
v = "characters"
print()

if len(t) > 10:
	print(t + " is " + str(len(t)) + "characters long")
else:
	print("nevermind")

if len(u) < len(v):
	print(v + " wins!")
else:
	print(u + " wins!")

# ASCII Notes
print()
print("=== ASCII Character Set ===")
# ord()
# Grabs the ASCII code associated with the character
print(ord("A"))

# chr()
print(chr(66))
print(chr(98))

print("computers" < "computing")
# Helps with alphabetical order