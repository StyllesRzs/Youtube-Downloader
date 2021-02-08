from tkinter import * 
from pytube import YouTube
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

canv = Tk()
canv.geometry("300x250")
canv.title("YTB(BETA)")
Label(canv, text="Bem-Vindo(a) ao Youtube Downloader!!!").pack()
lvar = StringVar()
lvar.set("Coloque a URL aqui")
Label(canv, textvariable=lvar).pack()
url = StringVar()
Entry(canv, textvariable=url, width=30).pack(pady=10)

def download():
    try:
        lvar.set("Downloading...")
        canv.update()
        YouTube(url.get()).streams.first().download()
        lvar.set("Download Feito com Sucesso")
    except Exception as e:
        lvar.set("Error: " + str(e))
        canv.update()

Button(canv, text="Download", command=download).pack()

canv.mainloop()
