# import openpyxl
# filename = 'format_file.xlsx'
# wb = openpyxl.load_workbook(filename)
# ws = wb['01']
# img_name = 'img/Picture1.png'
# img = openpyxl.drawing.image.Image(img_name)
# img.anchor = 'C12' # Or whatever cell location you want to use.
# ws.add_image(img)
# wb.save(filename)
#
from PIL import Image, ImageOps
import cv2

#Resize Image
img_name = Image.open('img/im_crop_bottom_graph.jpg')
width = 920 #640
height = 65 #245
dim = (width, height)
resizeImg = img_name.resize(dim)
resizeImg.save('img/im_crop_bottom_graph_resize.jpg')

# Adding Border to Image
img = Image.open('img/im_crop_bottom_graph_resize.jpg')
img_with_border = ImageOps.expand(img, border=1, fill='black')
img_with_border.save('img/im_crop_bottom_graph_resize_border.jpg')