from customtkinter import CTk, CTkFrame, CTkEntry, CTkLabel, CTkButton, filedialog
from LIBS.filter_data import filter_data_show,data_filtar
from LIBS.temp import template
from PIL import Image,ImageTk
from threading import Thread
import requests
from io import BytesIO
import os, shutil,sys
import webbrowser


if getattr(sys,'frozen',False):
    import pyi_splash

class Printer:
    def __init__(self):
        self.sizes = []
        self.colors = []
        self.color_buttons = []
        self.size_buttons = [] 
        self.selected_color = None
        self.selected_size = None

    def print_qr(self):
        if self.entry.get()!='':
            try:
                os.startfile(os.path.join(os.getcwd(),"output.png"),"print")
            except:
                pass

    def th_img(self,link):
        try:
            th = Thread(target=self.img_loader,args=(link[0],))    
            th.start()
        except IndexError as e:
            pass

    def img_loader(self,link):
        
        try:
                response = requests.get(link)
                img_data = response.content
                img = Image.open(BytesIO(img_data))
                img = img.resize((300, 400))  
                img_tk = ImageTk.PhotoImage(img)
         
                self.imgae_label.configure(image=img_tk,text='')
                
        except Exception as e:
            pass

    def final_data(self):
        id = self.entry.get().upper()

        if self.selected_color!=None and self.selected_size!=None:
            data = data_filtar(id=id,color=self.selected_color,size=self.selected_size)

            sku = data[0]
            size= data[5]
            taly = data[1]

            template(sku[0],size,taly[0])


            link = data[2]
            self.th_img(link)

            img = Image.open('for_show_only.png')
            imgtk = ImageTk.PhotoImage(img)

            self.qr_label.configure(image = imgtk)
    def th_color_button(self):
        th = Thread(target=self.create_color_button)
        th.start()

    def create_color_button(self):
        self.clear_color_buttons()
        colors = self.show[2]

        def create_button(color):
            row = i // 9
            column = i % 9
            color_button = CTkButton(self.color_fram, text=color, width=65, command=lambda c=color: self.select_color(c))
            color_button.grid(row=row, column=column, padx=5, pady=5)
            self.color_buttons.append(color_button)

        # Create buttons concurrently
        threads = []
        for i, color in enumerate(colors):
            t = Thread(target=create_button, args=(color,))
            t.start()
            threads.append(t)
        
    def create_size_button(self):
        self.clear_size_buttons()
        self.sizes = sorted(self.show[1])
        self.size_buttons = []
        for i, size in enumerate(self.sizes):
            row = i // 9
            column = i % 9
            size_button = CTkButton(master=self.size_fram, text=str(size), width=80, command=lambda x=size: self.select_size(x))
            size_button.grid(row=row, column=column, padx=2, pady=5)
            self.size_buttons.append(size_button)

    def select_color(self, color):
        self.selected_color = color
        self.final_data()

    def fileOpener(self):
        loadfile = filedialog.askopenfilename(title="Select File",filetypes=[("CSV files","*.csv")])
        if loadfile:
            shutil.copy(loadfile,os.path.join(os.getcwd(),"data.csv"))
        else:
            pass    


        webbrowser.open('https://www.instagram.com/amit_sark/')    

    def duelcoller(self):


        # Create thread for opening the file
        th2 = Thread(target=self.fileOpener)
        th2.start()

        # Wait for both threads to finish


        


    def select_size(self, size):
        self.selected_size = size
        self.final_data()

    def clear_size_buttons(self):
        if self.size_buttons:
            for button in self.size_buttons:
                button.destroy()
            self.size_buttons.clear()

    def clear_color_buttons(self):
        if self.color_buttons:
            for button in self.color_buttons:
                button.destroy()
            self.color_buttons.clear()

    def search_on_key_release(self, dt):
        self.data = self.entry.get().upper()
        self.show = filter_data_show(id=self.data)

        if self.show:
            self.clear_size_buttons()
            self.clear_color_buttons()
            self.create_size_button()
            self.th_color_button()
        else:
            self.clear_size_buttons()

    def gui(self):
        self.window = CTk()
        self.window.title("Label printer by sark")
        self.window.iconbitmap(os.path.join(os.getcwd(),"printer.ico"))
        self.window.resizable(False,False)
        width = 1080
        height = 720
        x = (self.window.winfo_screenwidth() // 2) - (width // 2)
        y = (self.window.winfo_screenheight() // 2) - (height // 2)
        self.window.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        self.upper_fram = CTkFrame(master=self.window, width=680, height=80)
        self.upper_fram.place(x=40, y=20)

        self.middle_fram = CTkFrame(master=self.window, width=680, height=570)
        self.middle_fram.place(x=40, y=120)

        self.color_fram = CTkFrame(master=self.middle_fram, width=660, height=400)
        self.color_fram.place(x=10, y=10)

        self.size_fram = CTkFrame(master=self.middle_fram, width=660, height=140)
        self.size_fram.place(x=10, y=420)

        self.side_fram = CTkFrame(master=self.window, width=320)
        self.side_fram.place(x=740, y=20)

        self.side_lower_fram = CTkFrame(master=self.window, width=320, height=450)
        self.side_lower_fram.place(x=740, y=240)

        self.search_label = CTkLabel(master=self.upper_fram, text='Search: ')
        self.search_label.place(x=5+35, y=28)

        self.entry = CTkEntry(master=self.upper_fram, width=200)
        self.entry.place(x=80+30, y=28)
        self.entry.bind('<KeyRelease>', self.search_on_key_release)

        self.print_button = CTkButton(master=self.upper_fram, text='Print', command=self.print_qr)
        self.print_button.place(x=300+30, y=28)
        self.window.bind('<Return>', lambda event: self.print_qr())


        self.load_button = CTkButton(master=self.upper_fram, text='Load', command=self.duelcoller)
        self.load_button.place(x=450+35, y=28)

        self.imgae_label = CTkLabel(self.side_lower_fram,text='')
        self.imgae_label.place(x=35,y=55)

        self.qr_label = CTkLabel(self.side_fram,text='')
        self.qr_label.place(x=35,y=40)

        if getattr(sys,'frozen',False):
            pyi_splash.close()

        self.window.mainloop()

if __name__ == '__main__':
    app = Printer()
    app.gui()
