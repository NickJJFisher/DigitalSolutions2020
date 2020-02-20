ppl = int(input("How many people are attending?: "))
hdpp = int(input("How many hot dogs per person?: "))

ttlhd = ppl * hdpp
HotdogsPackets = ttlhd // 10
HotdogsRemainder = ttlhd % 10
BunsPackets = ttlhd // 8
BunsRemainder = ttlhd % 8

print ("For a hod dog cookout for ", ppl," people, with each person eating", hdpp, "hotdogs, then ", HotdogsPackets)
print ("hot dog packets will be required with a remainder of", HotdogsRemainder, "with", BunsPackets, " Bun Packets being required")
print ("with a remainder of ", BunsRemainder, "buns left over")
