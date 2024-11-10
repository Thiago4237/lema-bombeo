import re
from collections import Counter

# ESTA FUNCION SE ENCARGA DE RECIBIR LA CADENA DEL LENGUAJE Y APARTE GENERA UNA CADENA PARA 
# VALIDAR EL LEMA DE BOMBEO 
def expandir(cadena):
    # Expresión regular para letras y exponentes
    elementos = re.findall(r'([a-zA-Z])\^([a-zA-Z])', cadena)
    
    # Diccionario para almacenar los valores de los exponentes ingresados por el usuario
    valores_exponentes = {}
    
    resultado = ""
    # se iteran los elementos encontrados en la cadena 
    for letra, exponente in elementos:

        # Pedimos el valor del exponente si no lo hemos solicitado antes
        if exponente not in valores_exponentes:
            valor = input(f"Ingrese el valor para {exponente}: ")
            valores_exponentes[exponente] = int(valor)
        
        # Repetimos la letra según el valor del exponente
        resultado += letra * valores_exponentes[exponente]
    
    return resultado, valores_exponentes, elementos

# ESTA FUNCION SE ENCARGA DE REALIZAR LAS VALIDACIONES A LA CADENA INGRESADA JUNTO CON LOS 
# VALORES DE LOS EXPONTES PARA VALIDAR SI SE DEBE SEGUIR EL PROCESO CON ESTA CADENA PARA EL LEMA DE 
# BOMBEO
def validar_reglas(valores_exponentes, reglas):
    # Iteramos sobre cada regla y la evaluamos usando los valores de los exponentes
    for regla in reglas:
        try:
            # Evalúa la regla usando los valores de los exponentes
            if not eval(regla, {}, valores_exponentes):
                print(f"La regla '{regla}' no se cumple.")
                return False
        except Exception as e:
            print(f"Error en la regla '{regla}': {e}")
            return False
    return True

# ESTA FUNCION SE ENCARGA DE REALIZAR LA SEPARACION EN LAS VARIABLES 
# X-Y-Z CON UN P INGRESADO POR EL USUARIO 
def dividir_cadena(cadena_expandida, p):
    # Dividimos la cadena en tres partes según el valor de p
    x = cadena_expandida[:p-1]   # Primera parte de longitud p - 1
    y = cadena_expandida[p-1: p]  # Segunda parte de longitud p
    z = cadena_expandida[p:]  # El resto de la cadena
    y = y * i
    
    return x, y, z



# Solicita al usuario la cadena de entrada
#entrada = "a^n s^m b^p"
entrada = input("Ingrese el lenguaje (ejemplo: a^n s^m b^p)") 

# Pedimos al usuario las reglas de validación
reglas = input("Ingrese las reglas de validación (separadas por comas, los operadores son: '<, > , <=, >=, ==') ")
reglas = [regla.strip() for regla in reglas.split(',')]

# Llamamos a la función para expandir la cadena y obtener los valores de los exponentes
cadena_expandida, valores_exponentes, elementos = expandir(entrada)
print("Cadena expandida:", cadena_expandida)
print("Cadena expandida:", valores_exponentes)
print("Cadena expandida:", elementos)

# Validamos las reglas usando los valores de los exponentes
if not validar_reglas(valores_exponentes, reglas):
    print("Algunas reglas no se cumplen con la formacion, por ende no pertenece al lenguaje y no se aplica el lema.")
else:
    print("Todas las reglas basicas se cumplen, se procede con el lema de bombeo.")

    # Pedimos al usuario el valor de p para dividir la cadena expandida
    while True:
        p = int(input("Ingrese el valor para dividir la cadena expandida (valor de p): "))
        if p < len(cadena_expandida):
            break
        print(f"El valor de p debe ser menor que la longitud de la cadena expandida ({len(cadena_expandida)}). Intente de nuevo.")

    # i para realizar el bombeo
    i = 2

    # Dividimos la cadena expandida en x, y, z
    x, y, z = dividir_cadena(cadena_expandida, p)
    cadenaBombeada = x+y+z

    print("Cadena bombeada:", cadenaBombeada)

    valores_exponentes_b = {}
    contador = Counter(cadenaBombeada)

    # generacion del contador de los exponentes
    for letra, exponente in elementos:
        # Actualizamos el valor del exponente con la cantidad de veces que aparece la letra
        valores_exponentes_b[exponente] = contador[letra]

    print(valores_exponentes_b)

    if (validar_reglas(valores_exponentes, reglas)) {
        print("cumple con el lema pero no se asegura que es un lenguaje regular.....")
    }
    else {
        print("No es un lenguaje regular ya que no cumple con el lema...")
    }
