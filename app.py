import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import sys
import os
import tempfile
import shutil

# Función para manejar archivos empaquetados
def get_file_path(relative_path):
    """Obtiene la ruta correcta del archivo, funciona en .exe y desarrollo"""
    try:
        # PyInstaller crea una carpeta temporal en _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

def extract_program_files():
    """Extrae los archivos .py del .exe a una carpeta temporal"""
    temp_dir = tempfile.mkdtemp()
    archivos = ["divisibilidad.py", "primos.py", "tfa.py", "recursividad.py", "euclides.py"]
    
    for archivo in archivos:
        try:
            # Ruta del archivo dentro del .exe
            source_path = get_file_path(archivo)
            # Ruta destino en carpeta temporal
            dest_path = os.path.join(temp_dir, archivo)
            
            # Copiar archivo
            shutil.copy2(source_path, dest_path)
        except Exception as e:
            print(f"Error extrayendo {archivo}: {e}")
    
    return temp_dir

class ProgramaMatematicas:
    def __init__(self, root):
        self.root = root
        self.root.title("Programas Matemáticos")
        self.root.geometry("700x600")
        self.root.configure(bg='#DFBBCA')
        
        # Carpeta temporal donde estarán los archivos extraídos
        self.temp_dir = extract_program_files()
        
        self.centrar_ventana()
        self.crear_menu_principal()
        
        # Diccionario con definiciones de cada programa
        self.definiciones = {
            "Divisibilidad": "La divisibilidad estudia las condiciones bajo las cuales un número puede ser dividido exactamente por otro. Un número 'a' es divisible por 'b' si existe un número entero 'c' tal que a = b × c.\n\nCriterios de divisibilidad:\n• Por 2: Último dígito par\n• Por 3: Suma de dígitos divisible por 3\n• Por 4: Últimos dos dígitos divisible por 4\n• Por 5: Termina en 0 o 5\n• Por 9: Suma de dígitos divisible por 9\n• Por 10: Termina en 0",
            
            "TFA": "El Teorema Fundamental de la Aritmética establece que todo número entero mayor que 1 puede ser representado de manera única como producto de números primos, ignorando el orden de los factores.\n\nEste teorema garantiza que:\n• Cada número tiene una descomposición única en factores primos\n• Los números primos son los 'bloques de construcción' de todos los números\n• No importa el orden en que se multipliquen los factores primos",
            
            "Números Primos": "Los números primos son aquellos números naturales mayores que 1 que solo son divisibles por sí mismos y por 1. Son los 'bloques de construcción' de todos los números enteros.\n\nPropiedades importantes:\n• El 2 es el único número primo par\n• Hay infinitos números primos (Euclides)\n• Los números mayores que 1 que no son primos se llaman compuestos\n• La distribución de primos sigue patrones complejos",
            
            "Recursividad": "La recursividad es un concepto en programación y matemáticas donde una función se define en términos de sí misma. Es especialmente útil para resolver problemas que pueden ser divididos en subproblemas similares.\n\nCaracterísticas:\n• Caso base: Condición de terminación\n• Caso recursivo: La función se llama a sí misma\n• Ejemplos clásicos: Factorial, Fibonacci\n• Ventaja: Código más elegante para problemas recursivos naturales",
            
            "MCD y MCM": "El Máximo Común Divisor (MCD) es el número más grande que divide exactamente a dos o más números. El Mínimo Común Múltiplo (MCM) es el número más pequeño que es múltiplo de dos o más números.\n\nPropiedades:\n• MCD(a,b) × MCM(a,b) = a × b\n• Algoritmo de Euclides: Método eficiente para calcular MCD\n• El MCD se usa para simplificar fracciones\n• El MCM se usa para sumar fracciones con diferente denominador"
        }
        
        # Diccionario con nombres de archivos (ahora en carpeta temporal)
        self.archivos = {
            "Divisibilidad": os.path.join(self.temp_dir, "divisibilidad.py"),
            "TFA": os.path.join(self.temp_dir, "tfa.py"), 
            "Números Primos": os.path.join(self.temp_dir, "primos.py"),
            "Recursividad": os.path.join(self.temp_dir, "recursividad.py"),
            "MCD y MCM": os.path.join(self.temp_dir, "euclides.py")
        }

    def __del__(self):
        """Limpia la carpeta temporal al cerrar el programa"""
        try:
            if hasattr(self, 'temp_dir'):
                shutil.rmtree(self.temp_dir, ignore_errors=True)
        except:
            pass

    def centrar_ventana(self):
        """Centra la ventana en la pantalla"""
        self.root.update_idletasks()
        ancho = 700
        alto = 600
        x = (self.root.winfo_screenwidth() // 2) - (ancho // 2)
        y = (self.root.winfo_screenheight() // 2) - (alto // 2)
        self.root.geometry(f'{ancho}x{alto}+{x}+{y}')

    def crear_menu_principal(self):
        """Crea el menú principal con los 5 programas"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#DFBBCA', padx=30, pady=40)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        titulo = tk.Label(main_frame, text="PROGRAMAS MATEMÁTICOS", 
                         font=('Arial', 24, 'bold'), 
                         fg='black', bg='#DFBBCA')
        titulo.pack(pady=(0, 30))
        
        # Frame para botones
        botones_frame = tk.Frame(main_frame, bg='#DFBBCA')
        botones_frame.pack(expand=True)
        
        # Botones para cada programa
        programas = [
            "Divisibilidad",
            "TFA", 
            "Números Primos",
            "Recursividad",
            "MCD y MCM"
        ]
        
        # Colores para botones del menú principal
        colores_botones = ['#8674C9', '#774972', '#7C5D72', '#710755', '#8674C9']
        
        for i, programa in enumerate(programas):
            color_btn = colores_botones[i % len(colores_botones)]
            btn = tk.Button(botones_frame, text=programa, 
                          font=('Arial', 14, 'bold'),
                          width=20, height=2,
                          bg=color_btn, fg='white',
                          activebackground='#5A4A6B',
                          relief='raised',
                          borderwidth=2,
                          command=lambda p=programa: self.mostrar_definicion(p))
            btn.pack(pady=10)
        
        # Botón salir
        btn_salir = tk.Button(main_frame, text="SALIR", 
                             font=('Arial', 12, 'bold'),
                             width=15, height=1,
                             bg='#7B0323', fg='white',
                             activebackground='#5A021A',
                             relief='raised',
                             borderwidth=2,
                             command=self.cerrar_programa)
        btn_salir.pack(pady=20)

    def cerrar_programa(self):
        """Cierra el programa limpiando recursos"""
        try:
            if hasattr(self, 'temp_dir'):
                shutil.rmtree(self.temp_dir, ignore_errors=True)
        except:
            pass
        self.root.quit()

    def mostrar_definicion(self, programa):
        """Muestra la ventana con la definición del programa seleccionado"""
        # Limpiar ventana
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#DFBBCA', padx=30, pady=30)
        main_frame.pack(expand=True, fill='both')
        
        # Título
        titulo = tk.Label(main_frame, text=programa, 
                         font=('Arial', 20, 'bold'), 
                         fg='black', bg='#DFBBCA')
        titulo.pack(pady=(0, 20))
        
        # Frame para definición
        def_frame = tk.Frame(main_frame, bg='#DFBBCA')
        def_frame.pack(fill='both', expand=True, pady=20)
        
        # Área de texto para definición
        texto_def = scrolledtext.ScrolledText(def_frame, 
                                            wrap=tk.WORD,
                                            width=70, 
                                            height=15,
                                            font=('Arial', 12),
                                            bg='#F5E6E8',
                                            fg='black',
                                            insertbackground='black',
                                            relief='sunken',
                                            borderwidth=2,
                                            padx=10, pady=10)
        texto_def.pack(fill='both', expand=True)
        texto_def.insert('1.0', self.definiciones[programa])
        texto_def.config(state='disabled')
        
        # Frame para botones
        btn_frame = tk.Frame(main_frame, bg='#DFBBCA')
        btn_frame.pack(pady=20)
        
        # Botones Ejecutar y Ver Código
        btn_ejecutar = tk.Button(btn_frame, text="EJECUTAR", 
                                font=('Arial', 12, 'bold'),
                                width=12, height=1,
                                bg='#774972', fg='white',
                                activebackground='#5A384A',
                                relief='raised',
                                borderwidth=2,
                                command=lambda: self.ejecutar_programa(programa))
        btn_ejecutar.pack(side='left', padx=10)
        
        btn_codigo = tk.Button(btn_frame, text="VER CÓDIGO", 
                              font=('Arial', 12, 'bold'),
                              width=12, height=1,
                              bg='#8674C9', fg='white',
                              activebackground='#6A5CA9',
                              relief='raised',
                              borderwidth=2,
                              command=lambda: self.mostrar_codigo(programa))
        btn_codigo.pack(side='left', padx=10)
        
        # Botón regresar
        btn_regresar = tk.Button(btn_frame, text="REGRESAR", 
                                font=('Arial', 12, 'bold'),
                                width=12, height=1,
                                bg='#7C5D72', fg='white',
                                activebackground='#5D4655',
                                relief='raised',
                                borderwidth=2,
                                command=self.crear_menu_principal)
        btn_regresar.pack(side='left', padx=10)

    def ejecutar_programa(self, programa):
        """Ejecuta el programa en una consola externa"""
        try:
            archivo_path = self.archivos[programa]
            
            # Verificar si el archivo existe
            if not os.path.exists(archivo_path):
                messagebox.showerror("Error", f"No se encontró el archivo: {archivo_path}")
                return
            
            # Ejecutar en consola externa
            if sys.platform == "win32":
                subprocess.Popen(['cmd', '/k', 'python', archivo_path], 
                               creationflags=subprocess.CREATE_NEW_CONSOLE)
            elif sys.platform == "darwin":
                subprocess.Popen(['open', '-a', 'Terminal', archivo_path])
            else:
                subprocess.Popen(['xterm', '-e', 'python3', archivo_path])
                
            messagebox.showinfo("Éxito", f"El programa '{programa}' se está ejecutando en una consola externa.")
            
        except FileNotFoundError:
            messagebox.showerror("Error", "No se pudo encontrar Python en el sistema. Asegúrate de que Python esté instalado y en el PATH.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo ejecutar el programa: {e}")

    def mostrar_codigo(self, programa):
        """Muestra el código del programa seleccionado"""
        try:
            archivo_path = self.archivos[programa]
            
            # Verificar si el archivo existe
            if not os.path.exists(archivo_path):
                messagebox.showerror("Error", f"No se encontró el archivo: {archivo_path}")
                return
            
            # Leer el contenido del archivo
            with open(archivo_path, 'r', encoding='utf-8') as f:
                codigo = f.read()
            
            # Crear nueva ventana para mostrar código
            ventana_codigo = tk.Toplevel(self.root)
            ventana_codigo.title(f"Código: {programa}")
            ventana_codigo.geometry("900x700")
            ventana_codigo.configure(bg='#DFBBCA')
            ventana_codigo.transient(self.root)
            ventana_codigo.grab_set()
            
            # Centrar ventana
            ventana_codigo.update_idletasks()
            ancho = 900
            alto = 700
            x = (ventana_codigo.winfo_screenwidth() // 2) - (ancho // 2)
            y = (ventana_codigo.winfo_screenheight() // 2) - (alto // 2)
            ventana_codigo.geometry(f'{ancho}x{alto}+{x}+{y}')
            
            # Frame principal
            main_frame = tk.Frame(ventana_codigo, bg='#DFBBCA', padx=20, pady=20)
            main_frame.pack(expand=True, fill='both')
            
            # Título
            titulo = tk.Label(main_frame, text=f"CÓDIGO: {programa}", 
                             font=('Arial', 16, 'bold'), 
                             fg='black', bg='#DFBBCA')
            titulo.pack(pady=(0, 20))
            
            # Área de texto para código
            texto_codigo = scrolledtext.ScrolledText(main_frame, 
                                                   wrap=tk.WORD,
                                                   width=100, 
                                                   height=35,
                                                   font=('Consolas', 10),
                                                   bg='#2D2B3D',
                                                   fg='#E8E6F2',
                                                   insertbackground='white',
                                                   relief='sunken',
                                                   borderwidth=2,
                                                   padx=10, pady=10)
            texto_codigo.pack(fill='both', expand=True, pady=10)
            texto_codigo.insert('1.0', codigo)
            texto_codigo.config(state='disabled')
            
            # Frame para botón
            btn_frame = tk.Frame(main_frame, bg='#DFBBCA')
            btn_frame.pack(pady=10)
            
            # Botón regresar
            btn_regresar = tk.Button(btn_frame, text="REGRESAR", 
                                   font=('Arial', 12, 'bold'),
                                   width=15, height=1,
                                   bg='#7B0323', fg='white',
                                   activebackground='#5A021A',
                                   relief='raised',
                                   borderwidth=2,
                                   command=ventana_codigo.destroy)
            btn_regresar.pack()
            
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo: {e}")

def main():
    root = tk.Tk()
    app = ProgramaMatematicas(root)
    root.mainloop()

if __name__ == "__main__":
    main()