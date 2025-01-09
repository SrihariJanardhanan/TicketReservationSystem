import tkinter
window = tkinter.Tk()
window.title('SAMPLE')
label = tkinter.Label(window, text='HELLO WORLD!').pack()
l1 = tkinter.Label(window, text='hi').pack()


def clicked():
    l1.configure(text='BUTTON WAS CLICKED!!')


b1 = tkinter.Button(window, text='Enter', command=clicked).pack()

window.mainloop()
