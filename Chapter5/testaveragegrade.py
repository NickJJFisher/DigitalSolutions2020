Grade1 = int(input("What was your grade? "))
Grade2 = int(input("What was your grade? "))
Grade3 = int(input("What was your grade? "))
Grade4 = int(input("What was your grade? "))
Grade5 = int(input("What was your grade? "))
points = ((Grade1 + Grade2 + Grade3 + Grade4 + Grade5)/5)
if points <= 7:
    print("E-")
elif points <= 14:
    print("E")
elif points <= 21:
    print("E+")
elif points <= 28:
    print("D-")
elif points <= 35:
    print("D")
elif points <= 42:
    print("D+")
elif points <= 49:
    print("C-")
elif points <= 56:
    print("C")
elif points <= 63:
    print("C+")
elif points <= 70:
    print("B-")
elif points <= 77:
    print("B")
elif points <= 83:
    print("B+")
elif points <= 89:
    print("A-, Good Job!")
elif points <= 95:
    print("A, Great!")
elif points <= 100:
    print("A+, AWESOME!")
else:
    print("Invalid Response")
