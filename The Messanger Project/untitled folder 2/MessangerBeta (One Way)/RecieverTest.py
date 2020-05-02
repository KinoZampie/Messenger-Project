##old_message = None
##x = True
##while True:
##    try:
##        readMessage = open('MessageData.txt','r')
##        message = (readMessage.read())
##        if message != old_message:
##            print (message)
##            old_message = message
##        readMessage.close()
##    except:
##        x = False

def TextFinder():
    old_message = None
    x = True
    while True:
        tk.update()
        try:
            readMessage = open('MessageData.txt','r')
            message = (readMessage.read())
            if message != old_message:
                canvas.create_text(250,250,text = message, fill = 'white',font = 'TNR 78')
                old_message = message
            readMessage.close()
        except:
            x = False

from tkinter import *



tk = Tk()
canvas = Canvas(width = 500,height = 500,bg = 'black')
canvas.pack()
TextFinder()
tk.mainloop()
