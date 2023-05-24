menu = """
Bienvenido al conversor de monedas
1 - Pesos argentino
2 - pesos colombianos
3 - pesos mexicanos

Elige una opcion: """

opcion = int(input(menu))
if opcion == 1:
    pesos = input("cuantos dolares son: $")
    pesos = float(pesos)
    valor_dolar_blue = 497
    dolares = pesos / valor_dolar_blue
    dolares = round(dolares, 2)
    dolares = str(dolares)
    valor_dolar_blue = str(valor_dolar_blue)
    print("son $" + dolares + " dolares, a una cotizacion de: $" + valor_dolar_blue)
    
elif opcion == 2:
    pesos = input("cuantos dolares son: $")
    pesos = float(pesos)
    valor_dolar_blue = 4450
    dolares = pesos / valor_dolar_blue
    dolares = round(dolares, 2)
    dolares = str(dolares)
    valor_dolar_blue = str(valor_dolar_blue)
    print("son $" + dolares + " dolares, a una cotizacion de: $" + valor_dolar_blue)
elif opcion ==3:
    pesos = input("cuantos dolares son: $")
    pesos = float(pesos)
    valor_dolar_blue = 18
    dolares = pesos / valor_dolar_blue
    dolares = round(dolares, 2)
    dolares = str(dolares)
    valor_dolar_blue = str(valor_dolar_blue)
    print("son $" + dolares + " dolares, a una cotizacion de: $" + valor_dolar_blue)
else:
    print("ingresa una opcion correcta")
