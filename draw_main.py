from tkinter import ttk
from tkinter import *
from calculation_multiplication_by_calar import DrawVector

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
        
        controler = DrawVector()
        multiplied_vector = controler.draw(vec_sc, scalar)
        
        info = Toplevel()
        
        Label(info, text=f"Ваш вектор после умножения на скаляр: {multiplied_vector}", 
              font="30").grid(row=0, column=0, padx=10, pady=10)
        
        Button(info, text="OK", command=info.destroy, 
               width=100).grid(row=1, column=0, padx=10, pady=10)
        
            
        
        