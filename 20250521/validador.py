def verificar_presion(presion):
    if 100 <=  presion <= 300:
        return "Presión en rango peligroso"
    else:
        return "Presión en rango seguro"

def calcular_volumen_total(producción):
    volumen_total = 0
    for p in producción:
        if verificar_presion(p) == 'Presión en rango seguro':
            volumen_total += p
    return volumen_total
