def getBondPrice_E(face, couponRate, yc):
    coupon = face*couponRate
    bondPrice = 0
    m = len(yc)
    
    for i, x in enumerate (yc, start=1):
        if i == m:
            cf = coupon + face
        else:
            cf = coupon
        pv = cf / (1 + x) ** i
        bondPrice = bondPrice + pv
        
    return(bondPrice)
