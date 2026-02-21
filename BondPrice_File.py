def getBondPrice(y, face, couponRate, m, ppy=1):
    y_eff = y/ppy
    m_eff = m * ppy
    coupon = face*couponRate/ppy
    bondPrice = 0

    for i in range (1,m_eff+1):
        bondPrice = bondPrice + coupon / (1 + y_eff) ** i
    bondPrice = bondPrice + face / (1 + y_eff) ** m_eff  
    return(bondPrice)
