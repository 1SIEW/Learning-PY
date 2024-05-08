
import os,time
m_edad = True
m_rut = True
paciente = True
fecha= True
while True:
    os.system("cls")
    print("****Centro Médico DUOC****")
    print("1. Registrar Paciente")
    print("2. Atención Paciente")
    print("3. Consultar Datos Paciente")
    print("4. Salir")
    try:
        opc = int(input("\nIngresa una opcion\n"))
        if opc == 1:
            print("***Registrar Paciente***")
            os.system("cls")
            name=input("Ingresa nombre del paciente:\n")
            while name =="":
                name=input("Nombre del paciente no puede estar vacio")
                
            while m_rut:
                try:
                    rut = int(input("Ingresa rut del paciente:\n"))
                    if rut >=5000000 or rut <=999999999:
                        break
                    else:
                        input("Ingresa un rut dentro del rango 5000000 y 99999999.\n")
                except:
                    print("Ingresa solo numeros.\n")  
            os.system("cls")
            
            while m_edad:
                try:
                    edad=int(input("Ingresa edad del paciente:\n"))
                    if edad >= 0 or edad <111:
                        break
                    else:
                        input("Ingresa la edad dentro del rango 0 a 110")
                except:
                    print("Error: ingresa solo numeros.")
            os.system("cls")        
            
            direccion=input("Ingresa direccion del paciente:\n")
            while direccion == "":
                direccion=input("Error: Direccion del paciente no puede estar vacio")
            
            gender = input("Ingresa el genero del paciente:\n")
            while gender not in "fmFM" :
                gender = input("Error: ingresa un genero como f o m.\n")
            os.system("cls")    
            
            ps = input("Ingresa tu ps: isapre o fonasa.\n")
            while ps not in "isaprefonasaISAPREFONASA" :
                ps = print("Eligue isapre o fonasa")
            os.system("cls")
            
            email = input("Ingresa tu email, debe contener @ y un dominio exsiste\nEj: gmail.com, duocuc.cl\n")
            while "@"and "." not in email:
                email = input("Ingresa un email valido segun lo indicado parfavar.")
            os.system("cls")
            print("Datos de paciente completado.")
        elif opc ==2:
            print("***Atención Paciente***")
            os.system("cls")
            while paciente:
                try:
                    validacion_rut = int(input("Ingresa rut paciente para validar:\n"))
                    if validacion_rut == rut:
                        while fecha:
                            os.system("cls")    
                            print("Ingresa la fecha de ingreso para el paciente.\n")
                            try:
                                dia=int(input("Ingresa el dia.(1a31):\n"))
                                if dia >=1 and dia <=31:
                                    mes=int(input("Ingresa el mes.(1a12):\n"))
                                    if mes >=1 and mes <=12:
                                        os.system("cls")
                                        fecha_ingreso=(f"{dia}/{mes}/2024")
                                        print(f"Fecha de ingreso: {fecha_ingreso}")
                                        break
                                    else:
                                        print("Mes no es válido, debe estar entre 1 y 12.")
                                        os.system("cls")
                                else:
                                    print("Día no es válido, debe estar entre 1 y 31.")
                                    os.system("cls")
                            except:
                                print("Ingresa una fecha valida")
                                os.system("cls")

                        obs=input("Ingresa una las observaciones del paciente.\n")
                        while obs == "":
                            obs= input("Las observaciones del paciente no pueden estar vacias.")
                        print("\nregistrado ok")
                        break
                    else:
                        print("Rut de paciente no se encuentra registrado.")
                except:
                    print("Paciente no existe.")
            
        elif opc ==3:
            os.system("cls")
            print("***Consultar Datos Paciente***\n")
            print(f"NOMBRE:\t\\tt{name}")
            print(f"RUT:\t\t\t{rut}")
            print(f"EDAD:\t\t\t{edad}")
            print(f"SEXO:\t\t\t{gender}")
            print(f"DIRECCION:\t\t{direccion}")
            print(f"CORREO:\t\t\t{email}")
            print(f"PS:\t\t\t{ps}")
            print(f"FECHA DE INGRESO:\t{fecha_ingreso}\n")
            print(f"OBSERVACION:\t{obs}\n")
            cerrar_visualizacion=input("\npresiona para terminar la visualizacion.\n")
        elif opc ==4:
            print("Salir.")
            break
        time.sleep(2)
        os.system("cls")
    except:
        print("Opcion no existe.")
os.system("cls")        
print("Ha salido del sistema…\n")
