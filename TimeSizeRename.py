import glob
import os
import time

image_path = 'C:/Users/shao7631/Pictures/夏目/'
labels = glob.glob(image_path + '*.jpg')
print(labels, len(labels))

for i in range(0, len(labels), 9):
    for file in labels[i:(i + 9)]:
        n = time.strftime("%y%m%d%H%M%S", time.localtime(os.path.getctime(file)))  # time.struct_time to str
        s = str(os.path.getsize(file))
        os.rename(file, image_path + n + '_' + s + '.jpg')
