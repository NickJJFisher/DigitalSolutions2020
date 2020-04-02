laps = int(input("How many laps have you done?"))
c = 0
run = set()
while c < laps:
    s = int(input("Time for the lap (in seconds): "))
    c = c + 1
    run.add(s)
run = list(run)
print("Fastest lap: " , run[0])
print("Slowest Lap: ", run[c-1])
d = 0
x = 0
while d < laps:
    x = run[d] + x
    d = d + 1
print ("Average lap time: ", x/laps)


