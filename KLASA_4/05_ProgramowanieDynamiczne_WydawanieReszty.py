
def MinimalnaLiczbaNominaluw(nominaly, kwota, n):
    MAX = kwota + 1
    LN = []
    nominal = 0
    for i in range(kwota):
        LN[i] = MAX
    LN[0] = 0
    for i in range(kwota):
        for j in range(n - 1):
            nominal = nominaly[j]
            if i >= nominal:
                if LN[i - nominal] + 1 < LN[i]:
                    LN[i] = LN[i - nominal] + 1
    if LN[kwota] != MAX:
        return LN[kwota]
    else:
        return -1
