import customtkinter

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")  

import time

app = customtkinter.CTk()  
app.title("Digi Clock")
# app.geometry("150x50")
def time_update():
    t1 = time.strftime("%H:%M:%S %p")
    label1.configure(text=t1)
    label1.after(1000, time_update)
def date_update():
    t1 = time.strftime("%d %b, %Y\n%Z")
    label2.configure(text=t1)
    label2.after(1000, date_update)

label1 = customtkinter.CTkLabel(master=app, font=("ds-digital", 35), fg_color="black", text_color="cyan")
label1.grid(row = 0, column = 0, columnspan = 2, padx = 5, pady = 5)
label2 = customtkinter.CTkLabel(master=app, font=("Consolas", 15), fg_color="black", text_color="cyan")
label2.grid(row = 0, column = 2, columnspan = 1, padx = (0,5), pady = 5)
time_update()
date_update()

app.mainloop()