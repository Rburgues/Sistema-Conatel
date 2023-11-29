"""
BUSCADOR-FUNCIONARIOS
-Buscar Funcionarios
-Buscar en bd SQlite
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox 
#Python image Library
from PIL import ImageTk, Image
import sqlite3
import webbrowser


class Funcionario():
    db_name='database.db'
    def __init__(self, app_porteria):
        menubar=Menu(app_porteria)   
        app_porteria.title("PORTERIA VIVION-CONATEL")
        app_porteria.geometry("725x650")
        app_porteria.resizable(width=False, height=False)  # Hacer la ventana redimensionable
        app_porteria.config(bd=10,menu=menubar)
        
        "---------------------Menu---------------------------"
        Funcionarios=Menu(menubar,tearoff=0)
        Llaves=Menu(menubar,tearoff=0)
        Informacion=Menu(menubar,tearoff=0)
        menubar.add_cascade(label="Funcionarios",menu=Funcionarios)
        menubar.add_cascade(label="Llaves",menu=Llaves)
        menubar.add_cascade(label="Info",menu=Informacion)
        #Iconos
        self.img_registrar=PhotoImage(file="C:/xampp/htdocs/Python-Tkinter/SISTEMA DESKTOP/Imagenes/registrar.png")
        self.img_buscar=PhotoImage(file="C:/xampp/htdocs/Python-Tkinter/SISTEMA DESKTOP/Imagenes/buscar.png")
        self.img_informacion=PhotoImage(file="C:/xampp/htdocs/Python-Tkinter/SISTEMA DESKTOP/Imagenes/informacion.png")
        #Acciones de menu
        self.boton_registrar=Funcionarios.add_command(label=" Gestionar Funcionarios",command= self.widgets_crud,image=self.img_registrar,compound=LEFT)
        self.boton_buscar=Funcionarios.add_command(label=" Buscar Funcionarios",command=self.widgets_buscador,image=self.img_buscar,compound=LEFT)
        self.boton_registrar=Llaves.add_command(label=" Gestionar Llaves",command= self.widgets_crud_llaves,image=self.img_registrar,compound=LEFT)
        self.boton_buscar=Llaves.add_command(label=" Buscar Llaves",command=self.widgets_buscador_llaves,image=self.img_buscar,compound=LEFT)
        
        self.boton_informacion=Informacion.add_command(label=" Info del sistema",command=self.widgets_informacion,image=self.img_informacion,compound=LEFT)
        
        "---------------------Widgets---------------------------"
        #widgets crud
        self.Label_titulo_crud=LabelFrame(app_porteria)
        self.frame_logo_Funcionarios = LabelFrame(app_porteria)
        self.frame_registro = LabelFrame(app_porteria, text="Info del Funcionario",font=("Comic Sans", 10,"bold"),pady=5)
        self.frame_botones_registro=LabelFrame(app_porteria)
        self.frame_tabla_crud=LabelFrame(app_porteria)
         #widgets crud llaves
        self.Label_titulo_crud_llaves=LabelFrame(app_porteria)
        self.frame_logo_llaves = LabelFrame(app_porteria)
        self.frame_registro_llaves = LabelFrame(app_porteria, text="Registro de Llave",font=("Comic Sans", 10,"bold"),pady=5)
        self.frame_botones_registro_llaves=LabelFrame(app_porteria)
        self.frame_tabla_crud_llaves=LabelFrame(app_porteria)
        #widgets buscador
        self.Label_titulo_buscador=LabelFrame(app_porteria)
        self.frame_buscar_funcionario = LabelFrame(app_porteria, text="",font=("Comic Sans", 10,"bold"),pady=10)
        self.frame_boton_buscar=LabelFrame(app_porteria)
        self.frame_tabla_crud_buscar=LabelFrame(app_porteria)
        #widgets buscador llaves
        self.Label_titulo_buscador_llaves=LabelFrame(app_porteria)
        self.frame_buscar_llaves = LabelFrame(app_porteria, text="",font=("Comic Sans", 10,"bold"),pady=10)
        self.frame_boton_buscar_llaves=LabelFrame(app_porteria)
        self.frame_tabla_crud_buscar_llaves=LabelFrame(app_porteria)

        
        #widgets informacion
        self.Label_informacion = LabelFrame(app_porteria)

        #Pantalla inicial
        self.widgets_crud()

    def widgets_crud(self):
        self.Label_titulo_crud.config(bd=0)
        self.Label_titulo_crud.grid(row=0,column=0,padx=5,pady=5)
        "--------------- Titulo --------------------"
        self.titulo_crud= Label(self.Label_titulo_crud, text="Gestion de Funcionarios",fg="black",font=("Comic Sans", 17,"bold"))
        self.titulo_crud.grid(row=0,column=0)
        
        "--------------- Logos Funcionarios --------------------"
        self.frame_logo_Funcionarios.config(bd=0)
        self.frame_logo_Funcionarios.grid(row=1,column=0,padx=5,pady=5)

        #Logo conatel
        imagen_arduino=Image.open("C:/xampp/htdocs/Python-Tkinter/SISTEMA DESKTOP/Imagenes/conatel.png")
        nueva_imagen=imagen_arduino.resize((120,20))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.frame_logo_Funcionarios, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=0,padx=15,pady=5)

        #Logo vivion
        imagen_nodemcu=Image.open("C:/xampp/htdocs/Python-Tkinter/SISTEMA DESKTOP/Imagenes/vivion.png")
        nueva_imagen=imagen_nodemcu.resize((120,20))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.frame_logo_Funcionarios, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=1,padx=15,pady=5)
        
        "--------------- Frame marco --------------------"
        self.frame_registro.config(bd=2)
        self.frame_registro.grid(row=2,column=0,padx=5,pady=5)

        "--------------- Formulario --------------------"
        label_nombre=Label(self.frame_registro,text="Nombre: ",font=("Comic Sans", 11,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.nombre=Entry(self.frame_registro,width=25,font="Comic-Sans 11")
        self.nombre.grid(row=0, column=1, padx=5, pady=8)
        
        label_sector=Label(self.frame_registro,text="Sector: ",font=("Comic Sans", 11,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        self.sector=Entry(self.frame_registro,width=25,font="Comic-Sans 11")
        self.sector.grid(row=1, column=1, padx=5, pady=8)
        
        label_empresa=Label(self.frame_registro,text="Empresa: ",font=("Comic Sans", 11,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=9)
        self.combo_empresa=ttk.Combobox(self.frame_registro,values=["Conatel","Vivion"], width=22,state="readonly",font="Comic-Sans 11")
        self.combo_empresa.current(0)
        self.combo_empresa.grid(row=2,column=1,padx=5,pady=0)

        label_telefono=Label(self.frame_registro,text="Teléfono: ",font=("Comic Sans", 11,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=8)
        self.telefono=Entry(self.frame_registro,width=25,font="Comic-Sans 11")
        self.telefono.grid(row=0, column=3, padx=5, pady=8)

        label_email=Label(self.frame_registro,text="Email: ",font=("Comic Sans", 11,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=8)
        self.email=Entry(self.frame_registro,width=25,font="Comic-Sans 11")
        self.email.grid(row=1, column=3, padx=5, pady=8)

        
        
        "--------------- Frame botones --------------------"
        self.frame_botones_registro.config(bd=0)
        self.frame_botones_registro.grid(row=3,column=0,padx=5,pady=5)

        "--------------- Botones --------------------"
        boton_registrar=Button(self.frame_botones_registro,text="REGISTRAR",command=self.Agregar_Funcionario,height=1,width=10,bg="green",fg="white",font=("Comic Sans", 9,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_editar=Button(self.frame_botones_registro,text="EDITAR",command=self.Editar_Funcionario ,height=1,width=10,bg="gray",fg="white",font=("Comic Sans", 9,"bold")).grid(row=0, column=2, padx=10, pady=15)
        boton_eliminar=Button(self.frame_botones_registro,text="ELIMINAR",command=self.Eliminar_Funcionario,height=1,width=10,bg="red",fg="white",font=("Comic Sans", 9,"bold")).grid(row=0, column=3, padx=10, pady=15)
        
        "--------------- Tabla --------------------"
        self.frame_tabla_crud.config(bd=2)
        self.frame_tabla_crud.grid(row=5,column=0,padx=5,pady=5)

        self.tree=ttk.Treeview(self.frame_tabla_crud,height=14, columns=("columna1","columna2","columna3","columna4", "columna5"))
        
        self.tree.heading("#0",text='', anchor=CENTER)
        self.tree.column("#0", width=1, minwidth=1, stretch=NO)

        self.tree.heading("columna1",text='Nombre', anchor=CENTER)
        self.tree.column("columna1", width=160, minwidth=160, stretch=NO)

        self.tree.heading("columna2",text='Sector', anchor=CENTER)
        self.tree.column("columna2", width=130, minwidth=130, stretch=NO)
        
        self.tree.heading("columna3",text='Empresa', anchor=CENTER)
        self.tree.column("columna3", width=80, anchor=CENTER, minwidth=80, stretch=NO)
                
        self.tree.heading("columna4",text='Telefono', anchor=CENTER)
        self.tree.column("columna4", width=90, anchor=CENTER, minwidth=90, stretch=NO)
        
        self.tree.heading("columna5",text='Email', anchor=CENTER)
        self.tree.column("columna5", width=230, minwidth=230, stretch=NO)

        
        self.tree.grid(row=0,column=0,sticky=E)
        self.inicializar_estilos_de_fuente()
        self.Obtener_Funcionarios()
        
        #REMOVER OTROS WIDGETS
        self.widgets_buscador_remove()
        self.widgets_buscador_llaves_remove()
        self.widgets_crud_llaves_remove()
        self.Label_informacion.grid_remove()

    def widgets_crud_llaves(self):
        self.Label_titulo_crud_llaves.config(bd=0)
        self.Label_titulo_crud_llaves.grid(row=0,column=0,padx=250,pady=5)
        "--------------- Titulo --------------------"
        self.titulo_crud_llaves= Label(self.Label_titulo_crud_llaves, text="Gestion de Llaves",fg="black",font=("Comic Sans", 17,"bold"))
        self.titulo_crud_llaves.grid(row=0,column=0)
        
        "--------------- Logos Funcionarios --------------------"
        self.frame_logo_llaves.config(bd=0)
        self.frame_logo_llaves.grid(row=1,column=0,padx=5,pady=5)

        #Logo conatel
        imagen_arduino=Image.open("C:/xampp/htdocs/Python-Tkinter/SISTEMA DESKTOP/Imagenes/conatel.png")
        nueva_imagen=imagen_arduino.resize((120,20))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.frame_logo_llaves, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=0,padx=15,pady=5)

        #Logo vivion
        imagen_nodemcu=Image.open("C:/xampp/htdocs/Python-Tkinter/SISTEMA DESKTOP/Imagenes/vivion.png")
        nueva_imagen=imagen_nodemcu.resize((120,20))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.frame_logo_llaves, image= render)
        label_imagen.image=render
        label_imagen.grid(row=0, column=1,padx=15,pady=5)
        
        "--------------- Frame marco --------------------"
        self.frame_registro_llaves.config(bd=2)
        self.frame_registro_llaves.grid(row=2,column=0,padx=5,pady=5)

        "--------------- Formulario --------------------"
        label_numero=Label(self.frame_registro_llaves,text="Numero: ",font=("Comic Sans", 11,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        self.numero=Entry(self.frame_registro_llaves,width=25,font=("Comic Sans", 11))
        self.numero.grid(row=0, column=1, padx=5, pady=8)
        
        label_color=Label(self.frame_registro_llaves,text="Color: ",font=("Comic Sans", 11,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        self.color=Entry(self.frame_registro_llaves,width=25,font=("Comic Sans", 11))
        self.color.grid(row=1, column=1, padx=5, pady=8)
        
        label_sector=Label(self.frame_registro_llaves,text="Sector: ",font=("Comic Sans", 11,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=9)
        self.sector=Entry(self.frame_registro_llaves,width=25,font=("Comic Sans", 11))
        self.sector.grid(row=2, column=1, padx=5, pady=8)
        
        "--------------- Frame botones --------------------"
        self.frame_botones_registro_llaves.config(bd=0)
        self.frame_botones_registro_llaves.grid(row=3,column=0,padx=5,pady=5)

        "--------------- Botones --------------------"
        boton_registrar=Button(self.frame_botones_registro_llaves,text="REGISTRAR",command=self.Agregar_Llave,height=1,width=10,bg="green",fg="white",font=("Comic Sans", 9,"bold")).grid(row=0, column=1, padx=10, pady=15)
        boton_editar=Button(self.frame_botones_registro_llaves,text="EDITAR",command=self.Editar_Llave ,height=1,width=10,bg="gray",fg="white",font=("Comic Sans", 9,"bold")).grid(row=0, column=2, padx=10, pady=15)
        boton_eliminar=Button(self.frame_botones_registro_llaves,text="ELIMINAR",command=self.Eliminar_Llave,height=1,width=10,bg="red",fg="white",font=("Comic Sans", 9,"bold")).grid(row=0, column=3, padx=10, pady=15)
        
        "--------------- Tabla --------------------"
        self.frame_tabla_crud_llaves.config(bd=2)
        self.frame_tabla_crud_llaves.grid(row=5,column=0,padx=5,pady=5)

        self.tree=ttk.Treeview(self.frame_tabla_crud_llaves,height=13, columns=("columna1","columna2","columna3"))
        
        self.tree.heading("#0",text='', anchor=CENTER)
        self.tree.column("#0", width=1, minwidth=1, stretch=NO)

        self.tree.heading("columna1",text='Numero', anchor=CENTER)
        self.tree.column("columna1", width=80, anchor=CENTER, minwidth=80, stretch=NO)

        self.tree.heading("columna2",text='Color', anchor=CENTER)
        self.tree.column("columna2", width=80, anchor=CENTER, minwidth=80, stretch=NO)
        
        self.tree.heading("columna3",text='Sector', anchor=CENTER)
        self.tree.column("columna3", width=220, anchor=CENTER, minwidth=220, stretch=NO)

        
        self.tree.grid(row=0,column=0,sticky=E)
        self.inicializar_estilos_de_fuente()
        self.Obtener_Llaves()
        
        #REMOVER OTROS WIDGETS
        self.widgets_buscador_remove()
        self.widgets_crud_remove()
        self.widgets_buscador_llaves_remove()
        self.Label_informacion.grid_remove()


    def widgets_buscador(self):
        self.Label_titulo_buscador.config(bd=0)
        self.Label_titulo_buscador.grid(row=0,column=0,padx=5,pady=5)

        "--------------- Titulo --------------------"
        self.titulo_buscador= Label(self.Label_titulo_buscador, text="Buscador de Funcionarios",fg="black",font=("Comic Sans", 17,"bold"))
        self.titulo_buscador.grid(row=0,column=0)
        
        "--------------- Frame buscar --------------------"
        self.frame_buscar_funcionario.config(bd=2)
        self.frame_buscar_funcionario.grid(row=2,column=0,padx=5,pady=5)
        
        "--------------- Formulario Buscar--------------------"
        
        label_sector_sector=Label(self.frame_buscar_funcionario,text="Nombre del Funcionario: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=5)
        self.sector_nombre=Entry(self.frame_buscar_funcionario,width=25)
        self.sector_nombre.focus()
        self.sector_nombre.grid(row=0, column=3, padx=10, pady=5)

        "--------------- Frame marco --------------------"
        self.frame_boton_buscar.config(bd=0)
        self.frame_boton_buscar.grid(row=3,column=0,padx=5,pady=5)

        "--------------- Boton 1 --------------------"
        self.boton_listar=Button(self.frame_boton_buscar,text="VER TODOS",command=self.Listar_Funcionarios,height=1,width=15,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_listar.grid(row=0,column=0,padx=5,pady=5)
        "--------------- Boton --------------------"
        self.boton_buscar=Button(self.frame_boton_buscar,text="BUSCAR",command=self.Buscar_Funcionarios,height=1,width=15,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_buscar.grid(row=0,column=1,padx=5,pady=5)

        "--------------- Tabla --------------------"
        self.frame_tabla_crud_buscar.config(bd=2)
        self.frame_tabla_crud_buscar.grid(row=5,column=0,padx=5,pady=5)

        self.tree=ttk.Treeview(self.frame_tabla_crud_buscar,height=22, columns=("columna1","columna2","columna3","columna4", "columna5"))
        
        self.tree.heading("#0",text='', anchor=CENTER)
        self.tree.column("#0", width=1, minwidth=1, stretch=NO)

        self.tree.heading("columna1",text='Nombre', anchor=CENTER)
        self.tree.column("columna1", width=160, minwidth=160, stretch=NO)

        self.tree.heading("columna2",text='Sector', anchor=CENTER)
        self.tree.column("columna2", width=130, minwidth=130, stretch=NO)
        
        self.tree.heading("columna3",text='Empresa', anchor=CENTER)
        self.tree.column("columna3", width=80, anchor=CENTER, minwidth=80, stretch=NO)
                
        self.tree.heading("columna4",text='Telefono', anchor=CENTER)
        self.tree.column("columna4", width=90, anchor=CENTER, minwidth=90, stretch=NO)
        
        self.tree.heading("columna5",text='Email', anchor=CENTER)
        self.tree.column("columna5", width=230, minwidth=230, stretch=NO)

        
        self.tree.grid(row=0,column=0,sticky=E)
        self.inicializar_estilos_de_fuente()
        self.Obtener_Funcionarios()
        
        self.tree.delete(*self.tree.get_children())
        self.Obtener_Funcionarios()

        #REMOVER OTROS WIDGETS
        self.widgets_crud_remove()
        self.widgets_crud_llaves_remove()
        self.widgets_buscador_llaves_remove()
        self.Label_informacion.grid_remove()

    def widgets_buscador_llaves(self):
        self.Label_titulo_buscador_llaves.config(bd=0)
        self.Label_titulo_buscador_llaves.grid(row=0,column=0,padx=250,pady=5)

        "--------------- Titulo --------------------"
        self.titulo_buscador_llaves= Label(self.Label_titulo_buscador_llaves, text="Buscador de Llaves",fg="black",font=("Comic Sans", 17,"bold"))
        self.titulo_buscador_llaves.grid(row=0,column=0)
        
        "--------------- Frame buscar --------------------"
        self.frame_buscar_llaves.config(bd=2)
        self.frame_buscar_llaves.grid(row=2,column=0,padx=5,pady=5)
        
        "--------------- Formulario Buscar--------------------"
        
        label_sector_sector=Label(self.frame_buscar_llaves,text="Nombre / Número de Llave: ",font=("Comic Sans", 11,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=5)
        self.sector_llave=Entry(self.frame_buscar_llaves,width=25,font=("Comic Sans", 11))
        self.sector_llave.focus()
        self.sector_llave.grid(row=0, column=3, padx=10, pady=5)

        "--------------- Frame marco --------------------"
        self.frame_boton_buscar_llaves.config(bd=0)
        self.frame_boton_buscar_llaves.grid(row=3,column=0,padx=5,pady=5)

        "--------------- Boton 1 --------------------"
        self.boton_listar=Button(self.frame_boton_buscar_llaves,text="VER TODOS",command=self.Listar_Llaves,height=1,width=15,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_listar.grid(row=0,column=0,padx=5,pady=5)
        "--------------- Boton --------------------"
        self.boton_buscar_llaves=Button(self.frame_boton_buscar_llaves,text="BUSCAR",command=self.Buscar_Llaves,height=1,width=15,bg="black",fg="white",font=("Comic Sans", 10,"bold"))
        self.boton_buscar_llaves.grid(row=0,column=1,padx=5,pady=5)

        "--------------- Tabla --------------------"
        self.frame_tabla_crud_buscar_llaves.config(bd=2)
        self.frame_tabla_crud_buscar_llaves.grid(row=5,column=0,padx=5,pady=5)

        self.tree=ttk.Treeview(self.frame_tabla_crud_buscar_llaves, height=21, columns=("columna1","columna2","columna3"))
        
        self.tree.heading("#0",text='', anchor=CENTER)
        self.tree.column("#0", width=0, stretch=NO)

        self.tree.heading("columna1",text='Numero', anchor=CENTER)
        self.tree.column("columna1", width=80, anchor=CENTER, minwidth=80, stretch=NO)

        self.tree.heading("columna2",text='Color', anchor=CENTER)
        self.tree.column("columna2", width=80, anchor=CENTER, minwidth=80, stretch=NO)
        
        self.tree.heading("columna3",text='Sector', anchor=CENTER)
        self.tree.column("columna3", width=220, anchor=CENTER, minwidth=220, stretch=NO)

        
        self.tree.grid(row=0,column=0,sticky=E)
        self.inicializar_estilos_de_fuente()
        self.Obtener_Llaves()
        
        self.tree.delete(*self.tree.get_children())
        self.Obtener_Llaves()

        #REMOVER OTROS WIDGETS
        self.widgets_crud_remove()
        self.widgets_crud_llaves_remove()
        self.widgets_buscador_remove()
        self.Label_informacion.grid_remove()

        self.tree.delete(*self.tree.get_children())
        self.Obtener_Llaves()

        #REMOVER OTROS WIDGETS
        self.widgets_crud_remove() 
        self.widgets_crud_llaves_remove()
        self.widgets_buscador_remove()
        self.Label_informacion.grid_remove()
       
        
    def widgets_crud_remove(self):
        self.Label_titulo_crud.grid_remove()
        self.frame_logo_Funcionarios.grid_remove()
        self.frame_registro.grid_remove()
        self.frame_botones_registro.grid_remove()
        self.frame_tabla_crud.grid_remove()

    def widgets_crud_llaves_remove(self):
        self.Label_titulo_crud_llaves.grid_remove()
        self.frame_logo_llaves.grid_remove()
        self.frame_registro_llaves.grid_remove()
        self.frame_botones_registro_llaves.grid_remove()
        self.frame_tabla_crud_llaves.grid_remove()

    def widgets_buscador_remove(self):
        self.Label_titulo_buscador.grid_remove()
        self.frame_buscar_funcionario.grid_remove()
        self.frame_boton_buscar.grid_remove()
        self.frame_tabla_crud_buscar.grid_remove()

    def widgets_buscador_llaves_remove(self):
        self.Label_titulo_buscador_llaves.grid_remove()
        self.frame_buscar_llaves.grid_remove()
        self.frame_boton_buscar_llaves.grid_remove()
        self.frame_tabla_crud_buscar_llaves.grid_remove()


    def widgets_informacion(self):

        self.Label_informacion.config(bd=0)
        self.Label_informacion.grid(row=0,column=0)

        
        "--------------- Titulo --------------------"
        self.Label_titulo = Label(self.Label_informacion,text="APP PORTERIA",fg="black",font=("Comic Sans", 25,"bold"),padx=137,pady=20)
        self.Label_titulo.grid(row=0,column=0)

        "--------------- Logos imagenes--------------------"
        #Logo 
        imagen_arduino=Image.open("C:/xampp/htdocs/Python-Tkinter/SISTEMA DESKTOP/Imagenes/app_logo_2.png")
        nueva_imagen=imagen_arduino.resize((170,170))
        render=ImageTk.PhotoImage(nueva_imagen)
        label_imagen= Label(self.Label_informacion, image= render)
        label_imagen.image=render
        label_imagen.grid(row=1,column=0,padx=10,pady=0)

        "--------------- opciones--------------------"
        self.Label_titulo = Label(self.Label_informacion,text="-GESTION DE FUNCIONARIOS-",fg="black",font=("Comic Sans", 15,"bold"))
        self.Label_titulo.grid(row=2,column=0,sticky=W,padx=220,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="-GESTION DE LLAVES-",fg="black",font=("Comic Sans", 15,"bold"))
        self.Label_titulo.grid(row=3,column=0,sticky=W,padx=255,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="-BUSQUEDA DE DATOS-",fg="black",font=("Comic Sans", 15,"bold"))
        self.Label_titulo.grid(row=4,column=0,sticky=W,padx=250,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="",fg="black",font=("Comic Sans",10,"bold"))
        self.Label_titulo.grid(row=5,column=0,pady=40)

        self.Label_titulo = Button(self.Label_informacion,command=self.abrir_web, text="Visita mi sitio web",fg="black", foreground="blue", font=("Comic Sans",10,"bold"), )
        self.Label_titulo.grid(row=6,column=0,pady=10)

        self.Label_titulo = Label(self.Label_informacion,text="Creado por Richard Burgues - 2023",fg="black",font=("Comic Sans",10,"bold"))
        self.Label_titulo.grid(row=7,column=0,pady=20)

        #Remove
        self.widgets_buscador_remove()
        self.widgets_crud_remove()
        self.widgets_buscador_llaves_remove()
        self.widgets_crud_llaves_remove()

    
    "--------------- CRUD --------------------"               
    def Obtener_Funcionarios(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        query = 'SELECT * FROM Funcionarios ORDER BY Nombre DESC'
        db_rows = self.Ejecutar_consulta(query)

        for row in db_rows:
            # Insertar datos en la fila y aplicar estilo a todas las columnas
            item_id = row[5]
            self.tree.insert("", 0, text=item_id, values=(row[1], row[2], row[3], row[4], row[5]), tags="fuente_comun")

    def inicializar_estilos_de_fuente(self):
        # Configurar el estilo de fuente común para todas las columnas
        self.tree.tag_configure("fuente_comun", font=("Comic-Sans", 11))

    def Obtener_Llaves(self):
        records=self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        query='SELECT * FROM Llaves ORDER BY Numero desc'
        db_rows=self.Ejecutar_consulta(query)
        for row in db_rows:
            self.tree.insert("",0,text=row[3],values=(row[1],row[2],row[3]),tags="fuente_comun")
            
    def Agregar_Funcionario(self):
        if self.Validar_formulario_completo() and self.Validar_registrar() and self.Validar_campo_telefono():
            query='INSERT INTO Funcionarios VALUES(NULL, ?, ?, ?, ?, ?)'
            parameters = (self.nombre.get(),self.sector.get(),self.combo_empresa.get(),self.telefono.get(),self.email.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Funcionario registrado: {self.nombre.get()}')
            print('REGISTRADO')
            self.Limpiar_formulario()
        self.Obtener_Funcionarios()
    
    def Agregar_Llave(self):
        if self.Validar_formulario_llaves() and self.Validar_registrar_llave() and self.Validar_campo_numero_llaves():
            query='INSERT INTO Llaves VALUES(NULL, ?, ?, ?)'
            parameters = (self.numero.get(),self.color.get(),self.sector.get())
            self.Ejecutar_consulta(query, parameters)
            messagebox.showinfo("REGISTRO EXITOSO", f'Llave Registrada: {self.sector.get()}')
            print('REGISTRADO')
            self.Limpiar_formulario_llaves()
        self.Obtener_Llaves()
    
    def Eliminar_Funcionario(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            messagebox.showerror("ERROR","Porfavor selecciona un funcionario") 
            return
        dato=self.tree.item(self.tree.selection())['text']
        nombre=self.tree.item(self.tree.selection())['values'][0]
        query="DELETE FROM Funcionarios WHERE Email = ?"
        respuesta=messagebox.askquestion("ADVERTENCIA",f"¿Seguro que desea eliminar el Funcionario: {nombre}?")
        if respuesta == 'yes':
            self.Ejecutar_consulta(query,(dato,))
            self.Obtener_Funcionarios()
            messagebox.showinfo('EXITO',f'Funcionario eliminado: {nombre}')
        else:
           return

    def Eliminar_Llave(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            messagebox.showerror("ERROR","Porfavor selecciona una Llave") 
            return
        dato=self.tree.item(self.tree.selection())['text']
        sector=self.tree.item(self.tree.selection())['values'][0]
        query="DELETE FROM Llaves WHERE sector = ?"
        respuesta=messagebox.askquestion("ADVERTENCIA",f"¿Seguro que desea eliminar la llave: {sector}?")
        if respuesta == 'yes':
            self.Ejecutar_consulta(query,(dato,))
            self.Obtener_Llaves()
            messagebox.showinfo('EXITO',f'Llave eliminada: {sector}')
        else:
            return
     
    def Editar_Funcionario(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            messagebox.showerror("ERROR","Primero selecciona un funcionario") 
            return
        nombre=self.tree.item(self.tree.selection())['values'][0]
        sector=self.tree.item(self.tree.selection())['values'][1]
        empresa=self.tree.item(self.tree.selection())['values'][2]
        telefono=self.tree.item(self.tree.selection())['values'][3]
        email=self.tree.item(self.tree.selection())['text']
        
        self.Ventana_editar = Toplevel()
        self.Ventana_editar.title('Editar Funcionario')
        self.Ventana_editar.resizable(0,0)
        
        
        #Valores ventana editar
        label_sector=Label(self.Ventana_editar,text="Sector: ",font=("Comic Sans", 11,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        nuevo_sector=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=sector),width=25,font=("Comic Sans", 11))
        nuevo_sector.grid(row=1, column=1, padx=5, pady=8)
        
        label_nombre=Label(self.Ventana_editar,text="Nombre: ",font=("Comic Sans", 11,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        nuevo_nombre=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=nombre),width=25,font=("Comic Sans", 11))
        nuevo_nombre.grid(row=0, column=1, padx=5, pady=8)
    
        label_empresa=Label(self.Ventana_editar,text="Empresa: ",font=("Comic Sans", 11,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=9)
        nuevo_combo_empresa=ttk.Combobox(self.Ventana_editar,values=["Conatel","Vivion"], width=22,state="readonly",font=("Comic Sans", 11))
        nuevo_combo_empresa.set(empresa)
        nuevo_combo_empresa.grid(row=2,column=1,padx=5,pady=0)

        label_telefono=Label(self.Ventana_editar,text="Teléfono: ",font=("Comic Sans", 11,"bold")).grid(row=0,column=2,sticky='s',padx=5,pady=8)
        nuevo_telefono=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=telefono),width=25,font=("Comic Sans", 11))
        nuevo_telefono.grid(row=0, column=3, padx=5, pady=8)

        label_email=Label(self.Ventana_editar,text="Email: ",font=("Comic Sans", 11,"bold")).grid(row=1,column=2,sticky='s',padx=5,pady=8)
        nuevo_email=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=email),width=25,font=("Comic Sans", 11))
        nuevo_email.grid(row=1, column=3, padx=5, pady=8)
        
        boton_actualizar=Button(self.Ventana_editar,text="ACTUALIZAR",command= lambda: self.Actualizar(nuevo_sector.get(),nuevo_nombre.get(),nuevo_combo_empresa.get(),nuevo_telefono.get(),nuevo_email.get(),sector,nombre),height=1,width=15,bg="green",fg="white",font=("Comic Sans", 9,"bold"))
        boton_actualizar.grid(row=3, column=3,columnspan=2, padx=25, pady=15)
        
        self.Ventana_editar.mainloop()      

    def Editar_Llave(self):
        try:
            self.tree.item(self.tree.selection())['text'][0]
        except IndexError as e:
            messagebox.showerror("ERROR","Primero selecciona una Llave") 
            return
        numero=self.tree.item(self.tree.selection())['values'][0]
        color=self.tree.item(self.tree.selection())['values'][1]
        sector=self.tree.item(self.tree.selection())['values'][2]
        
        self.Ventana_editar = Toplevel()
        self.Ventana_editar.title('Editar Llave')
        self.Ventana_editar.resizable(0,0)
        
        
        #Valores ventana editar
                
        label_numero=Label(self.Ventana_editar,text="Numero: ",font=("Comic Sans", 10,"bold")).grid(row=0,column=0,sticky='s',padx=5,pady=8)
        nuevo_numero=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=numero),width=25,font="Comic-Sans 11")
        nuevo_numero.grid(row=0, column=1, padx=5, pady=8)
    
        label_color=Label(self.Ventana_editar,text="Color: ",font=("Comic Sans", 10,"bold")).grid(row=1,column=0,sticky='s',padx=5,pady=8)
        nuevo_color=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=color),width=25, font="Comic-Sans 11")
        nuevo_color.grid(row=1, column=1, padx=5, pady=8)

        label_sector=Label(self.Ventana_editar,text="Sector: ",font=("Comic Sans", 10,"bold")).grid(row=2,column=0,sticky='s',padx=5,pady=8)
        nuevo_sector=Entry(self.Ventana_editar,textvariable=StringVar(self.Ventana_editar,value=sector),width=25, font="Comic-Sans 11")
        nuevo_sector.grid(row=2, column=1, padx=5, pady=8)
        
        boton_actualizar=Button(self.Ventana_editar,text="ACTUALIZAR",command= lambda: self.Actualizar_Llave(nuevo_numero.get(),nuevo_color.get(),nuevo_sector.get(),sector),height=1,width=15,bg="green",fg="white",font=("Comic Sans", 9,"bold"))
        boton_actualizar.grid(row=3, column=3,columnspan=2, padx=25, pady=15)
        
        self.Ventana_editar.mainloop()    
        
    def Actualizar(self,nuevo_sector,nuevo_nombre,nuevo_combo_empresa,nuevo_telefono,nuevo_email,sector,nombre):
        
            query='UPDATE Funcionarios SET sector = ?, Nombre = ?, empresa = ?, telefono =?, email=? WHERE sector = ? AND Nombre =?'
            parameters=(nuevo_sector,nuevo_nombre,nuevo_combo_empresa,nuevo_telefono,nuevo_email,sector,nombre)
            self.Ejecutar_consulta(query,parameters)
            messagebox.showinfo('EXITO',f'Funcionario actualizado:{nuevo_nombre}')
            self.Ventana_editar.destroy()
            self.Obtener_Funcionarios()
        
    
    def Actualizar_Llave(self,nuevo_numero,nuevo_color,nuevo_sector,sector):
        query='UPDATE Llaves SET numero = ?, color = ?, sector =? WHERE sector = ?'
        parameters=(nuevo_numero,nuevo_color,nuevo_sector,sector)
        self.Ejecutar_consulta(query,parameters)
        messagebox.showinfo('EXITO',f'Llave Actualizada:{nuevo_sector}')
        self.Ventana_editar.destroy()
        self.Obtener_Llaves()

    def Buscar_Funcionarios(self):
        if(self.Validar_busqueda()):
            #Obtener todos los elementos con get_children(), que retorna una tupla de ID.
            records=self.tree.get_children()
            for element in records:
                self.tree.delete(element)

                if (self.sector_nombre.get()=='Codigo'):
                    query=("SELECT * FROM Funcionarios WHERE Codigo LIKE ?") 
                    parameters=(self.codigo_nombre.get()+"%")
                    db_rows=self.Ejecutar_consulta(query,(parameters,))
                    for row in db_rows:
                        self.tree.insert("",0, text=row[1],values=(row[1],row[2],row[3],row[4],row[5]), tags="fuente_comun")
                        self.inicializar_estilos_de_fuente()
                    if(list(self.tree.get_children())==[]):
                        messagebox.showerror("ERROR","Funcionario no encontrado")
            else:
                query=("SELECT * FROM Funcionarios WHERE Nombre LIKE ?")
                parameters=("%"+self.sector_nombre.get()+"%")
                db_rows=self.Ejecutar_consulta(query,(parameters,))
                for row in db_rows:
                    self.tree.insert("",0, text=row[1],values=(row[1],row[2],row[3],row[4],row[5]), tags="fuente_comun")
                    self.inicializar_estilos_de_fuente()
                if(list(self.tree.get_children())==[]):
                    messagebox.showerror("ERROR","Funcionario no encontrado")
                    
    def Buscar_Llaves(self):
        if(self.Validar_busqueda_llaves()):
            records=self.tree.get_children()
            for element in records:
                self.tree.delete(element)

            search_term = self.sector_llave.get()

            # Verificar si el término de búsqueda es un número
            if search_term.isdigit():
                # Es un número
                query = "SELECT * FROM Llaves WHERE Numero LIKE ?"
                parameters = search_term + "%"
                db_rows=self.Ejecutar_consulta(query,(parameters,))
                for row in db_rows:
                    self.tree.insert("",0, text=row[1],values=(row[1],row[2],row[3]), tags="fuente_comun")
                    self.inicializar_estilos_de_fuente()
                if(list(self.tree.get_children())==[]):
                    messagebox.showerror("ERROR","Llave no encontrada")
            else:
                # No es un número, asumimos que es una cadena
                query=("SELECT * FROM Llaves WHERE Sector LIKE ?")
                parameters=("%"+self.sector_llave.get()+"%")
                db_rows=self.Ejecutar_consulta(query,(parameters,))
                for row in db_rows:
                    self.tree.insert("",0, text=row[3],values=(row[1],row[2],row[3]), tags="fuente_comun")
                    self.inicializar_estilos_de_fuente()
                if(list(self.tree.get_children())==[]):
                    messagebox.showerror("ERROR","Llave no encontrada")

    def Listar_Funcionarios(self):
            self.sector_nombre.children 
            records=self.tree.get_children()
            for element in records:
                self.tree.delete(element)
                        
            else:
                query=("SELECT * FROM Funcionarios ORDER BY Nombre desc")
                db_rows=self.Ejecutar_consulta(query)
                for row in db_rows:

                    self.tree.insert("",0, text=row[1],values=(row[1],row[2],row[3],row[4],row[5]),tags="fuente_comun")
                    self.inicializar_estilos_de_fuente()
                self.Limpiar_busqueda_funcionarios()
                

    def Listar_Llaves(self):
            self.sector_llave.children 
            records=self.tree.get_children()
            for element in records:
                self.tree.delete(element)
                        
            else:
                query=("SELECT * FROM Llaves ORDER BY Numero desc")
                db_rows=self.Ejecutar_consulta(query)
                for row in db_rows:
                    self.tree.insert("",0, text=row[1],values=(row[1],row[2],row[3]),tags="fuente_comun")
                self.Limpiar_busqueda_llaves()
                self.inicializar_estilos_de_fuente()

    "--------------- OTRAS FUNCIONES --------------------"
    def Ejecutar_consulta(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as conexion:
            cursor=conexion.cursor()
            result=cursor.execute(query,parameters)           
            conexion.commit()
        return result   
          
    def Validar_formulario_completo(self):
        if len(self.sector.get()) !=0 and len(self.nombre.get()) !=0 and len(self.combo_empresa.get()) !=0 and len(self.telefono.get()) !=0 and len(self.email.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR", "Complete todos los campos del formulario") 
             
    def Validar_campo_telefono(self):
        
        x = self.telefono.get()
        if (x.isdigit()):
            return True
        else:
             messagebox.showerror("ERROR", "El campo Teléfono debe ser numerico")     

    def Validar_formulario_llaves(self):      
        
        if len(self.numero.get()) !=0 and len(self.color.get()) !=0 and len(self.sector.get()) !=0:
            return True
        else:
             messagebox.showerror("ERROR", "Complete todos los campos del formulario") 

    def Validar_campo_numero_llaves(self):
        
        x = self.numero.get()
        if (x.isdigit()):
            return True
        else:
             messagebox.showerror("ERROR", "El campo Numero debe ser numerico")        
        
    
    def Validar_busqueda(self):
        if len(self.sector_nombre.get()) !=0:
            return True
        else:
             self.tree.delete(*self.tree.get_children())
             messagebox.showerror("ERROR", "Complete todos los campos para la busqueda") 
             self.Obtener_Funcionarios()

    def Validar_busqueda_llaves(self):
        if len(self.sector_llave.get()) !=0:
            return True
        else:
             self.tree.delete(*self.tree.get_children())
             messagebox.showerror("ERROR", "Complete el campo de busqueda") 
             self.Obtener_Llaves()

    def Limpiar_formulario(self):
        self.sector.delete(0, END)
        self.nombre.delete(0, END)
        self.telefono.delete(0, END)
        self.email.delete(0, END)
    
    def Limpiar_formulario_llaves(self):
        self.numero.delete(0, END)
        self.color.delete(0, END)
        self.sector.delete(0, END)

    def Limpiar_busqueda_funcionarios(self):
        self.sector_nombre.delete(0, END)

    def Limpiar_busqueda_llaves(self):
        self.sector_llave.delete(0, END)

    def Validar_registrar(self):
        parameters= self.email.get()
        query="SELECT * FROM Funcionarios WHERE Email = ?"
        dato = self.Ejecutar_consulta(query,(parameters,))
        if (dato.fetchall() == []):
            return True
        else:
            messagebox.showerror("ERROR EN REGISTRO", "Ya existe un funcionario con ese email")

    def Validar_registrar_llave(self):
        parameters= self.sector.get()
        query="SELECT * FROM Llaves WHERE Sector = ?"
        dato = self.Ejecutar_consulta(query,(parameters,))
        if (dato.fetchall() == []):
            return True
        else:
            messagebox.showerror("ERROR EN REGISTRO", "Ya existe una llave en ese Sector")

    def abrir_web(self):
        webbrowser.open_new('https://richardburgues.com/')


if __name__ == '__main__':
    app_porteria=Tk()
    label_crud=Label(app_porteria)
    application=Funcionario(app_porteria)
    app_porteria.mainloop()
