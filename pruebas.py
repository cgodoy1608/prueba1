#!/usr/bin/env python3
# -- coding: utf-8 --
"""

@author: claudio
"""

import os

x = 0
y = 0

campus = ["zona core", "campus uno", "campus matriz", "sector outsourcing"]

while True:
    os.system("clear")

    print("¿Qué quiere hacer? ")
    print("1. Ver los dispositivos.\n2. Ver los campus.\n3. Añadir dispositivo.\n4. Añadir campus.\n5. Borrar dispositivo.\n6. Borrar campus\n7. Salir")

    selector = int(input("Elija una opción: "))

    if selector == 1:
        os.system("clear")
        print("Elija un campus:\n")
        for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
        
        selector = int(input("\nElija una opción: "))
        if 1 <= selector <= len(campus):
            os.system("clear")
            file_name = campus[selector - 1] + ".txt"
            try:
                with open(file_name, "r") as file:
                    for item in file:
                        item = item.strip()
                        print(item)
            except FileNotFoundError:
                print(f"No se encontró el archivo {file_name}")
        else:
            print("Opción no válida.")
    
    elif selector == 2:
        os.system("clear")
        print("Lista de campus:\n")
        for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
# abreviaciones creadas en /n segun python 1 esential
    elif selector == 3:
        os.system("clear")  
        servicios = []
        print("¿Dónde agregar un nuevo dispositivo?\n")
        for idx, item in enumerate(campus, 1):
            print(f"{idx}. {item}")
        
        selector = int(input("\nElija una opción: "))
        if 1 <= selector <= len(campus):
            os.system("clear")
            file_name = campus[selector - 1] + ".txt"
            
            print("Elija un dispositivo:\n1. Router\n2. Switch\n3. Switch multicapa\n")
            dispositivo = int(input("Elija su opción: "))
            
            os.system("clear")
            nombre_dispositivo = input("Agregue el nombre de su dispositivo: ")

            while True:
                confirmacion = input("¿Confirma este nombre?\n1. Sí\n2. No\n")
                if confirmacion == "1":
                    print("Nombre confirmado.")
                    break
                else:
                    nombre_dispositivo = input("Reingrese el nombre de su dispositivo: ")
            
            print("Elija una jerarquía:\n1. Núcleo\n2. Acceso\n3. Distribución\n")
            jerarquia = int(input("Elija una opción: "))
            
            with open(file_name, "a") as file:
                file.write("\n---------------------------------\n")
                if dispositivo == 1:
                    file.write(f"Router: {nombre_dispositivo}\n")
                elif dispositivo == 2:
                    file.write(f"Switch: {nombre_dispositivo}\n")
                elif dispositivo == 3:
                    file.write(f"Switch multicapa: {nombre_dispositivo}\n")
                
                if jerarquia == 1:
                    file.write("Jerarquía: Núcleo\n")
                elif jerarquia == 2:
                    file.write("Jerarquía: Distribución\n")
                elif jerarquia == 3:
                    file.write("Jerarquía: Acceso\n")
                
                # Agregador de IP a los dispositivos 
                ip_dispositivo = input("Ingrese la dirección IP del dispositivo: ")
                file.write(f"IP: {ip_dispositivo}\n")

                if dispositivo == 2 or dispositivo == 3:
                    print("Elija un servicio de red:\n1. Datos\n2. VLAN\n3. Trunking\n4. Salir\n")
                    while True:
                        servicio = int(input("Elija una opción: "))
                        if servicio == 4:
                            break
                        elif servicio == 1:
                            servicios.append("Datos")
                        elif servicio == 2:
                            servicios.append("VLAN")
                        elif servicio == 3:
                            servicios.append("Trunking")
                    file.write(f"Servicio: {', '.join(servicios)}\n")
                
                file.write("---------------------------------\n")
            
            # Variable que guarda el txt dentro del spyder
            variable_name = input("Ingrese la variable que desea guardar en el archivo: ")
            with open(file_name, "a") as file:
                file.write(f"Variable guardada: {variable_name}\n")
            
            print("Dispositivo, IP y variable añadidos con éxito.")
        else:
            print("Opción no válida.")

    elif selector == 7:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no implementada.")
# para vovler al retorno
    input("\nPresione Enter para volver al menú principal...")
