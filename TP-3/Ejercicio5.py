hp_jugador = 100
hp_enemigo = 100
pociones = 3
dmg_base = 15
dmg_enemigo = 12

nombre = ""
while not nombre.isalpha():
    nombre = input("Ω Nombre del Gladiador: ")
    if not nombre.isalpha():
        print("! Solo se permiten letras -")

print("\n-:- Inicio de combate -:-")

while hp_jugador > 0 and hp_enemigo > 0:

    print(f"\n-·· {nombre} (HP: {hp_jugador}) vs Enemigo (HP: {hp_enemigo}) | ↑ Pociones: {pociones} ··-")

    opcion = ""
    while not opcion.isdigit():
        print("\n1. × Ataque Pesado")
        print("2. Ŧ Ráfaga Veloz")
        print("3. ↑ Curar")
        opcion = input("« Opción: ")

        if not opcion.isdigit():
            print("! Opción no válida -")
        elif int(opcion) not in [1,2,3]:
            print("! Fuera de rango -")

    opcion = int(opcion)

    if opcion == 1:
        if hp_enemigo < 20:
            dmg = dmg_base * 1.5
            print("¡ -Golpe-crítico- !")
        else:
            dmg = dmg_base

        hp_enemigo -= dmg
        print(f"ı: Atacaste al enemigo por {dmg} de daño -")

    elif opcion == 2:
        print("« Inicias una ráfaga de golpes »")
        for i in range(3):
            hp_enemigo -= 5
            print("ı: Golpe conectado por 5 de daño -")

    elif opcion == 3:
        if pociones > 0:
            hp_jugador += 30
            pociones -= 1
            print("ı: Te curaste 30 HP ↑")
        else:
            print("! No quedan pociones -")

    if hp_enemigo > 0:
        hp_jugador -= dmg_enemigo
        print(f"! El enemigo te atacó por {dmg_enemigo} de daño -")

print("\n-: Resultados :-")

if hp_jugador > 0:
    print("- ¡VICTORIA! -")
    print(f"ı: {nombre} ha ganado la batalla -")
else:
    print(".- Derrota -.")
    print("! Has caído en combate !")