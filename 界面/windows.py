# 日期 : 2021/8/12
# 时间 : 20:31
# 作者 : kiritio

from tkinter import *
from tkinter.tix import Tk, Control, ComboBox  #升级的组合控件包
from tkinter.messagebox import showinfo, showwarning, showerror #各种类型的提示框

root = Tk() # 初始化Tk()

root.title("hello tkinter")    # 设置窗口标题
root.geometry("600x400")    # 设置窗口大小 注意：是x 不是*
root.resizable(width=True, height=True) # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
root.tk.eval('package require Tix')  #引入升级包，这样才能使用升级的组合控件

lable = Label(root, text="label", bg="pink",bd=10, font=("Arial",12), width=8, height=3)
lable.pack(side=LEFT)


# Booleans
NO = FALSE = OFF = 0
YES = TRUE = ON = 1

# -anchor and -sticky
N = 'n'
S = 's'
W = 'w'
E = 'e'
NW = 'nw'
SW = 'sw'
NE = 'ne'
SE = 'se'
NS = 'ns'
EW = 'ew'
NSEW = 'nsew'
CENTER = 'center'

# -fill
NONE = 'none'
X = 'x'
Y = 'y'
BOTH = 'both'

# -side
LEFT = 'left'
TOP = 'top'
RIGHT = 'right'
BOTTOM = 'bottom'

# -relief
RAISED = 'raised'
SUNKEN = 'sunken'
FLAT = 'flat'
RIDGE = 'ridge'
GROOVE = 'groove'
SOLID = 'solid'

# -orient
HORIZONTAL = 'horizontal'
VERTICAL = 'vertical'

# -tabs
NUMERIC = 'numeric'

# -wrap
CHAR = 'char'
WORD = 'word'

# -align
BASELINE = 'baseline'

# -bordermode
INSIDE = 'inside'
OUTSIDE = 'outside'

# Special tags, marks and insert positions
SEL = 'sel'
SEL_FIRST = 'sel.first'
SEL_LAST = 'sel.last'
END = 'end'
INSERT = 'insert'
CURRENT = 'current'
ANCHOR = 'anchor'
ALL = 'all'  # e.g. Canvas.delete(ALL)

# Text widget and button states
NORMAL = 'normal'
DISABLED = 'disabled'
ACTIVE = 'active'
# Canvas state
HIDDEN = 'hidden'

# Menu item types
CASCADE = 'cascade'
CHECKBUTTON = 'checkbutton'
COMMAND = 'command'
RADIOBUTTON = 'radiobutton'
SEPARATOR = 'separator'

# Selection modes for list boxes
SINGLE = 'single'
BROWSE = 'browse'
MULTIPLE = 'multiple'
EXTENDED = 'extended'

# Activestyle for list boxes
# NONE='none' is also valid
DOTBOX = 'dotbox'
UNDERLINE = 'underline'

# Various canvas styles
PIESLICE = 'pieslice'
CHORD = 'chord'
ARC = 'arc'
FIRST = 'first'
LAST = 'last'
BUTT = 'butt'
PROJECTING = 'projecting'
ROUND = 'round'
BEVEL = 'bevel'
MITER = 'miter'

# Arguments to xview/yview
MOVETO = 'moveto'
SCROLL = 'scroll'
UNITS = 'units'
PAGES = 'pages'

root.mainloop()