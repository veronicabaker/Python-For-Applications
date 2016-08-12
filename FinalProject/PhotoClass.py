from PIL import Image
import math


class Photo:
    def __init__(self, image):
        self.pixels = image.load
        self.height, self.width = image.size
        self.size = image.size


    def pixelate(self, pixel_size = 10):
        new_img = Image.new('RGB', self.size)
        pixel2 = new_img.load()
        for i in range(0, self.height, pixel_size):
            for j in range(0, self.width, pixel_size):
                for r in range(pixel_size):
                    for s in range(pixel_size):
                        try:
                            pixel2[i + r, j + s] = self.pixels[i, j]
                        except IndexError:
                            continue
        return new_img


    def kaleidoscope(self):
        lower_right = scale_down(image)
        lower_left = flip_horizontal(lower_right)
        upper_right = flip_vertical(lower_right)
        upper_left = flip_horizontal(upper_right)
        new_img = Image.new('RGB', self.size)
        pixel_new = new_img.load()
        pixelur = upper_right.load()
        pixelul = upper_left.load()
        pixellr = lower_right.load()
        pixelll = lower_left.load()
        for i in range(upper_right.size[0]):
            for j in range(upper_right.size[1]):
                pixel_new[i, j] = pixelur[i, j]
        for i in range(upper_right.size[0], self.size[0]):
            for j in range(self.size[1]):
                try:
                    pixel_new[i, j] = pixelul[i - upper_right.size[0], j]
                except IndexError:
                    continue
        for i in range(upper_right.size[0]):
            for j in range(upper_right.size[1], self.size[1]):
                try:
                    pixel_new[i, j] = pixellr[i, j - upper_right.size[1]]
                except IndexError:
                    continue
        for i in range(upper_right.size[0], self.size[0]):
            for j in range(upper_right.size[1], self.size[1]):
                try:
                    pixel_new[i, j] = pixelll[i - upper_right.size[0], j - upper_right.size[1]]
                except IndexError:
                    continue
        return new_img


    def gray_day(self):
        for i in range(self.height):
            for j in range(self.width):
                avg = sum(self.pixels[i, j]) // 3
                self.pixels[i, j] = (avg,) * 3
        return self


    def righty(self):
        width, height = self.size
        img = Image.new("RGB", (height, width))
        pixels2 = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                pixels2[i, j] = self.pixels1[j, i]

        return flip_horizontal(img)


    def scale_down(self, ratio = 2):
        small_image = Image.new('RGB', (int(self.width / ratio), int(self.height/ ratio)))
        pixels2 = small_image.load()
        r, s = 0, 0
        for i in range(0, self.width, ratio):
            for j in range(0, self.height, ratio):
                try:
                    pixels2[int(i / ratio), int(j / ratio)] = self.pixels[i, j]
                except IndexError:
                    continue
        return small_image


    def flip_vertical(self):
        img = Image.new('RGB', (self.width, self.height))
        pixels = img.load()
        for x in range(self.width):
            for y in range(self.height):
                clc_x, clc_y = x, self.height - y - 1
                t = clc_x, clc_y
                pixels[x, y] = self.pixels[t]
        return img


    def flip_horizontal(self):
        img = Image.new('RGB', (self.width, self.height))
        pixels = img.load()
        for x in range(self.width):
            for y in range(self.height):
                clc_x, clc_y = self.width - x - 1, y
                t = clc_x, clc_y
                pixels[x, y] = self.pixels[t]
        return img
