from PIL import Image

# Load a grayscale image of Suzanne (e.g. side-lit so it has depth)
img = Image.open("Rasterizer.png").convert("L")  # "L" = grayscale
img.save("DepthMap.png")
img.show()
