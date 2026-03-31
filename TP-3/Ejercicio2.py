user = "admin"
clave = "1234"


menu = '''
1 - Ver estado de inscripción
2 - Cambiar clave
3 - Mensaje motivacional del dia
4 - Salir'''

att_limit = 3
attempts = 0


    
while attempts < att_limit:
    ingreso_user = input("ł Usuario: ")
    ingreso_clave = input("¬ Clave: ")
    
    if ingreso_user == user and ingreso_clave == clave:
        print("· Acceso Concedido ·")
        
        print(f'''
              Usuario: {user}
              Clave: {clave}''' )
        
        print("\n-.-. Campus .-.-")
        
        opcion = ""
        
        while opcion != 4:
            print(menu)
            ent_opcion = input("\n· Seleccione opción: ")
            
            while not ent_opcion.isdigit():
                print("- Notificación: Opcion no valida")
                ent_opcion = input("\n· Seleccione opción: ")

            opcion = int(ent_opcion)
            
            if opcion == 1:
                print("\n? Estado de inscripción: Inscripto ")
                
            elif opcion == 2: 
                new_clave = input("\n¬ Ingrese nueva clave: ")
                confirm_clave = input("¬ Confirme clave: ")
                
                
                if len(new_clave) < 6:
                    print("- Notificación: La clave debe contener al menos 6 caracteres -")
                
                elif new_clave != confirm_clave:
                    print("- Notificación: La contraseña debe coincidir -")
                
                else:
                    clave = new_clave
                    print("¬ La contraseña ha sido actualizada correctamente")
                
                
        
            elif opcion == 3:
                print(''' ð Mensaje del dia:
                      Trabajas para tu sueño o trabajas para el sueño de otro - Profe Francisco Varverde''')
            
            elif opcion == 4:
                print("-·Saliendo...\n")
            
            else:
                print("- Notificación: Opcion no valida. Fuera de rango")
            
    else:
        print("- Notificación: Credenciales invalidas - ")
        attempts += 1
        print(f"̉« {attempts}/3 intentos »")


if attempts == att_limit:
    print("- Notificación: Demasiados intentos. Cuenta Bloqueada.")
    print(f"{attempts}/3 intentos")