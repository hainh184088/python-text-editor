import sys
v = sys.version

if "2.7" in v:
    from Tkinter import *
    import tkFileDialog
elif "3." in v:
    from tkinter import *
    from tkinter import filedialog, Menu

def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    print(savelocation)
    file1=open(savelocation, "w+")
    file1.write(t)
    file1.close()

root = Tk("Text Editor")
root.title("Text Editor")

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='SaveAs', command=saveas)
file_menu.add_command(label='Close')
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)
# create the Help menu
help_menu = Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

text = Text(root)
text.grid()
root.mainloop()





