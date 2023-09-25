def strength(password):
    result = []
    digit = False
    upper = False
    if len(password) < 8:
        result.append(False)
    else:
        result.append(True)
    for i in password:
        if i.isdigit():
            digit = True
        if i.isupper():
            upper = True
    result.append(digit)
    result.append(upper)

    if all(result):
        output = "Strong Password"
    else:
        output = "Weak Password"
    return output

password = input("Input a password: ")
print(strength(password))