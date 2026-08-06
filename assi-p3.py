password = input("Enter your password: ")

upper = False
lower = False
digit = False
speacial = False
repeated = False
speacial_char = "!@#$%^&*()-_=+[]{}|\\/:;'<>,.?"

for i in range(len(password)-1):
    if password[i]==password[i+1]:
        repeated=True

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    elif ch in speacial_char:
        speacial = True

print("\nPassword Analysis")
print("Uppercase letter :", upper)
print("Lowercase letter :", lower)
print("Digit            :", digit)
print("Speacial character:", speacial)
print("Repeated consective:",repeated)

if len(password)>=8 and upper and lower and digit and speacial and not repeated:
    print("Password strength:strong")
else:
    print("Password strength:week")
