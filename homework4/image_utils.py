from PIL import Image
import math

def pixelate(image, pixel_size = 10):
    new_img = Image.new('RGB', image.size)
    pixel1 = image.load()
    pixel2 = new_img.load()
    for i in range(0, image.size[0], pixel_size):
        for j in range(0, image.size[1], pixel_size):
            for r in range(pixel_size):
                for s in range(pixel_size):
                    try:
                        pixel2[i + r, j + s] = pixel1[i, j]
                    except IndexError:
                        continue
    return new_img


def kaleidoscope(image):
    lower_right = scale_down(image)
    lower_left = flip_horizontal(lower_right)
    upper_right = flip_vertical(lower_right)
    upper_left = flip_horizontal(upper_right)
    new_img = Image.new('RGB', image.size)
    pixel_new = new_img.load()
    pixelur = upper_right.load()
    pixelul = upper_left.load()
    pixellr = lower_right.load()
    pixelll = lower_left.load()
    for i in range(upper_right.size[0]):
        for j in range(upper_right.size[1]):
            pixel_new[i, j] = pixelur[i, j]
    for i in range(upper_right.size[0], image.size[0]):
        for j in range(image.size[1]):
            try:
                pixel_new[i, j] = pixelul[i - upper_right.size[0], j]
            except IndexError:
                continue
    for i in range(upper_right.size[0]):
        for j in range(upper_right.size[1], image.size[1]):
            try:
                pixel_new[i, j] = pixellr[i, j - upper_right.size[1]]
            except IndexError:
                continue
    for i in range(upper_right.size[0], image.size[0]):
        for j in range(upper_right.size[1], image.size[1]):
            try:
                pixel_new[i, j] = pixelll[i - upper_right.size[0], j - upper_right.size[1]]
            except IndexError:
                continue
    return new_img


def gray_day(image):
    pixels = image.load()
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            avg = sum(pixels[i, j]) // 3
            pixels[i, j] = (avg,) * 3
    return image


def righty(image):
    width, height = image.size
    img = Image.new("RGB", (height, width))
    pixels1 = image.load()
    pixels2 = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            pixels2[i, j] = pixels1[j, i]

    return flip_horizontal(img)


def scale_down(image, ratio = 2):
    width, height = image.size
    small_image = Image.new('RGB', (int(width / ratio), int(height/ ratio)))
    pixels1 = image.load()
    pixels2 = small_image.load()
    r, s = 0, 0
    for i in range(0, image.size[0], ratio):
        for j in range(0, image.size[1], ratio):
            try:
                pixels2[int(i / ratio), int(j / ratio)] = pixels1[i, j]
            except IndexError:
                continue
    return small_image


def flip_vertical(image):
    width, height = image.size
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    orig_pixels = image.load()
    for x in range(width):
        for y in range(height):
            clc_x, clc_y = x, height - y - 1
            t = clc_x, clc_y
            pixels[x, y] = orig_pixels[t]
    return img


def flip_horizontal(image):
    width, height = image.size
    img = Image.new('RGB', (width, height))
    pixels = img.load()
    orig_pixels = image.load()
    for x in range(width):
        for y in range(height):
            clc_x, clc_y = width - x - 1, y
            t = clc_x, clc_y
            pixels[x, y] = orig_pixels[t]
    return img


