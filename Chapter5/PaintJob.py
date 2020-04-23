Amount = int(input("How much in feet are you painting?"))
Cost = int(input("How much for a gallon of paint?"))
Paint = (Amount / 112)
print (Paint, "Galloons of paint is required")
Hours = (Paint / 8)
print (Hours, "hours of labour is required")
PaintCost = Paint * Cost
print (PaintCost, "dollars is required for the paint")
LabourCost = Hours * 35
print (LabourCost, "Dollars is required for labour")
print (PaintCost + LabourCost, " Is the total Cost")