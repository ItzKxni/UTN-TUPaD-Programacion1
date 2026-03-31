energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0
nombre = ""

nombre = input("Ω Nombre del agente: ")

while not nombre.isalpha():
    print("ı: No valido. Intente nuevamente")
    nombre = input("Ω Nombre del agente: ")

print(f"\nBienvenido {nombre}")
print("! Misión: Abrir la bóveda\n")




while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    
    if alarma and tiempo <= 3:
        print("ı: Sistema bloqueado por alarma -")
        print("-· Mision Fallida ·-")
        break
    
    print("\n Estado")
    print(f'''
Energía: {energia}
Tiempo: {tiempo}
Cerraduras abiertas: {cerraduras_abiertas}
Alarma: {'ON' if alarma else 'OFF'}
''')

    opcion = ""

    while not opcion.isdigit():
        opcion = input("1- Forzar | 2- Hackear | 3- Descansar: ")


    opcion = int(opcion)
    
    
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1
    
        if racha_forzar == 3:
            print("ı: Forzaste demasiado. La cerradura se trabó -")
            print("¡Alarma Activada!")
            alarma = True
    
        else:
            if energia < 40:
                num = ""
                while not num.isdigit():
                    num = input("! Riesgo de alarma: Elige numero (1-3): ")
            
                if int(num) == 3:
                    print("-· Fallido ·-")
                    print("¡Alarma Activada!")
                    alarma = True
            
                else:
                    if not alarma:
                        cerraduras_abiertas += 1
                        print("ı: Se abrió una cerradura -")
        
            else:
                if not alarma:
                    cerraduras_abiertas += 1
                    print("ı: Se abrió una cerradura -")

    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0
    
        print("ı: Iniciando hackeo... -")
    
        for i in range(4):
            print(f"Paso {i+1}/4...")
            codigo_parcial += "A"
    
        print(f"ı: Código parcial: {codigo_parcial} -")
    
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("ı: Hackeo Exitoso: Se abrió una cerradura -")
        

    elif opcion == 3:
        energia += 15
        if energia > 100:
            energia = 100
    
        racha_forzar = 0
        tiempo -= 1
    
        if alarma: 
            energia -= 10
            print("ı: Descansaste, pero la alarma te drenó la energía extra -")

        print("ı: Recuperaste energía -")


print("\n«« Resultado de la misión »»")

if cerraduras_abiertas == 3:
    print("\n--:Mision Cumplida:-- ")
    print("ı: Abriste la bóveda -")

elif energia <= 0 or tiempo <= 0:
    print("\n--· Mision Fallida ·--")
    print("!: Te quedaste sin recursos - ")

elif alarma and tiempo <= 3:
    print("\n--· Mision Fallida ·--")
    print("!: Sistema bloqueado por alarma")