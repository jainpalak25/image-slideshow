# Image Slideshow
A simple GUI-based Image Slideshow application built using Python's tkinter library and Pillow for image processing. This application allows you to display images in a slideshow format with a smooth transition effect.

Features
Slideshow Display: Automatically displays images in a loop.
Transition Effect: Images slide with a fade effect for a smooth visual experience.
Customizable Paths: Easily add or change images by modifying the file paths in the code.

Requirements
Python 3.x

Libraries:
tkinter (usually included with Python)
Pillow for handling image processing and display

Installation
Clone the Repository:
git clone https://github.com/palakjain/image-slideshow.git
Navigate to the Project Directory:
cd image-slideshow

Install Required Libraries:
pip install pillow

Usage
Add Images: Place the images you want to display in the slideshow inside the project folder or update the paths directly in image-slideshow.py.

Run the Application:

python image-slideshow.py

The application window will open and start displaying images in a loop with a fade transition effect.

Code Overview
Slider Class: The core of the slideshow functionality, handling image loading, resizing, and display transitions.
Main Application Loop: Initializes the tkinter root window and starts the slideshow.
Customization
Add More Images:
To add more images, add their paths in the image_paths list inside Slider.__init__ method.
Change Transition Speed:
Adjust the self.root.after(2000, self.slider_func) line to increase or decrease the delay between transitions.
File Structure
bash
Copy code
Image-Slideshow/
├── image-slideshow.py     # Main application file
├── README.md              # This README file
├── lakes.png              # Sample image
├── mountains.jpg          # Sample image
└── gallery.png            # Application icon image
Dependencies
tkinter: Standard Python GUI library.
Pillow: Library for advanced image processing. Pillow Documentation
