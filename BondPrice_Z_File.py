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
