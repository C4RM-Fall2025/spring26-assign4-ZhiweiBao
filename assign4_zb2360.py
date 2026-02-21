# Identify yourself for grading
def WhoAmI():
    return('zb2360')

print(WhoAmI())


#getBondPrice
def getBondPrice(y, face, couponRate, m, ppy=1):
    y_eff = y/ppy
    m_eff = m * ppy
    coupon = face*couponRate/ppy
    bondPrice = 0

    for i in range (1,m_eff+1):
        bondPrice = bondPrice + coupon / (1 + y_eff) ** i
    bondPrice = bondPrice + face / (1 + y_eff) ** m_eff  
    return(bondPrice)

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
print("getBondPrice: ")
print("ppy = 1: ",getBondPrice(y, face, couponRate, m, 1))
print("ppy = 2: ",getBondPrice(y, face, couponRate, m, 2))
print("no ppy : ",getBondPrice(y, face, couponRate, m))


#getBondDuration
def getBondDuration(y, face, couponRate, m, ppy = 1):
    y_eff = y/ppy
    m_eff = m * ppy
    coupon = face*couponRate/ppy
    bondPrice = 0
    weightedSum = 0
    for i in range (1,m_eff+1):
        if i == m_eff:
            cf = coupon + face
        else:
            cf = coupon
        pv = cf / (1 + y_eff) ** i
        bondPrice = bondPrice + pv
        weightedSum = weightedSum + i*pv
    bondDuration = weightedSum/bondPrice
    bondDuration = bondDuration/ppy
    return(bondDuration)

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
print("getDuration: ", getBondDuration(y, face, couponRate, m, ppy))


#getBondPrice_Enumerate
def getBondPrice_E(face, couponRate, m, yc):
    coupon = face*couponRate
    bondPrice = 0
    for i, x in enumerate (yc, start=1):
        if i == m:
            cf = coupon + face
        else:
            cf = coupon
        pv = cf / (1 + x) ** i
        bondPrice = bondPrice + pv
        
    return(bondPrice)

yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04
m = 5
print("getBondPrice_Enumerate: ", getBondPrice_E(face, couponRate, m, yc))


#getBondPrice_Zip
def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face*couponRate
    bondPrice = 0
    for t,y in zip(times,yc):
        if t == times[-1]:
            cf = coupon + face
        else:
            cf = coupon
        pv = cf / (1 + y) ** t
        bondPrice = bondPrice + pv
    return(bondPrice)

yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04
print("getBondPrice_Zip: ", getBondPrice_Z(face, couponRate, times, yc))


#FizzBuzz
def FizzBuzz(start, finish):
    outlist = []
    for i in range (start,finish +1):
        if i % 3 == 0 and i % 5 == 0:
            outlist.append("fizzbuzz")
        elif i % 3 == 0:
            outlist.append("fizz")
        elif i % 5 == 0:
            outlist.append("buzz")
        else:
            outlist.append(i)
    
    return(outlist)
    
print("FizzBuzz 15: ", FizzBuzz(1,15))
