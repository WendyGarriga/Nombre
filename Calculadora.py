from tkinter import Tk,Button,Text,END,re
class Calcu():
    def __init__(self):
        self.ventana1=Tk()
        self.pantalla=Text(self.ventana1, state="disabled", width=30, height=3, background="darkslategray", foreground="white", font=("Helvetica",15))
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=0, pady=0)
        self.ventana1.geometry("333x403")
        self.operacion=""
        boton1=self.crearBoton("C",escribir=False,ancho=13)
        boton1.grid(column=0,row=1, columnspan=2)
        boton2=self.crearBoton(0,ancho=13)
        boton2.grid(column=0,row=5,columnspan=2)
        boton3=self.crearBoton("%")
        boton4=self.crearBoton("/",fondo="orange")
        boton5=self.crearBoton(7)
        boton6=self.crearBoton(8)
        boton7=self.crearBoton(9)
        boton8=self.crearBoton("*",fondo="orange")
        boton9=self.crearBoton(4)
        boton10=self.crearBoton(5)
        boton11=self.crearBoton(6)
        boton12=self.crearBoton("-",fondo="orange")
        boton13=self.crearBoton(1)
        boton14=self.crearBoton(2)
        boton15=self.crearBoton(3)
        boton15.grid(row=2,column=2)
        boton16=self.crearBoton("+",fondo="orange")
        boton17=self.crearBoton(".")
        boton18=self.crearBoton("=",escribir=False,fondo="orange")
        botones=[boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8,boton9,boton10,boton11,boton12,boton13,boton14,boton15,boton16,boton17,boton18]
        contador=0
        for fila in range(1,5):
            for columna in range(4):
                botones[contador].grid(row=fila,column=columna)
                contador+=1
        botones[1].grid(row=5,column=0,columnspan=2)
        botones[16].grid(row=5,column=2)
        botones[17].grid(row=5,column=3)
        self.ventana1.mainloop()
    def crearBoton(self,valor,escribir=True,ancho=6,alto=2,fondo="gray94"):
        return Button(self.ventana1,text=valor,width=ancho,height=alto,font=("Helvetica",15,"bold"),command=lambda:self.click(valor,escribir),background=fondo)
    def click(self,texto,escribir):
        if not escribir:
            if texto == "=" and self.operacion !="":
                resultado=str(eval(self.operacion))
                self.operacion=""
                self.limpiarpantalla()
                self.mostrarenpantalla(resultado)
            elif texto == "C":
                self.operacion=""
                self.limpiarpantalla()
        else:
            self.operacion=self.operacion+str(texto)
            self.mostrarenpantalla(texto)
    def limpiarpantalla(self):
        self.pantalla.configure(state="normal")
        self.pantalla.delete("1.0",END)
        self.pantalla.configure(state="disabled")
    def mostrarenpantalla(self,valor):
        self.pantalla.configure(state="normal")
        self.pantalla.insert(END,valor)
        self.pantalla.configure(state="disabled")
Alfa=Calcu()