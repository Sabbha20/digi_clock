import customtkinter

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")  

import time

app = customtkinter.CTk()  
app.title("Digi Clock")
app.geometry("200x50")
def time_update():
    t1 = time.strftime("%H:%M:%S %p")
    label1.configure(text=t1)
    label1.after(1000, time_update)

label1 = customtkinter.CTkLabel(master=app, font=("ds-digital", 26), fg_color="black", text_color="cyan")
label1.pack(anchor="center")
time_update()


app.mainloop()