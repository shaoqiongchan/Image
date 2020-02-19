import cv2
import os
import numpy as np

sign = 'May van Millingen'
image_path = 'C:/Users/shao7631/Pictures/' + sign + '/'
print(image_path)
image_names = [image_path + name for name in os.listdir(image_path) if
               name.startswith(sign) or name.endswith(('jpg', 'jpeg', 'png'))]

print(image_names)
print('共{}张图片'.format(len(image_names)))
image_list = []
x_list = []
y_list = []
images = []

for name in image_names:
    img = cv2.imread(name)
    print(type(img))
    image_list.append(img)
    x_list.append(img.shape[1])
    y_list.append(img.shape[0])
    images.append(img, img.shape[1], img.shap[0])

try:
    I = np.vstack(image_list)
    cv2.imwrite(image_path + 'v_' + sign + '.jpg', I)
except:
    print('宽度不同：{}'.format(x_list))
    sorted(images, key=lambda image: image[1])
try:
    h = np.hstack(image_list)
    cv2.imwrite(image_path + 'h_' + sign + '.jpg', h)
except:
    print('高度不同：{}'.format(y_list))
