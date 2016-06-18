import sys
import os
from tkinter import *
#import tkMessageBox

top=Tk()

def callGraph():
    os.system('python3 sentiment_graph.py')

B=Button(top,text="Graph",command= callGraph)
B.pack()
top.mainloop()
