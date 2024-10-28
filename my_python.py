
from tkinter import*
from tkinter import ttk
from views   import*
from tkinter import messagebox


#color
co0 = "blue"
co1 =  "black"
co2 = "white"


#window setup

window = Tk()
window.title ("my app")
window.geometry("485x450")
window.configure(background=co2)
window.resizable(width=False, height=False)



#frames
frame_up =Frame(window, width=500, height=50, bg=co0)
frame_up.grid(row=0, column=0,padx=0,pady=1)

frame_dwon =Frame(window, width=500, height=150, bg=co2)
frame_dwon.grid(row=1, column=0,padx=0,pady=1)

frame_table =Frame(window, width=500, height=100, bg=co1)
frame_table.grid(row=2, column=0, columnspan=2,padx=0,pady=1)

# Functions
def show():
    global tree

    listheader = ["name", "gender", "email", "telephone"]

    demo_list = view()

    tree = ttk.Treeview(frame_table, selectmode="extended", columns=listheader, show="headings")

    # Adding the headers
    for col in listheader:
        tree.heading(col, text=col)
        tree.column(col, minwidth=0, width=100)

    tree.grid(row=0, column=0, sticky='nsew')

    # Create Scrollbars after defining the tree
    vsb = ttk.Scrollbar(frame_table, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_table, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    vsb.grid(row=0, column=1, sticky='ns')
    hsb.grid(row=1, column=0, sticky='ew')

    for item in demo_list:
        tree.insert('','end', values=item)

show()

def insert():
    name = e_name.get()
    gender = c_gender.get()
    telephone =e_telephone.get()
    email =e_email.get()

    data = [name, gender, telephone, email]

    if name =='' or gender =='' or telephone =='' or email == '':
       messagebox.showwarning('data', 'please fill in the all fields')

    else:
        add(data)  
        messagebox.showinfo('data','data add successfully')
        e_name.delete(0,'end')
        c_gender.delete(0,'end')
        e_telephone.delete(0,'end')
        e_email.delete(0,'end')

        show() 
def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary =tree.item(tree_data)
        tree_list = tree_dictionary['values']

        name = str(tree_list[0])
        gender = str(tree_list[1])
        telephone =str(tree_list[2])
        email = str(tree_list[3])

        e_email.insert(0, name)
        c_gender.insert(o, gender)
        e_telephone.insert(0, telephone)
        e_email.insert(0, email)

        def confirm():
            new_name= e_name.get()
            new_gender= c_gender.get()
            new_telephone= e_telephone.get()
            new_email= e_email.get()

            data = [new_telephone,new_name, new_gender, new_telephone, new_email]


            update(data)

            messagebox.showinfo('success', 'data update successfully')
            e_name.delete(0,'end')
            c_gender.delete(0,'end')
            e_telephone.delete(0,'end')
            e_email.delete(0,'end')

            for widget in frame_table.winfo_children():
                widget.destroy

            b_confirm.destroy

            show()
        b_confirm= Button(frame_dwon, text="confirm", width=10, height=1, bg=co1,fg=co2, font=("Ivy 8 bold"), command=confirm)
        b_confirm.place(X =230, y=110)

    except IndexError:
           messagebox.showerror('Error', 'select of them from the table')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary =tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_telephone= str[tree_list[2]]
        remove(tree_telephone)
        messagebox.showinfo('success', 'data has been deleted successfully')
        for widget in frame_table.winfo_children():
                widget.destroy
        show()        
    except IndexError:
        messagebox.showerror('Error', 'select of them from the table')
def to_search():
    telephone =e_search.get()
    data=search(telephone)
    def delete_command():
        tree.delete(*tree.get_children())
    delete_command
    for item in data:
        tree.insert('','end',values=item)
        e_search.delete(0,'')                        


#frame_up Widgets


app_name = Label(frame_up, text="phonebook",height=1, font=("vardana 17 bold"),fg=co1)
app_name.place(x=5, y=5)

#frame_dwon widgets

i_name = Label(frame_dwon,text="name *", width=20, height=1, font=("ivy 10"),bg=co2,anchor=NW)
i_name.place(x=10, y=20)
e_name = Entry(frame_dwon, width=25, justify="left",highlightthickness=1,relief="solid")
e_name.place(x=80, y=20)

i_gender = Label(frame_dwon,text="gender *", width=25, height=1, font=("ivy 10"),bg=co2,anchor=NW)
i_gender.place(x=10, y=50)
c_gender = ttk.Combobox(frame_dwon, width=22, )
c_gender["values"]=["", "F","M"]
c_gender.place(x=80, y=50)

i_telephone = Label(frame_dwon,text="telephone*",  height=1, font=("ivy 10"),bg=co2,anchor=NW)
i_telephone.place(x=10, y=80)
e_telephone = Entry(frame_dwon, width=25, justify="left",highlightthickness=1,relief="solid")
e_telephone.place(x=80, y=80)

i_email = Label(frame_dwon,text="email*",  height=1, font=("ivy 10"),bg=co2,anchor=NW)
i_email.place(x=10, y=110)
e_email = Entry(frame_dwon, width=25, justify="left",highlightthickness=1,relief="solid")
e_email.place(x=80, y=110)


b_search = Button(frame_dwon, text="search", height=1, bg=co1,fg=co2, font=("Ivy 8 bold"),command=to_search)
b_search.place(x=290, y=20)
e_search = Entry(frame_dwon, width=16, justify="left", font=("Ivy", 11), highlightthickness=1, relief="solid")
e_search.place(x=347, y=20)

b_view = Button(frame_dwon, text="view",width=10,  height=1, bg=co1,fg=co2, font=("Ivy 8 bold"),command=show)
b_view.place(x=290, y=50)

b_add = Button(frame_dwon, text="add", width=10, height=1, bg=co1,fg=co2, font=("Ivy 8 bold"),command=insert)
b_add.place(x=400, y=50)

b_update = Button(frame_dwon, text="update", width=10, height=1, bg=co1,fg=co2, font=("Ivy 8 bold"), command=to_update)
b_update.place(x=400, y=80)

b_delete = Button(frame_dwon, text="delete", width=10, height=1, bg=co1,fg=co2, font=("Ivy 8 bold"))
b_delete.place(x=400, y=110)


window.mainloop()
