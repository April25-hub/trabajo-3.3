print("Arzaba Diaz April")
print("3W")
print("1173")
#esta linea es el diccionario que almacena los precios de las frutas por kilo
precios_frutas = {
    'manzana': 2.5,
    'banana': 1.2,
    'naranja': 1.8,
    'fresa': 3.0,
    'kiwi': 4.0
}

#esta linea solicitara al usuario el nombre de la fruta
fruta = input("ingresa el nombre de la fruta: ").lower()  
#esta linea solicitara al usuario el número de kilos
kilos = float(input("ingresa el número de kilos: "))

#esta linea verificara si la fruta está en el diccionario
if fruta in precios_frutas:
    #esta linea  calculars el precio total
    precio_total = precios_frutas[fruta] * kilos
    #esta linea mostrara el precio total
    print(f"el precio de {kilos} kilos de {fruta} es: ${precio_total:.2f}")
else:
    #esta linea dara el mensaje si la fruta no está en el diccionario
    print("la fruta no esta en el diccionario")
