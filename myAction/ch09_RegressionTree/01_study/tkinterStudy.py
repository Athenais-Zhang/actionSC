from tkinter import Tk, Label, Entry, Button, IntVar, Checkbutton

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



def reDraw(tolS,tolN):
    pass

def drawNewTree():
    pass

def studyTkinter():
    root=Tk() #创建Tk类型的根部件

    Label(root,text="Plot place holder").grid(row=0,columnspan=3)

    Label(root,text="tolN").grid(row=1,column=0)
    tolNentry=Entry(root)
    tolNentry.grid(row=1,column=1)
    tolNentry.insert(0,'10')
    Label(root,text="tolS").grid(row=2,column=0)
    tolSentry=Entry(root)
    tolSentry.grid(row=2,column=1)
    tolSentry.insert(0,'1.0')

    Button(root,text="ReDraw",command=drawNewTree).grid(row=1,column=2,rowspan=3)

    chkBtnVar=IntVar()
    chkBtn=Checkbutton(root,text="Model Tree",variable=chkBtnVar)
    chkBtn.grid(row=3,column=0,columnspan=2)

    # 初始化一些与reDraw相关联的全局变量
    # reDraw.rawDat=mat(regTrees.loadDataSet('sine.txt'))
    # reDraw.testDat=arange(min(reDraw.rawDat[:,0]),max(reDraw.rawDat[:,0]),0.01)
    # reDraw(1.0,10)

    root.mainloop()

def createCanvas():
    root=Tk()
    reDraw.f=Figure(figsize=(5,4),dpi=100)
    reDraw.canvas=FigureCanvasTkAgg(reDraw.f,master=root)
    # reDraw.canvas.show()
    reDraw.canvas.draw()
    reDraw.canvas.get_tk_widget().grid(row=0,columnspan=3)
    root.mainloop()



