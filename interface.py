from tkinter import *
from PIL import ImageTk, Image
from tkinterweb import HtmlFrame

class Loc:
    def __init__(self, root, callback):
        self.root = root
        self.callback = callback
        self.root.title("Tracking")
        self.root.geometry("1180x600+100+50")

        # Load and resize the background image
        self.original_bg = Image.open("image/pic3.jpg")
        self.bg = ImageTk.PhotoImage(self.original_bg.resize((1180, 600), Image.Resampling.LANCZOS))
        
        # Display the background image
        self.bg_image = Label(self.root, image=self.bg)
        self.bg_image.place(x=0, y=0, relwidth=1, relheight=1)

        # Text
        title1 = Label(self.root, text="Welcome to Tracking_app", font=("Impact", 25, "bold"), fg="white", bg="#030d3f")
        title1.place(x=100, y=30)

        title2 = Label(self.root, text="Enter a phone number into this app, and we'll track its location anywhere in the world.", font=("", 15), fg="white", bg="#0b1649")
        title2.place(x=80, y=100)

        # Input
        self.num = Entry(self.root, font=("", 10), bg="#E7E6E6")
        self.num.place(x=80, y=150, width=320, height=30)

        # Button
        search_btn = Button(self.root, text="search", font=("", 15), bg="white", fg="black", command=self.search_click)
        search_btn.place(x=430, y=150, width=100, height=30)

        # Frame for map
        self.map_frame = Frame(self.root, bg="white")
        self.map_frame.place(x=80, y=230, width=1020, height=330)

        # Initial empty map
        self.map_label = HtmlFrame(self.map_frame)
        self.map_label.pack(fill="both", expand=True)

        # Bind the resize event to a function to adjust the background image
        self.root.bind("<Configure>", self.resize_background)

    def resize_background(self, event):
        # Get the new size of the window
        new_width = event.width
        new_height = event.height
        
        # Resize the image to the new size of the window
        resized_bg = self.original_bg.resize((new_width, new_height), Image.Resampling.LANCZOS)
        self.bg = ImageTk.PhotoImage(resized_bg)
        
        # Update the background image
        self.bg_image.config(image=self.bg)
        self.bg_image.image = self.bg

    def search_click(self):
        # This method is called when the search button is clicked
        phone_number = self.num.get()
        # Call the callback function with the phone number
        self.callback(phone_number)

    def update_map(self, map_html):
        self.map_label.load_file(map_html)
