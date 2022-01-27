from MyQR import myqr as mq
from PIL import Image
import tkinter

window = tkinter.Tk()
window.title("QR Creater")
window.rowconfigure(0, minsize = 100, weight = 1)
window.columnconfigure(1, minsize = 30, weight = 1)
window.configure(bg = "white")
#frame
frm_entry = tkinter.Frame(master = window, bg = "white")
frm_entry.grid(row = 0, column = 0, padx = 0)

#label 1
lb_link = tkinter.Label(master = frm_entry, text = "Enter the link of the website you want to make a QR of: ", bg = "white")
lb_link.grid(row = 0, column = 0)

#entry field
ent_link = tkinter.Entry(master = frm_entry, width = 50, bg = "white")
ent_link.grid(row = 0, column = 1)

#label 2
lb_link = tkinter.Label(master = frm_entry, text = "Enter the name of the QR code file: ", bg = "white")
lb_link.grid(row = 1, column = 0, padx = 40, pady = 10)

#entry field 2
ent_name = tkinter.Entry(master = frm_entry, width = 50, bg = "white")
ent_name.grid(row = 1, column = 1, padx = 20, pady = 10)

#link = ent_link.get()
#name = ent_name.get()
#mq.run(link, save_name = name)

def sadStuff():
    link = ent_link.get()
    name = ent_name.get()
    name = "qr/" + name + ".png"
    mq.run(link, save_name = name)
    image = Image.open(name)
    image.show()


btn_show = tkinter.Button(
    master = window,
    text = "Show",
    bg = "white",
    command = sadStuff
)
btn_show.grid(row = 2, column = 0, pady = 10)
window.mainloop()
