from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

from tkinter import *

# TODO:
#   import graphs
#   visualize graphs using Force-Directed layout
#   implement kruskals for barcode retrieval
#   and repulsion and contraction homology UI

# Initialize TKInter Window
root = Tk()
root.wm_title("Scientific Visualization Final")
root.geometry("1280x720")

time_step = 1.0

# Initialize plotting canvas
fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))
plot = FigureCanvasTkAgg(fig, master=root)

# Initialize constant sliders
sliders = Frame()
spring_constant = DoubleVar()
s1 = Scale(
        sliders,
        variable=spring_constant,
        from_=100,
        to=300,
        orient=HORIZONTAL)
l1 = Label(sliders, text = "Spring Constant")
Coulumb_constant = DoubleVar()
s2 = Scale(
        sliders,
        variable=Coulumb_constant,
        from_=0,
        to=1500,
        orient=HORIZONTAL)
l2 = Label(sliders, text = "Coulumb Constant")
damping_coefficient = DoubleVar()
s3 = Scale(
        sliders,
        variable=damping_coefficient,
        from_=100,
        to=300,
        orient=HORIZONTAL)
l3 = Label(sliders, text = "Damping Coefficient")
# Place sliders and labels on grid within sliders module
l1.grid(row=0, column=0, pady=2)
s1.grid(row=1, column=0, pady=2)
l2.grid(row=2, column=0, pady=2)
s2.grid(row=3, column=0, pady=2)
l3.grid(row=4, column=0, pady=2)
s3.grid(row=5, column=0, pady=2)

homology = Frame(root, bg="blue")

# Arrange main window
homology.pack(ipadx=10, ipady=10, expand=True, side="bottom", fill="both")
sliders.pack(ipadx=10, ipady=10, expand=True, side="left", fill="both")
plot.get_tk_widget().pack(ipadx=10, ipady=10, fill="both")

root.mainloop()
