import tkinter as tk
import numpy as np 

class SalaryPredictionAPP:
    def __init__(self,root):
        self.root = root
        self.root.title("Depi R4 - Machine learning Diploma")
        self.root.geometry("500x400")
        self.create_widget()

    def create_widget(self):
        header = tk.Label(self.root ,text = "DEPI" ,bg="black" ,fg = "blue" ,font= ("Arial",28,"bold"))
        header.pack(fill = tk.X)


if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryPredictionAPP(root)
    root.mainloop()
