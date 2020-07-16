import random
RHeart = list(range(1, 13))
RDiamo = list(range(1, 13))
BSpade = list(range(1, 13))
BClove = list(range(1, 13))
cardList = [RHeart, RDiamo, BSpade, BClove]
suite1 = random.randint(0,3)
suite2 = random.randint(0,3)
print (suite1)
print(suite2)
random.shuffle(RDiamo)
random.shuffle(RHeart)
random.shuffle(BClove)
random.shuffle(BSpade)
print(RDiamo)
print(RHeart)
print(BClove)
print(BSpade)
cardno1 = cardList[suite1][0]
print(cardno1)
cardno2 = cardList[suite2][1]
print(cardno2)

RDiamo.remove(cardno1)

print(RDiamo)
print(RHeart)
print(BClove)
print(BSpade)