import time

points = int(input('''what was your grade out of 100?
'''))
if points <= 50:
    print("Fail")
elif points <= 59:
    print("Pass")
elif points <= 80:
    print("Credit")
elif points <= 100:
    print("Distinction")


