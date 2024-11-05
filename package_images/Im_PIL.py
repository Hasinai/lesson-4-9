import random
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
from PIL.ImageFilter import (
    BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE,
    EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN
)

class ImageReader:
    def __init__(self, file_name: str):
        self.image = Image.open(file_name)
        self.draw = ImageDraw.Draw(self.image)
        self.width = self.image.size[0]
        self.height = self.image.size[1]
        self.pix = self.image.load()

    def show_image(self):
        plt.imshow(self.image)
        plt.show()

    def get_info(self):
        return {
            "image_file": self.image,
            "image_draw": self.draw,
            "image_width": self.width,
            "image_height": self.height,
            "image_pix": self.pix
        }

class Monochrome:
    def __init__(self, file_name_start: str):
        self.image_info = ImageReader(file_name_start).get_info()
        self.image = self.image_info["image_file"]
        self.draw = self.image_info["image_draw"]
        self.width = self.image_info["image_width"]
        self.height = self.image_info["image_height"]
        self.pix = self.image_info["image_pix"]

    def apply_monochrome(self, factor: int):
        for i in range(self.width):
            for j in range(self.height):
                a = self.pix[i, j][0]
                b = self.pix[i, j][1]
                c = self.pix[i, j][2]
                S = a + b + c
                if S > (((255 + factor) // 2) * 3):
                    a, b, c = 255, 255, 255
                else:
                    a, b, c = 0, 0, 0
                self.draw.point((i, j), (a, b, c))
        
        #self.show_image()

    def save_image(self, file_name_stop: str):
        self.image.save(file_name_stop, "JPEG")

    # def show_image(self):
    #     plt.imshow(self.image)
    #     plt.show()

# Class for applying filters to images
class Vector:
    def __init__(self, file_name_start: str):
        self.image_info = ImageReader(file_name_start).get_info()
        self.image = self.image_info["image_file"]
        self.draw = self.image_info["image_draw"]

    def apply_filter(self, filter_type):
        self.image = self.image.filter(filter_type)
        #self.show_image()

    def save_image(self, file_name_stop: str):
        self.image.save(file_name_stop, "JPEG")

    # def show_image(self):
    #     plt.imshow(self.image)
    #     plt.show()
