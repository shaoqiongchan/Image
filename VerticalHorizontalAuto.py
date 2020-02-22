import os
from PIL import Image


def all_open(images):
    im_list = []
    for image_name in images:
        im_list.append(Image.open(image_name))
    return im_list


def crop(im_list, x, y):
    im_crop_list = []
    for im in im_list:
        width = im.size[0]
        height = im.size[1]
        im_crop = im.crop((width / 2 - x / 2, height / 2 - y / 2, width / 2 + x / 2, height / 2 + y / 2))
        im_crop_list.append(im_crop)
    return im_crop_list


def vertical(im_crop, name):
    x = im_crop[0].size[0]
    y = im_crop[0].size[1]
    im_vertical = Image.new('RGB', (x, y * len(im_crop)))
    for i in range(len(im_crop)):
        im_vertical.paste(im_crop[i], (0, y * i))
    im_vertical.save(name)


def horizontal(im_crop, name):
    x = im_crop[0].size[0]
    y = im_crop[0].size[1]
    im_vertical = Image.new('RGB', (x * len(im_crop), y))
    for i in range(len(im_crop)):
        im_vertical.paste(im_crop[i], (x * i, 0))
    im_vertical.save(name)


sign = 'nine'
image_path = "C:/Users/shao7631/Pictures/" + sign + "/"
image_names = [name for name in os.listdir(image_path) if name.endswith(('jpg', 'jpeg', 'png'))]
image_names.sort()
image_path_names = [image_path + name for name in image_names]

if __name__ == '__main__':
    for i in range(0, len(image_names), 9):
        image_list = all_open(image_path_names[i:(i + 9)])
        narrow = min(image_list[0].size[0], image_list[0].size[1])
        image_crop = crop(image_list, narrow * 0.8, narrow * 0.8)
        vertical(image_crop, "C:/Users/shao7631/Pictures/PIL/Vertical_" + image_names[i] + ".jpg")
        horizontal(image_crop, "C:/Users/shao7631/Pictures/PIL/Horizontal_" + image_names[i] + ".jpg")
