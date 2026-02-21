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
