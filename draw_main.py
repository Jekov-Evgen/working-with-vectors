from tkinter import ttk
from tkinter import *
from calculation_multiplication_by_calar import DrawVectorSC
from add_vector import DrawVectorAdd

class MainWindow:
    def __init__(self) -> None:
        pass
    
    def draw_main(self):
        root = Tk()
        root.title("Вектора")
        
        frm = ttk.Frame(root, padding=10)
        frm.grid
        
        ttk.Label(text="Введите через запятую(без пробелов) ваш вектор", 
                  font="30").grid(row=0, column=0, padx=10, pady=10)
        
        self.vector_sc = ttk.Entry(width=100)
        self.vector_sc.grid(row=1, column=0, padx=10, pady=10)
        
        ttk.Label(text="Введите ваш скаляр").grid(row=2, column=0, padx=10, pady=10)
        
        self.scalar = ttk.Entry(width=100)
        self.scalar.grid(row=3, column=0, padx=10, pady=10)
        
        ttk.Button(text="Посчитать умножение на скаляр!", 
                   width=100, 
                   command=self.multiplication_by_scalar).grid(row=4, column=0, padx=10, pady=10)
        
        ttk.Label(text="Введите ваш первый вектор через запятую без пробелов", 
                  font="30").grid(row=5, column=0, padx=10, pady=10)
        
        self.add_vector_start = ttk.Entry(width=100)
        self.add_vector_start.grid(row=6, column=0, padx=10, pady=10)
        
        ttk.Label(text="Введите ваш второй вектор через запятую без пробелов", 
                  font="30").grid(row=7, column=0, padx=10, pady=10)
        
        self.add_vector_travel = ttk.Entry(width=100)
        self.add_vector_travel.grid(row=8, column=0, padx=10, pady=10)
        
        ttk.Button(text="Сложить вектора!", 
                   width=100, command=self.addition_processing).grid(row=9, column=0, padx=10, pady=10)
        
        root.mainloop()
        
    def multiplication_by_scalar(self):
        try:
            vec_sc = str(self.vector_sc.get()).split(',')
            scalar = int(self.scalar.get())
            
            for i in range(len(vec_sc)):
                vec_sc[i] = int(vec_sc[i])
        except:
            root = Toplevel()
            Label(root, text="Вы ввели значение неверно!", 
                  font="30").grid(row=0, column=0, padx=10, pady=10)
            
            Button(root, text="OK", command=root.destroy, width=100).grid(row=1, column=0)
        
        controler = DrawVectorSC()
        multiplied_vector = controler.draw(vec_sc, scalar)
        
        info = Toplevel()
        
        Label(info, text=f"Ваш вектор после умножения на скаляр: {multiplied_vector}", 
              font="30").grid(row=0, column=0, padx=10, pady=10)
        
        Button(info, text="OK", command=info.destroy, 
               width=100).grid(row=1, column=0, padx=10, pady=10)
        
    def addition_processing(self):
        try:
            start = str(self.add_vector_start.get()).split(',')
            travel = str(self.add_vector_travel.get()).split(',')
            
            list_start = []
            list_travel = []
            
            for i in range(len(start)):
                list_start.append(int(start[i]))
                list_travel.append(int(travel[i]))
        except:
            root = Toplevel()
            Label(root, text="Вы ввели значение неверно! Или количество точек векторов не одинаковое", 
                  font="30").grid(row=0, column=0, padx=10, pady=10)
            
            Button(root, text="OK", command=root.destroy, width=100).grid(row=1, column=0)
        
        controller = DrawVectorAdd()
        add_vector = controller.draw(list_start, list_travel)
        
        info = Toplevel()
        
        Label(info, text=f"Ваш вектор после сложения: {add_vector}", 
              font="30").grid(row=0, column=0, padx=10, pady=10)
        
        Button(info, text="ОК", width=100, 
               command=info.destroy).grid(row=1, column=0, padx=10, pady=10)
        
            
        
        