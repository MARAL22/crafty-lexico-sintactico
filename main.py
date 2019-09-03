import LineNumber
from lexico import * 
from sintactico import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
 
class Menubar:

    def __init__(self, parent):
        font_specs = ("ubuntu", 14)

        menubar = tk.Menu(parent.master, font=font_specs)
        parent.master.config(menu=menubar)

        file_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        file_dropdown.add_command(label="Nuevo Archivo",
                                  accelerator="Ctrl+N",
                                  command=parent.new_file)
        file_dropdown.add_command(label="Abrir Archivo",
                                  accelerator="Ctrl+O",
                                  command=parent.open_file)
        file_dropdown.add_command(label="Guardar",
                                  accelerator="Ctrl+S",
                                  command=parent.save)
        file_dropdown.add_command(label="Guardar como",
                                  accelerator="Ctrl+Shift+S",
                                  command=parent.save_as)
        file_dropdown.add_separator()
        file_dropdown.add_command(label="Salir",
                                  command=parent.master.destroy)

        about_dropdown = tk.Menu(menubar, font=font_specs, tearoff=0)
        about_dropdown.add_command(label="Compilar",
                                   command=parent.compilar)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="Compilar-",
                                   command=parent.tony)
        about_dropdown.add_separator()
        about_dropdown.add_command(label="Limpiar Consola",
                                   command=parent.cleanConsole)

        tablas_dropdown = tk.Menu(menubar,font=font_specs, tearoff=0)
        tablas_dropdown.add_command(label='Palabras Reservadas',
                                        command=self.show_reservadas)
        tablas_dropdown.add_command(label='Tokens',
                                        command=parent.show_tokens)
        #tablas_dropdown.add_command(label='identificadores',command=parent.identificadores)



        menubar.add_cascade(label="Archivo", menu=file_dropdown)
        menubar.add_cascade(label="Opciones de compilacion", menu=about_dropdown)
        menubar.add_cascade(label="Tablas de simbolos", menu=tablas_dropdown)

    
    def show_reservadas(self):
        box_title = "Palabras Reservadas"
        box_message = "CRAFTY_DATA \n END_CRAFTY_DATA \n CRAFTY_START \n END_CRAFTY_START \n CRAFTY_LIGHT \n CRAFTY_WATER \n CRAFTY_WARM \n CRAFTY_AIR \n IOT_CONSOLE \n IF_INTENSITY \n LIGHT_UP \n LIGHT_DOWN \n LIGHT_BLINK \n SET_ \n GET_ \n TRUE \n FALSE \n WARM_UP \n WARM_DOWN \n WATER_UP \n WATER_DOWN \n AIR_UP \n AIR_DOWN \n FOR_IOT \n RETURN \n VOID \n INT \n ENDL"
        messagebox.showinfo(box_title, box_message)


class Statusbar:

    def __init__(self, parent):

        font_specs = ("ubuntu", 12)
        
        self.status = tk.StringVar()
        self.status.set("Crafty Editor V.1")

        #label = tk.Label(parent.textarea, textvariable=self.status, fg="black",
                         #bg="lightgrey", anchor='sw', font=font_specs)
        #label.pack(side=tk.BOTTOM, fill=tk.BOTH)

    def update_status(self, *args):
        if isinstance(args[0], bool):
            self.status.set("El archivo se ha guardado con exito")
        else:
            self.status.set("Crafty Editor V.1")


class PyText:

    def __init__(self, master):
        master.title("Sin titulo -Crafty Editor")
        master.geometry("950x550")

        font_specs = ("ubuntu", 14)

        self.master = master
        self.filename = None
        #text widget codigo
        self.textarea = tk.Text(master, font=font_specs)
        txt = LineNumber.LineMain(self.textarea)
        self.textarea.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
       
        #text widget consola
        self.console = tk.Text(fg="black",bg="lightgrey", font=font_specs)
        self.console.pack(side=tk.RIGHT, fill=tk.BOTH)



        self.menubar = Menubar(self)
        self.statusbar = Statusbar(self)
        self.bind_shortcuts()

    def set_window_title(self, name=None):
        if name:
            self.master.title(name + " - PyText")
        else:
            self.master.title("Sin titulo -Crafty Editor")

    def new_file(self, *args):
        self.textarea.delete(1.0, tk.END)
        self.console.delete(1.0,tk.END)
        self.filename = None
        self.set_window_title()

    def open_file(self, *args):
        self.filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("Todos los archivos", "*.*"),
                       ("Archivos de texto", "*.txt"),
                       ("Crafty Scripts", "*.ciot")])
        if self.filename:
            self.textarea.delete(1.0, tk.END)
            with open(self.filename, "r") as f:
                self.textarea.insert(1.0, f.read())
            self.set_window_title(self.filename)
    
    def save(self, *args):
        if self.filename:
            try:
                textarea_content = self.textarea.get(1.0, tk.END)
                with open(self.filename, "w") as f:
                    f.write(textarea_content)
                self.statusbar.update_status(True)
            except Exception as e:
                print(e)
        else:
            self.save_as()

    def save_as(self, *args):
        try:
            new_file = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("Todos los archivos", "*.*"),
                       ("Archivos de texto", "*.txt"),
                       ("Crafty Scripts", "*.ciot")])
            textarea_content = self.textarea.get(1.0, tk.END)
            with open(new_file, "w") as f:
                f.write(textarea_content)
            self.filename = new_file
            self.set_window_title(self.filename)
            self.statusbar.update_status(True)
        except Exception as e:
            print(e)

    def compilar(self):
        self.console.delete(1.0,tk.END)
        textarea_content = self.textarea.get(1.0, tk.END)
        resultadoSintactico = prueba_sintactica(textarea_content)
        resultadoLexico = errorLexico(textarea_content)

        salidaSintactico = ''
        salidaLexico = ''

        if resultadoLexico:
            for lex in resultadoLexico:
                salidaLexico += lex + "\n"

            self.console.insert(1.0,salidaLexico)
            self.console.insert(1.0,salidaSintactico)
        else:
            for sin in resultadoSintactico:
                salidaSintactico += sin + "\n"

            self.console.insert(1.0,salidaSintactico)

    def tony(self):
        self.console.delete(1.0,tk.END)
        textarea_content = self.textarea.get(1.0, tk.END)
        resultadoSintactico = prueba_sintactica(textarea_content)
        resultadoLexico = errorLexico(textarea_content)

        salidaSintactico = ''
        salidaLexico = ''

        if resultadoLexico:
            for lex in resultadoLexico:
                salidaLexico += lex + "\n"

            self.console.insert(1.0,salidaLexico)
            self.console.insert(1.0,salidaSintactico)
        else:
    
            self.console.insert(1.0,"Compilado satisfactoriamente")

    def show_tokens(self):
        box_title = "Tokens"
        textarea_content = self.textarea.get(1.0, tk.END)
        resultado = prueba(textarea_content)

        salida = ''

        for lex in resultado:
            salida += lex + "\n"
        messagebox.showinfo(box_title, salida)

    def cleanConsole(self):
        self.console.delete(1.0,tk.END)

    def identificadores(self):
        pass
    






    def bind_shortcuts(self):
        self.textarea.bind('<Control-n>', self.new_file)
        self.textarea.bind('<Control-o>', self.open_file)
        self.textarea.bind('<Control-s>', self.save)
        self.textarea.bind('<Control-S>', self.save_as)
        self.textarea.bind('<Key>', self.statusbar.update_status)
        


if __name__ == "__main__":
    master = tk.Tk()
    pt = PyText(master)
    master.mainloop()