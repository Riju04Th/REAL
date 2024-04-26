from tkinter import *
root = Tk() 
root.geometry("1780x820") 
root.title("Riju04Th's Notepad") 
root.minsize(height=250, width=350) 
root.maxsize(height=1720, width=1050) 
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
text_info = Text(root, yscrollcommand=scrollbar.set) 
text_info.pack(fill=BOTH)  
scrollbar.config(command=text_info.yview) 
root.mainloop()
