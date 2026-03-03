romman="IV"
value={"I":1,"V":5,"X":10,"l":50,"c":100,"d":500,"M":1000}
total=0
for i in range(len(romman)):
    if i+1<len(romman) and value[romman[i]]<value[romman[i+1]]:
        total=total-value[romman[i]]
    else:
        total=total+value[romman[i]]
print(total)