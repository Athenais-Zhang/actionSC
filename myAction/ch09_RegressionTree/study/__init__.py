from tkinter import *

from numpy import mat
from numpy.core import shape

import tkinterStudy as tks
import myRegTrees as mrt

# root=Tk()
# # myLabel=Label(root,text="hello,world")
# # myLabel.grid()
# root.mainloop()

# tks.studyTkinter()
# tks.createCanvas()

myDat=mrt.loadDataSet('../dataset/ex00.txt')
myMat=mat(myDat)
# print(myMat)
# print(shape(myMat))
tree = mrt.createTree(myMat)
print (tree)