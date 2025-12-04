from PIL import Image

image = Image.open("images/test.png")
image.show()

print(f"Dimensions : {image.size}")
print(f"Mode : {image.mode}")