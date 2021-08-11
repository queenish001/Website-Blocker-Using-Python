from datetime import datetime
from tkinter import *
from tkinter import messagebox as msg

redirect_to = "127.0.0.1"
block_sites = []
path = r"C:\Windows\System32\drivers\etc\hosts"

root = Tk()
root.geometry('600x400')
root.title('Focus Mode')
root.configure(bg = "blue")

lbl_title = Label(root, text = "Welcome to Focus Mode", fg='pink', bg='gray', font = ('monotype corsiva', 30, 'bold'), borderwidth=6, relief=RAISED, pady=10)
lbl_title.pack()

#Taking website to be blocked as input
lbl_name = Label(root, text = "Site name (www.sitename.com)", fg = 'black', bg = "sky blue", font = ("Helvetica", 20, 'italic'), padx = 20, pady=10, borderwidth = 5, relief = RIDGE)
lbl_name.pack()
e_name = Entry(root, bg = 'peach puff', font = ("Helvetica", 14), fg = 'black', borderwidth=3, relief=RIDGE)
e_name.pack()


#Taking End time as input
lbl_till = Label(root, text = "Block Site Until (YYYY/MM/DD/HH)", fg = 'black', bg = "sky blue", font = ("Helvetica", 20, 'italic'), padx = 20, pady=10, borderwidth = 5, relief = RIDGE)
lbl_till.pack()
e_till = Entry(root, bg = 'peach puff', font = ("Helvetica", 14), fg = 'black', borderwidth=3, relief=RIDGE)

e_till.pack()

# def focus(): # to check if the datetime entry is working or not
#     x = e_till.get() # time entry 
#     print(int(x[:4]), int(x[5:7]), int(x[8:10]), int(x[11:]))

def focus_mode():
    x = e_till.get() # time entry 
    lbl.configure(text='Blocked!')

    blocked_until = datetime(int(x[:4]), int(x[5:7]), int(x[8:10]), int(x[11:])) # fetching the datetime from user input

    block_sites.append(e_name.get()) # adding the sitename to the list of blocked sites.
    if datetime.now() < blocked_until:
        with open(path, "r+") as hosts_file:
            data = hosts_file.read()
            for site in block_sites:
                if site not in data: # to avoid sitename repetition
                    hosts_file.write(redirect_to + site + '\n')

        print('Site(s) blocked till' + e_till.get())

    else:  # datetime.now >= blocked_until
        lbl.configure(text='Unblocked!')
        with open(path, "r+") as hosts_file:
            lines = hosts_file.readlines()
            hosts_file.seek(0) # start going through the data from the start
            for line in lines:
                if not any(site in line for site in block_sites): # write the line in our file, if it doesn't contain the site name that we want to unblock.
                    hosts_file.write(line)
            hosts_file.truncate()
        print("Site(s) Unblocked.")

def confirmation():
    m1 = msg.askokcancel("Confirm", "Are you sure?")
    if m1 == True:
        focus_mode()
    else:
        pass

submit = Button(root, text = "Submit", command = confirmation, font = ("monotype corsiva", 20, 'bold'), fg='white', bg='black', cursor='target')
submit.pack()
lbl = Label(root, text = " ", fg = 'yellow', bg='blue')
lbl.pack()

root.mainloop()