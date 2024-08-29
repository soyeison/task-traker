
while True:
    print("""
Bienvenido a la CLI
a. Saludar
b. Salir 
    """)
    option = input("Ingrese una opcion: ")
    if option == "a":
        print("Melo pai")
    elif option == "b":
        break

print("Saliendo de la CLI...")