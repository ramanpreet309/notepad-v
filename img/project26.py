from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("600x600")
root.title("BookStore")
root.config(bg='lightblue')
# root.resizable(False,False)

def openNewWindow():

    newWindow = Toplevel(root)

    newWindow.title("History")

    newWindow.geometry("200x200")


    Label(newWindow,
          text="Book Collection").pack()
    Label(newWindow,
          text="POST-GRADUATION BLUES").pack()

def openhomewin():
        home = Toplevel(root)

        home.title("Little Red Store Of Books")

        home.geometry("200x200")

        Label(home,
              text="Doing well by doing good").pack()
        Label(home,
              text="We believe profit is not the only way to measure business success.").pack()


label = Label(root,
              text="Welcome To Little Red Store of Books")
# label= Label(root, text="Dear readers,We offer huge collection of books in diverse category of Fiction, Non-fiction, Biographies, History, Religions, Self -Help, Children. We also sell in vast collection of Investments and Management, Computers, Engineering, Medical, College and School text references books proposed by different institutes as syllabus across the country. Besides to this, we also offer a large collection of E-Books at very fair pricing.We attempt to extend the customer satisfaction by catering easy user-friendly search engine, quick and user-friendly payment options and quicker delivery systems. Upside to all of this, we are disposed to provide exciting offers and pleasant discounts on our books.As well, we humbly invite all the sellers around the country to partner with us. We will surely provide you the platform for many sparkling domains and grow the “BooksWagon” family.We would like to thank you for shopping with us. You can write us for any new thoughts at “email-id” helping us to improvise for the reader satisfaction")

label.pack(pady=10)

# a button widget which will open a
# new window on button click
btn = Button(root,
             text="Enter to bookstore",
             command=openNewWindow)

btn.pack(pady=10)


btn = Button(root,
             text="Home",
             command=openhomewin)

btn.pack(pady=10)


btn = Button(root,
             text="About",
             command=openNewWindow)

btn.pack(pady=10)

btn = Button(root,
             text="Contact",
             command=openNewWindow)

btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()

lbl = Label(root, text = "Welcome To Little Red Store of Books")
lbl.pack()

photo = PhotoImage(file = "delete.png")



btn = Button(root, text = 'Click me !', bd = '5',
                          command = root.destroy)
btn.pack(side = 'top')


root.mainloop()