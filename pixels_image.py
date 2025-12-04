from PIL import Image
import numpy as np

image = Image.open("images/test.png")

# Conversion de img en array numpy
img_array = np.array(image)


def afficher_pixel(x, y):
    pixel = img_array[y, x]  # y puis x comme ca dans numpy
    print(f"Pixel à ({x}, {y}) : {pixel}")


afficher_pixel(0, 0)
afficher_pixel(10, 10)
afficher_pixel(50, 50)