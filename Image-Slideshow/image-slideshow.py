from tkinter import *
from PIL import Image, ImageTk
import time
from pathlib import Path


class Slider:
    def __init__(self, root):
        self.root = root
        self.root.title("TryCatch Image Slideshow")
        self.root.geometry("900x500")

        # Load images with pathlib and ensure paths are correct
        image_paths = [
            Path("D:/vidyaPY/Beginner-Python-Projects-main/Image-Slideshow/lakes.png"),
            Path("D:/vidyaPY/Beginner-Python-Projects-main/Image-Slideshow/mountains.jpg")
        ]

        # Resize images and store in a list
        self.images = [self.load_image(path) for path in image_paths]
        self.image_index = 0

        # Create frame and label for slideshow
        Frame_slider = Frame(self.root)
        Frame_slider.place(x=150, y=70, width=600, height=350)
        self.label = Label(Frame_slider, image=self.images[self.image_index], bd=0)
        self.label.place(x=0, y=0)
        
        # Start the transition loop
        self.slider_func()

    def load_image(self, path, size=(700, 400)):
        """Helper function to load and resize images."""
        image = Image.open(path)
        image = image.resize(size, Image.LANCZOS)  # Use LANCZOS instead of ANTIALIAS
        return ImageTk.PhotoImage(image)

    def slider_func(self):
        """Slide function with a fade-in effect."""
        # Increment image index and loop back if needed
        self.image_index = (self.image_index + 1) % len(self.images)
        next_image = self.images[self.image_index]

        # Fade effect with small delay
        for _ in range(20):  # 20 steps for fade transition
            self.label.config(image=next_image)
            self.root.update_idletasks()
            time.sleep(0.05)  # Delay for smoother transition

        # Call again after delay for next transition
        self.root.after(2000, self.slider_func)  # Change image every 2 seconds


root = Tk()
obj = Slider(root)
root.configure(bg="powderblue")

# Set title and icon
photo = PhotoImage(file="D:/vidyaPY/Beginner-Python-Projects-main/Image-Slideshow/gallery.png")
title = Label(root, text="Image Slideshow",
              fg="Black", bg="powderblue", font=("Arial", 25, 'bold')).place(x=320, y=10)
root.iconphoto(False, photo)
root.mainloop()
