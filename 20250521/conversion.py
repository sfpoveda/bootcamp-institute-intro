def celsius2farenheit():
    celsius = float(input('Por favor ingrese los grados Celsius:'))
    if not isinstance(celsius, (int, float)):
        raise ValueError('Debe ingresar un número.')
    farenheit = float(celsius)*9/5 + 32
    print(f'Grados Celsius: {celsius}')
    print(f'Grados Farenheit: {farenheit}')

def farenheit2celsius():
    farenheit = float(input('Por favor ingrese los grados Celsius:'))
    if not isinstance(farenheit, (int, float)):
        raise ValueError('Debe ingresar un número.')
    celsius = (farenheit - 32)*5/9
    print(f'Grados Celsius: {celsius}')
    print(f'Grados Farenheit: {farenheit}')