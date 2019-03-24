from tkinter import *

def donothing(var=''):
    pass

class interface(Tk):
    
    def __init__(self, name='Interface', size=None):
        super(interface, self).__init__()
        if size:
            self.geometry(size)
        self.title(name)
        self.frame=Frame(self)
        self.frame.pack()
        
    def gui_print(self, text='This is some text', command=donothing):
        self.frame.destroy()
        self.frame=Frame(self)
        self.frame.pack()
        Label(self.frame, text=text).pack()
        Button(self.frame, text='Ok', command=command).pack()
        
    def gui_input(self, text='Enter something', command=donothing):
        self.frame.destroy()
        self.frame=Frame(self)
        self.frame.pack()        
        Label(self.frame, text=text).pack()
        entry=StringVar(self)
        Entry(self.frame, textvariable=entry).pack()
        Button(self.frame, text='Ok', command=lambda: command(entry.get())).pack()
        
    def end(self):
        self.destroy()
        
    def start(self):
        mainloop()
if __name__=='__main__':
    
    def foo2(value):
        global main
        main.gui_print('Your name is '+value+'.', main.end)
        
    def foo1():
        global main
        main.gui_input('What is your name?', foo2)
    main=interface('Window')
    foo1()
    main.start()