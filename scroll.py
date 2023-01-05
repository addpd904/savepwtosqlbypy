from tkinter import *
root=Tk(className='scroll')
root.iconbitmap(r'E:\programme\Python\practice\others\app.ico')
root.geometry('500x500+200+200')

vbar=Scrollbar(root,orient=VERTICAL)
vbar.pack(fill=X)

mylist=Listbox(root,yscrollcommand=vbar.set)
for i in range(30):
    mylist.insert(END,f'{i}st\n')

# vbar.config(command=mylist.yview)
mylist.pack(fill=BOTH)

root.mainloop()
