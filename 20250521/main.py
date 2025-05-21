from validador import *

presiones = (90, 100, 150, 200, 250, 300, 301, 400)
for p in presiones:
    resultado = verificar_presion(p)
    print(f'Presión: {p}', resultado)

produccion = [100, 200, 300, 400, 500]
total = calcular_volumen_total(produccion)
print(f'Volumen total: {total}')