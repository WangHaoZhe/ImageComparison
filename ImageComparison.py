from PIL import Image
from PIL import ImageChops


path_one = r'C:\Users\13521\Desktop\ImageComparison\data\original\1.jpg'  # 原图片
path_two = r'C:\Users\13521\Desktop\ImageComparison\data\changed\2.jpg'  # 输入图片
diff_save_location = r'C:\Users\13521\Desktop\ImageComparison\data\difference\difference.jpg'  # 差异


def compare_images(image1, image2, difference):
    image_one = Image.open(image1)
    image_two = Image.open(image2)
    diff = ImageChops.difference(image_one, image_two)
    if diff.getbbox() is not None:
        diff.save(difference)


compare_images(path_one, path_two, diff_save_location)
