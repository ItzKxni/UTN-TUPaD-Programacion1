nombre = ""
cantidad_productos = 0

total_sin_descuento = 0
total_con_descuento = 0



nombre = input("Ω Usuario: ")

while not nombre.isalpha() or nombre == "":
    print("- Notificación: No valido -")
    nombre = input("Ω Usuario: ")
    

intentos_productos = input("? Cantidad de productos: ")


while not intentos_productos.isdigit() or intentos_productos == "0":
    print("- Notificación: No valido. Solo numeros -")
    intentos_productos = input("? Cantidad de productos: ")
    
cantidad_productos = int(intentos_productos)


for i in range(cantidad_productos):
 
    ent_precio = input("$ Precio: $")
    
    while not ent_precio.isdigit():
        print("- Notificación: No valido -")
        ent_precio = input("$ Precio: $")
    precio = int(ent_precio)
    
    total_sin_descuento += precio 
    
    ask_descuento = ""
    
    while not ask_descuento == "S" and not ask_descuento == "N":
        ask_descuento = input("? Agregar descuento - S/N: ").upper()


    if ask_descuento == "S":

        descuento = precio * 0.90
        total_con_descuento += descuento 
        print("- Notificación: Se agrego con el 10% de descuento")

    elif ask_descuento == "N":
        total_con_descuento += precio
        print("- Notificación: Se agrego sin descuento")


prom = total_con_descuento / cantidad_productos

print("\n- - - - - - - - - - - - - - - - ")
print(f"Total con descuento: ${total_con_descuento}")
print(f"Total sin descuento: ${total_sin_descuento}")
print(f"Te ahorraste: ${(total_sin_descuento - total_con_descuento)}")
print(f"Promedio por producto: ${prom:.2f}\n")