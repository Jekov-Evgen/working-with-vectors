from tkinter import ttk
from tkinter import *
from calculation_multiplication_by_calar import DrawVectorSC
from add_vector import DrawVectorAdd
from vector_subtraction import DrawVectorSub

def show_error(message):
    error = Toplevel()
    Label(error, text=message, font="30").grid(row=0, column=0, padx=10, pady=10)
    Button(error, text="ОК", command=error.destroy, width=50).grid(row=1, column=0, padx=10, pady=10)
    
def show_result(message):
    info = Toplevel()
    Label(info, text=message, font="30").grid(row=0, column=0, padx=10, pady=10)
    Button(info, text="ОК", command=info.destroy, width=50).grid(row=1, column=0, padx=10, pady=10)

class MainWindow:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("Вектора")

    def draw_main(self):
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.grid()

        ttk.Button(main_frame, text="Умножение вектора на скаляр", width=50, command=self.open_scalar_window).grid(row=0, column=0, padx=10, pady=10)

        ttk.Button(main_frame, text="Сложение векторов", width=50, command=self.open_addition_window).grid(row=1, column=0, padx=10, pady=10)

        ttk.Button(main_frame, text="Вычитание векторов", width=50, command=self.open_subtraction_window).grid(row=2, column=0, padx=10, pady=10)

        self.root.mainloop()


    def open_scalar_window(self):
        ScalarWindow()


    def open_addition_window(self):
        AdditionWindow()


    def open_subtraction_window(self):
        SubtractionWindow()


class ScalarWindow:
    def __init__(self) -> None:
        self.window = Toplevel()
        self.window.title("Умножение вектора на скаляр")


        ttk.Label(self.window, text="Введите ваш вектор через запятую (без пробелов):").grid(row=0, column=0, padx=10, pady=10)
        self.vector_entry = ttk.Entry(self.window, width=50)
        self.vector_entry.grid(row=1, column=0, padx=10, pady=10)


        ttk.Label(self.window, text="Введите ваш скаляр:").grid(row=2, column=0, padx=10, pady=10)
        self.scalar_entry = ttk.Entry(self.window, width=50)
        self.scalar_entry.grid(row=3, column=0, padx=10, pady=10)


        ttk.Button(self.window, text="Посчитать умножение на скаляр!", command=self.multiplication_by_scalar).grid(row=4, column=0, padx=10, pady=10)

    def multiplication_by_scalar(self):
        try:
            vector = [int(x) for x in self.vector_entry.get().split(',')]
            scalar = int(self.scalar_entry.get())
        except ValueError:
            show_error("Вы ввели значения неверно")
            return

        controller = DrawVectorSC()
        multiplied_vector = controller.draw(vector, scalar)
        show_result(f"Ваш вектор после умножения на скаляр {multiplied_vector}")


class AdditionWindow:
    def __init__(self) -> None:
        self.window = Toplevel()
        self.window.title("Сложение векторов")

        ttk.Label(self.window, text="Введите первый вектор через запятую (без пробелов):").grid(row=0, column=0, padx=10, pady=10)
        self.vector1_entry = ttk.Entry(self.window, width=50)
        self.vector1_entry.grid(row=1, column=0, padx=10, pady=10)

        ttk.Label(self.window, text="Введите второй вектор через запятую (без пробелов):").grid(row=2, column=0, padx=10, pady=10)
        self.vector2_entry = ttk.Entry(self.window, width=50)
        self.vector2_entry.grid(row=3, column=0, padx=10, pady=10)

        ttk.Button(self.window, text="Сложить вектора!", command=self.addition_processing).grid(row=4, column=0, padx=10, pady=10)

    def addition_processing(self):
        try:
            vector1 = [int(x) for x in self.vector1_entry.get().split(',')]
            vector2 = [int(x) for x in self.vector2_entry.get().split(',')]
        except ValueError:
            show_error("Вы ввели значения неверно")
            return

        controller = DrawVectorAdd()
        add_vec = controller.draw(vector1, vector2)
        show_result(f"Ваш вектор после сложения {add_vec}")


class SubtractionWindow:
    def __init__(self) -> None:
        self.window = Toplevel()
        self.window.title("Вычитание векторов")

        ttk.Label(self.window, text="Введите первый вектор через запятую (без пробелов):").grid(row=0, column=0, padx=10, pady=10)
        self.vector1_entry = ttk.Entry(self.window, width=50)
        self.vector1_entry.grid(row=1, column=0, padx=10, pady=10)

        ttk.Label(self.window, text="Введите второй вектор через запятую (без пробелов):").grid(row=2, column=0, padx=10, pady=10)
        self.vector2_entry = ttk.Entry(self.window, width=50)
        self.vector2_entry.grid(row=3, column=0, padx=10, pady=10)

        ttk.Button(self.window, text="Вычесть из вектора!", command=self.subtraction_processing).grid(row=4, column=0, padx=10, pady=10)

    def subtraction_processing(self):
        try:
            vector1 = [int(x) for x in self.vector1_entry.get().split(',')]
            vector2 = [int(x) for x in self.vector2_entry.get().split(',')]
        except ValueError:
            show_error("Вы ввели значения неверно")
            return

        controller = DrawVectorSub()
        sub_vec = controller.draw(vector1, vector2)
        show_result(f"Ваш вектор после вычитания {sub_vec}")