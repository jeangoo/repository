def manipulate_data():
    notas = []
    nombre = input("Ingrese su nombre: ")
    while True:
        notas.append(float(input("Ingrese sus notas: ")))
        if len(notas) == 3:
            break

    with open ("data.txt", "a+") as file:
        file.write(f"Nombre: {nombre} | Notas: {notas}\n")

manipulate_data()