from PIL import Image
from PIL import ImageChops
import math
import operator
from functools import reduce

path_one = r'C:\Users\13521\Desktop\ImageComparison\data\original\1.jpg'  # 原图片
path_two = r'C:\Users\13521\Desktop\ImageComparison\data\changed\2.jpg'  # 输入图片
diff_save_location = r'C:\Users\13521\Desktop\ImageComparison\data\difference\difference.jpg'  # 差异


def compare_images(image1, image2, difference):
    image_one = Image.open(image1)
    image_two = Image.open(image2)
    diff = ImageChops.difference(image_one, image_two)
    if diff.getbbox() is not None:
        diff.save(difference)


def image_contrast(image1, image2):

    image1 = Image.open(image1)
    image2 = Image.open(image2)

    h1 = image1.histogram()
    h2 = image2.histogram()

    result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
    return result


compare_images(path_one, path_two, diff_save_location)
result = image_contrast(path_one, path_two)
print(result)
