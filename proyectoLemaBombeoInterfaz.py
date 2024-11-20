import tkinter as tk
from tkinter import messagebox, scrolledtext
import re
from collections import Counter

class LemaApp:

    def __init__(self, master):
    
        self.master = master
        # Titulo pestaña
        master.title("Verificador de Lema de Bombeo")
        master.geometry("500x600")

        # Mensaje de ayuda
        self.help_label = tk.Label(
            master, 
            text=
                "Instrucciones:\n\n"
                "1. Ingrese una cadena en formato a^ns^mb^p\n"
                "   en caso de querer colocar solo un caracter poner en formato a^1\n\n"
                "2. Defina las reglas de validación\n"
                "   para esto puede poner ( <, <=, >, >=, == ) ej n <= m\n\n"
                "3. Haga clic en Procesar, esto le solicitara unos datos complemetarios.\n", 
            justify=tk.LEFT, 
            wraplength=550
        )

        self.help_label.pack(pady=10)

        # Entrada de cadena
        tk.Label(master, text="Cadena de Lenguaje:").pack()
        self.entrada_entry = tk.Entry(master, width=50)
        self.entrada_entry.pack(pady=5)
        self.entrada_entry.insert(0, "a^n s^m ")

        # Entrada de reglas
        tk.Label(master, text="Reglas de Validación (separadas por comas):").pack()
        self.reglas_entry = tk.Entry(master, width=50)
        self.reglas_entry.pack(pady=5)
        self.reglas_entry.insert(0, "n <= m")

        # Botón de procesamiento
        self.procesar_btn = tk.Button(master, text="Procesar", command=self.procesar)
        self.procesar_btn.pack(pady=20)

        # Área de logs
        tk.Label(master, text="Logs del proceso:").pack()
        self.log_area = scrolledtext.ScrolledText(master, width=50, height=10)
        self.log_area.pack(pady=10)

    def log(self, mensaje):
        self.log_area.insert(tk.END, mensaje + "\n")
        self.log_area.see(tk.END)

    def procesar(self):
        # Limpiar logs previos
        self.log_area.delete(1.0, tk.END)
        
        try:
            # Recuperar entradas
            entrada = self.entrada_entry.get()
            reglas_str = self.reglas_entry.get()
            
            # Proceso similar al script original
            reglas = [regla.strip() for regla in reglas_str.split(',')]
            
            # Llamar a las funciones originales (expandir, validar_reglas, etc.)
            cadena_expandida, valores_exponentes, elementos = self.expandir(entrada)
            
            self.log(f"Cadena expandida: {cadena_expandida}")
            self.log(f"Valores de exponentes: {valores_exponentes}")
            self.log("\n")
            
            if not self.validar_reglas(valores_exponentes, reglas):
                self.log("Algunas reglas no se cumplen. No pertenece al lenguaje.")
                return
            
            else:
                self.log("Todas las reglas basicas se cumplen, se procede con el lema de bombeo.\n")
            
                # Pedimos al usuario el valor de p para dividir la cadena expandida
                while True:
                    p = self.solicitar_valor("p")
                    if p < len(cadena_expandida):
                        break
                    self.log(f"El valor de p debe ser menor que la longitud de la cadena expandida ({len(cadena_expandida)}). Intente de nuevo.")

                # Dividimos la cadena expandida en x, y, z
                x, y, z = self.dividir_cadena(cadena_expandida, p)
                cadenaBombeada = x+y+z

                self.log(f"Cadena bombeada: {cadenaBombeada} \n")

                valores_exponentes_b = {}
                contador = Counter(cadenaBombeada)

                # generacion del contador de los exponentes
                for letra, exponente in elementos:
                    # Actualizamos el valor del exponente con la cantidad de veces que aparece la letra
                    valores_exponentes_b[exponente] = contador[letra]

                self.log(f"cantidad de caracteres luego del bombeo: {valores_exponentes_b} \n")

                # se valida si se cumple con el lema o no 
                if (self.validar_reglas(valores_exponentes_b, reglas)):
                    self.log(f"cumple con el lema pero no se asegura que es un lenguaje regular.....")
                
                else:
                    self.log(f"No es un lenguaje regular ya que no cumple con el lema...")
                
                return

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def expandir(self, cadena):
        # Implementación de la función expandir original
        elementos = re.findall(r'([a-zA-Z])\^([a-zA-Z])', cadena)
        
        valores_exponentes = {}
        resultado = ""
        
        for letra, exponente in elementos:
            if exponente not in valores_exponentes:
                # Usar un diálogo para solicitar valores
                valor = self.solicitar_valor(exponente)
                valores_exponentes[exponente] = int(valor)
            
            resultado += letra * valores_exponentes[exponente]
        
        return resultado, valores_exponentes, elementos

    def solicitar_valor(self, exponente):
        # Diálogo para solicitar valores de exponentes
        valor = tk.simpledialog.askinteger("Entrada", f"Ingrese el valor para {exponente}:")
        return valor

    def validar_reglas(self, valores_exponentes, reglas):
        # Implementación de validación de reglas original
        for regla in reglas:
            try:
                if not eval(regla, {}, valores_exponentes):
                    self.log(f"La regla '{regla}' no se cumple.")
                    return False
            except Exception as e:
                self.log(f"Error en la regla '{regla}': {e}")
                return False
        return True

    def dividir_cadena(self, cadena_expandida, p):
        # Dividimos la cadena en tres partes según el valor de p
        x = cadena_expandida[:p-1]   # Primera parte de longitud p - 1
        y = cadena_expandida[p-1: p]  # Segunda parte de longitud p
        z = cadena_expandida[p:]  # El resto de la cadena
        y = y * 2
    
        return x, y, z

def main():
    root = tk.Tk()
    import tkinter.simpledialog  # Importar después de crear la raíz
    app = LemaApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
