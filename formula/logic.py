def calcular_propina(total, porcentaje):
    decimal = porcentaje / 100
    propina = decimal * total
    return propina 

def calcular_total_con_propina(total, propina):
    return total + propina