"""
1. Calcular precio y tipo en función de edad
2. Pedir la edad
    Validar == int y > 0
    Solicitar hasta que se introduzca ""
3. Calcular precio total de grupo
4. Mostrar precio total y desglose por tipo de entrada
"""

precioTotal = 0
grupoPersonas = []
tipos_entradas = ["GRATUITA", "NINYOS", "ADULTOS", "JUBILADOS"]

GRATUITA = 0
NINYOS = 1
ADULTOS = 2
JUBILADOS = 3

#no ponemos += porque es variable local,
#crearemos otra función para el sumatorio

def calculo_entrada(edad):
    precio = 0
    if edad < 3:
        precio = 0
        tipo = GRATUITA
    elif edad < 13:
        precio = 14
        tipo = NINYOS
    elif edad < 65:
        precio = 23
        tipo = ADULTOS
    else:
        precio = 18
        tipo = JUBILADOS
    
    return precio, tipo



def validaEdad(dato):
    result = False
    try:
        int(dato) #si la conversión a int es correcta
        result = True
    except ValueError:
        result = False
    return result


while True:
    edad = input("Edad del visitante: ") #entra como str
    if edad == "":
        break
    elif validaEdad(edad):
        grupoPersonas.append(calculo_entrada(int(edad)))


contadores_entradas = [0,0,0,0] #una posición por cada tipo de entrada
totales_entradas = [0,0,0,0]

#entradaGratuita = 0
#precioGratuita = 0
#entradaNinios = 0
#precioNinios = 0
#entradaAdultos = 0
#precioAdultos = 0
#entradaJubilados = 0
#precioJubilados = 0

num_entradas = len(grupoPersonas)

for precio, tipo in grupoPersonas:
    precioTotal += precio
    contadores_entradas[tipo] += 1
    totales_entradas[tipo] += precio

# for precio, tipo in grupoPersonas:
#     precioTotal += precio
#     if tipo == GRATUITA:
#         entradaGratuita += 1
#         precioGratuita += precio
#     elif tipo == NINYOS:
#         entradaNinios += 1
#         precioNinios += precio
#     elif tipo == ADULTOS:
#         entradaAdultos += 1
#         precioAdultos += precio
#     elif tipo == JUBILADOS:
#         entradaJubilados += 1
#         precioJubilados += precio

for i in range(4):
    print(f"{contadores_entradas[i]:2d} entradas {tipos_entradas[i]} {totales_entradas[i]:6.2f} €")

# print(f"{entradaGratuita:2d} entradas gratuitas: {precioGratuita:6.2f} €")
# print(f"{entradaNinios:2d} entradas de niño: {precioNinios:6.2f} €") #6 números en total, 2 decimales
# print(f"{entradaAdultos:2d} entradas de adulto: {precioAdultos:6.2f} €")
# print(f"{entradaJubilados:2d} entradas de jubilado: {precioJubilados:6.2f} €")

print(f"Numero de entradas: {num_entradas} ")
print(f"Total a pagar.....: {precioTotal:6.2f} €")