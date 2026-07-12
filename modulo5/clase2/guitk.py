from tkinter import Tk
from tkinter.ttk import Treeview

root = Tk()
root.title("Mi Primera GUI")

tree = Treeview()
tree['columns'] = ('Nombre', 'Email')

tree.column('#0', width=0, stretch=True)
tree.column('Nombre')
tree.column('Email')

tree.heading('#0', text='id')
tree.heading('Nombre', text='Nombre')
tree.heading('Email', text='Email')

tree.grid(row=0, column=0)

tree.insert('', 'end', values=('cesar mayta', 'cmayta@ed.team'))

root.mainloop()
