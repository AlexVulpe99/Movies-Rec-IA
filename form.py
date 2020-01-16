import tkinter as tk

from test import form_function

#string intrare btn search 
def onclick1():
    print (entry1.get())
    #entry1.get() - mesajul introdus
    my_list = form_function(entry1.get())
    if len(my_list) == 0:
        text.insert(tk.END,'No movies found in database that decribe your search')
    for item in my_list:
        text.insert(tk.END, "Title: " + item['title'] + '\n')
        text.insert(tk.END, "Genres: " + str(item['genres']) + '\n')
        text.insert(tk.END, "Tags: " + str(item['tags']) + '\n')
        text.insert(tk.END, "Rating: " + str(item['rating']) + '\n')
        text.insert(tk.END,'\n')
        text.insert(tk.END,'\n')
        text.insert(tk.END,'\n')
    # insert in text box

#clear btn
def onclick2():
    text.delete('1.0', tk.END)
    entry1.delete(0,tk.END)

def onclick3():

    root1 = tk.Tk()
    root1.title("Information")
    root1.resizable(1, 1)

    root1.geometry("300x200")
    root1.configure(background="#add8e6")

    text1 = tk.Text(root1, height=300, width=100,bg="#add8e6",relief=tk.FLAT)
    inf="Welcome to Info!\nTry something like this:\nI am looking for ...\nShow me movies with ...\n\n\nFor searching movies by year you have to add \"year ****\"\n\nFor searching movies by rating you have to add \"rating *.*\""
    text1.insert(tk.END,inf)

    text1.pack()

    root1.mainloop()

#exit btn quit
def onclick4():
    exit()

root = tk.Tk()
root.title("Smart Searching")

root.geometry("1000x750")
root.configure(background="#add8e6")

#label
label1=tk.Label(root, text='Please write what you wanna search here: ',font="helvetica 15",bg="#add8e6")
label1.pack(padx=3, pady=10, side=tk.TOP)

#entry 
entry1 = tk.Entry(root,bg="#d5fdd5",width=50)
entry1.pack(padx=0, pady=7,ipady=2, side=tk.TOP)

#butoane
buton1 = tk.Button(root,text="Search",command=onclick1,relief=tk.FLAT,bg="#9090ee",width=10)
buton1.pack(padx=0, pady=7, side=tk.TOP)

buton2 = tk.Button(root,text="Clear",command=onclick2,relief=tk.FLAT,bg="#ffb347",width=10)
buton2.pack(padx=0, pady=7, side=tk.TOP)

buton3 = tk.Button(root,text="Info",command=onclick3,relief=tk.FLAT,bg="#BC8F8F",width=10)
buton3.pack(padx=0, pady=7, side=tk.TOP)

buton4 = tk.Button(root,text="Quit",command=onclick4,relief=tk.FLAT,bg="#ff392e",width=10)
buton4.pack(padx=0, pady=7, side=tk.TOP)


#textbox
text=tk.Text(root,width=90)
text.pack(padx=0, pady=0, side=tk.TOP,ipady=20)

#scrollbar
scrollbar = tk.Scrollbar(root, command=text.yview,width=30)
scrollbar.pack(padx=0,pady=5,ipadx=0,side=tk.TOP)


root.mainloop()