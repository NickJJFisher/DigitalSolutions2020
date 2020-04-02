done = False
Letters = set()
x = 0
while done == False:
    word = input("Type a word: ")
    Letters.add(len(word))
    x = x + 1
    if word == "":
        done = True
Letters = list(Letters)
d = 0
y = 0
while d < x:
    y = Letters[d] + y
    d = d + 1
print ("Average Word Length: ", round((y/x)))