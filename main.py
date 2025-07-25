name = "Jean"
print(name)

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

try:
    c = float(input("Introduce la temperatura en °C: "))
    f = celsius_a_fahrenheit(c)
    print(f"{c} °C equivalen a {f:.2f} °F")
except ValueError:
    print("Por favor, introduce un número válido.")
