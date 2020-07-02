from pytube import YouTube
from tkinter import *
from tkinter import filedialog
from io import BytesIO
import requests
import os
from moviepy.editor import *
from PIL import ImageTk, Image

path = ""

def clear_all():
    try:
        action.pack_forget()
        link_entry.delete(0,END)
        action.destroy()
    except Exception as e:
        print(e)

def download_video():
    try:
        b1.config(text="Please wait...")
        b1.config(state=DISABLED)
        stream = yt.streams.first()
        path = filedialog.askdirectory()
        if path == None:
            return
        stream.download(path)
        l2 = Label(action,text="Download Complete",font=("Calibri",12),fg = "green").pack()
        b1.config(text="Download Video")
    except:
        l2 = Label(action,text="Error occured while Downloading",font=("Calibri",12),fg = "red").pack()


def download_audio():
    try:
        global stram
        b2.config(text="Please wait...")
        b2.config(state=DISABLED)
        stream = yt.streams.filter(progressive=True)
        path = filedialog.askdirectory()
        if path == None:
            return
        print(stream)
        stream[0].download(path)
        for i in os.listdir(path):
            os.rename(os.path.join(path,i),os.path.join(path,i.replace(' ','_')))
        title = yt.title.replace(' ','_')
        video = VideoFileClip(os.path.join(path+"/"+title+".mp4"))
        video.audio.write_audiofile(os.path.join(path+"/"+title+".mp3"))

        l3 = Label(action,text="Download Complete",font=("Calibri",12),fg = "green").pack()
        b2.config(text="Download Audio")
        if os.path(f'{title}.mp4'):
            os.remove(f'{title}.mp4')
    except Exception as e:
        print(e)
        l3 = Label(action,text="Error occured while Downloading",font=("Calibri",12),fg = "red").pack()

def search_vid():
    global action,b1,b2,yt,l1
    try:
        action.destroy()
        l1.destroy()
    except:
        pass
    action = Frame(root)
    action.pack(expand="yes",fill="both")
    url = link.get()
    try:
        yt = YouTube(url)
    except:
        action.pack_forget()
        action.destroy()
        l1 = Label(root,text="An Error Occured",font=("Calibri",12))
        l1.pack()

    Label(action,text="").pack()
    response = requests.get(yt.thumbnail_url)
    image = Image.open(BytesIO(response.content))
    image = image.resize((150,105),Image.ANTIALIAS)
    img = ImageTk.PhotoImage(image)
    panel = Label(action,image=img)
    panel.image = img
    panel.pack()
    Label(action,text="").pack()
    l1 = Label(action,text=yt.streams[0].title+'\n'+yt.author,font=("Calibri",14))
    l1.pack()
    Label(action,text="").pack()
    top = Frame(action)
    bottom = Frame(action)
    top.pack(side=TOP)
    bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

    b1 = Button(action,text="Download Video",command=download_video,width="15",fg="gray26",font=("Calibri",12,"bold"),relief="ridge")
    b1.pack(in_=top, side=LEFT)
    Label(action,text="").pack(in_=top, side=LEFT)
    b2 = Button(action,text="Download Audio",command=download_audio,width="15",fg="gray26",font=("Calibri",12,"bold"),relief="ridge")
    b2.pack(in_=top, side=LEFT)
    Label(action,text="").pack()


root = Tk()
root.geometry("600x600")
root.title("Youtube Downloader")
font = ("poppins",25,"normal")
Label(root,text="Youtube Downloader",width="150",height="2",bg="RoyalBlue1",fg="white",font=("Calibri",22,"bold")).pack()
Label(root,text="").pack()
Label(root,text="").pack()
Label(root,text="Enter Youtube Link : ",fg="gray26",font=("Calibri",16,"bold")).pack()
link = StringVar()
link_entry = Entry(root,textvariable = link,width="70")
link_entry.pack()
Label(root,text="").pack()

top = Frame(root)
bottom = Frame(root)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)


Button(root,text="Search",command=search_vid,width="8",fg="gray26",font=("Calibri",12,"bold"),relief="ridge").pack(in_=top, side=LEFT)
Label(root,text="").pack(in_=top, side=LEFT)
Button(root,text="Clear",command=clear_all,width="8",fg="gray26",font=("Calibri",12,"bold"),relief="ridge").pack(in_=top, side=LEFT)
Label(root,text="").pack()

root.mainloop()
