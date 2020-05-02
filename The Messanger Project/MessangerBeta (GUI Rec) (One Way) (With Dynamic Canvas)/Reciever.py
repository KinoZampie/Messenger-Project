from tkinter import *

def TextFinder():
    old_message = None
    x = True
    while True:
        tk.update()
        a = canvas.winfo_width()  
        b = canvas.winfo_height()
        try:
            readMessage = open('MessageData.txt','r')
            message = (readMessage.read())
            if message != old_message:
                canvas.delete(ALL)
                canvas.create_text(a/2,b/2,text = message,fill = 'white',font = 'TNR 100')
                old_message = message
            readMessage.close()
        except:
            x = False

tk = Tk()
canvas = Canvas(tk,width = 500, height = 500, bg = 'black')
canvas.pack(fill=BOTH, expand=YES)
TextFinder()
tk.mainloop()
