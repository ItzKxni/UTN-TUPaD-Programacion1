lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = ""

menu = '''
1» Reservar turno
2» Cancelar turno [Por nombre]
3» Ver agenda del día
4» Ver resumen general
5» Salir
'''

opcion = 0



operador = input("Nombre del operador: ")

while not operador.isalpha():
    print("ı Notificación: No valido -")
    operador = input("Nombre del operador: ")



while opcion != 5:
    print(menu)
    ent_opcion = input("« Seleccione opcion: ")
    
    while not ent_opcion.isdigit():
        print(menu)
        print("\nı Notificación: Opcion no valida -")
        ent_opcion = input("« Seleccione opcion: ")
        
    opcion = int(ent_opcion)


    
    if opcion == 1:
        nombre = input("ð Nombre del paciente: ")
        dia = input("? Día ([1] Lunes [2] Martes: ")
        
        
        if dia == "1":
            
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("! Paciente ya registrado") 

            
            
            if lunes1 == "":
                lunes1 = nombre
                print("! Registrado -")
            
            elif lunes2 == "":
                lunes2 = nombre
                print("! Registrado -")
            
            elif lunes3 == "":
                lunes3 = nombre
                print("! Registrado -")
            
            elif lunes4 == "":
                lunes4 = nombre
                print("! Registrado -")
            else:
                print("! No hay turnos disponibles - ")
                
        
        elif dia == "2":

            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("! Paciente ya registrado")

            else:
                if martes1 == "":
                    martes1 = nombre
                    print("! Registrado -")

                elif martes2 == "":
                    martes2 = nombre
                    print("! Registrado -")

                elif martes3 == "":
                    martes3 = nombre
                    print("! Registrado -")

                else:
                    print("! No hay turnos disponibles -")
    
    elif opcion == 2:
        
        dia = input("? Día ([1] Lunes [2] Martes): ")
        nombre = input("ð Nombre del paciente a cancelar: ")

        if dia == "1":

            if nombre == lunes1:
                lunes1 = ""
                print("! Turno cancelado")

            elif nombre == lunes2:
                lunes2 = ""
                print("! Turno cancelado")

            elif nombre == lunes3:
                lunes3 = ""
                print("! Turno cancelado")

            elif nombre == lunes4:
                lunes4 = ""
                print("! Turno cancelado")

            else:
                print("× Paciente no encontrado")

        elif dia == "2":

            if nombre == martes1:
                martes1 = ""
                print("! Turno cancelado")

            elif nombre == martes2:
                martes2 = ""
                print("! Turno cancelado")

            elif nombre == martes3:
                martes3 = ""
                print("! Turno cancelado")

            else:
                print("× Paciente no encontrado")
    
    elif opcion == 3: 
        
        dia = input("? Día ([1] Lunes [2] Martes): ")

        if dia == "1":

            print("\n- Agenda Lunes -\n")

            print("- Turno 1:", lunes1 if lunes1 != "" else "(libre)")
            print("- Turno 2:", lunes2 if lunes2 != "" else "(libre)")
            print("- Turno 3:", lunes3 if lunes3 != "" else "(libre)")
            print("- Turno 4:", lunes4 if lunes4 != "" else "(libre)")

        elif dia == "2":

            print("\n- Agenda Martes -\n")

            print("- Turno 1:", martes1 if martes1 != "" else "(libre)")
            print("- Turno 2:", martes2 if martes2 != "" else "(libre)")
            print("- Turno 3:", martes3 if martes3 != "" else "(libre)")

    elif opcion == 4:

        ocupados_lunes = 0
        ocupados_martes = 0

        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        if martes1 != "":
            ocupados_martes += 1
        if martes2 != "":
            ocupados_martes += 1
        if martes3 != "":
            ocupados_martes += 1


        libres_lunes = 4 - ocupados_lunes
        libres_martes = 3 - ocupados_martes


        print("« Resumen general »")
        print(f"- Lunes » Ocupados: {ocupados_lunes} | Libres: {libres_lunes}")
        print(f"- Martes » Ocupados: {ocupados_martes} | Libres: {libres_martes}")


        if ocupados_lunes > ocupados_martes:
            print("· El día con más turnos es: Lunes")

        elif ocupados_martes > ocupados_lunes:
            print("· El día con más turnos es: Martes")

        else:
            print("- Hay empate de turnos -")
            
    elif opcion == 5:
        print("¬ Saliendo...")
        break