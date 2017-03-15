import tkinter as tk

LARGE_FONT = ("Verdana", 12)


class FinanceComp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self) #frame is a window

        container.pack(side="top", fill="both", expand=True) ## fill will fill in the space you have alloted with pack

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {} #the idea is that we'll have a lot of different frames and will be stored in this dictionary.
        #then, we'll have code that will call the frame to pop forward.

        for F in (StartPage, PageOne, PageTwo):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew") #grid is the other choice to pack. Grid you assign some frame tp
            #the grid. Specify row and column. Sticky parameter is allignment + stretch. If you want sticky to north
            #then everything will stick the frame to the front. BUt with NSEW, it'll stretch everything to the size
            #of the window

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont] #self.frames corresponds to the self.frames dictionary and cont is the key.
        frame.tkraise() #it'll raise the specified frame to the front. Going to run this method on the frame.

def qf(param):
    print(param)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) #parent class is tk.Tk
        label = tk.Label(self, text="Start Page", font=LARGE_FONT) #tk.Label adds text to a window
        #tk.Label is a class and returned the object called label. Now have to do something with that object.
        label.pack(pady=10, padx=10) #pady and padx are padding

        button = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne)) #the way command work is that it'll just run and
        #won't continue, but can use lambda (almost like a throw away function). If it returns something, then
        #there will be a problem.
        button.pack()

        button1 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button1.pack()


class PageOne(tk.Frame):
#have to pass PageOne
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back To Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visit Page 2",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class PageTwo(tk.Frame):
#have to pass PageOne
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        button1 = tk.Button(self, text="Back To Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Visit Page 1",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()




app = FinanceComp()
app.mainloop()
