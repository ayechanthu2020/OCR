from PIL import Image
import pytesseract
import pyocr.builders
import textract
import cv2


def ocr_detection_pyocr(image_name, grey_image_out):
    img = cv2.imread(image_name)
    img = cv2.medianBlur(img, 5)

    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    blur = cv2.GaussianBlur(blur, (5, 5), 0)
    blur = cv2.GaussianBlur(blur, (5, 5), 0)

    blur = cv2.GaussianBlur(blur, (5, 5), 0)

    ret3, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    threshGauss = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 27)
    cv2.imwrite(str(grey_image_out) + "/pyocr_image_grey.jpg", threshGauss)
    image_gray = str(grey_image_out) + "/pyocr_image_grey.jpg"

    tools = pyocr.get_available_tools()[0]
    text = str(tools.image_to_string(Image.open(image_gray), builder=pyocr.builders.DigitBuilder()))  # image to string
    return text


def ocr_detection_pytesseract(image_name, grey_image_out):
    image_name = Image.open(image_name)
    image_name = image_name.convert('L')  # to greyscale
    image_name.save(str(grey_image_out) + "/pytesseract_image_grey.jpg")
    image_gray = str(grey_image_out) + "/pytesseract_image_grey.jpg"

    text = str(pytesseract.image_to_string(Image.open(image_gray)))  # image to string
    return text


def ocr_detection_textract(image_name, grey_image_out):
    image_name = Image.open(image_name)
    image_name = image_name.convert('L')  # to greyscale
    image_name.save(str(grey_image_out) + "/textract_image_grey.jpg")
    image_gray = str(grey_image_out) + "/textract_image_grey.jpg"

    text = str(textract.process(image_gray, encoding='ascii', method='tesseract'))  # image to string
    return text


def ocr_pyocr_img_to_text(image_name, OUT_File_Name):
    file = open(OUT_File_Name, "w+")  # Open file

    text = ocr_detection_pyocr(image_name, "greyscale_img")

    text = text.replace('-\n', '')
    file.write(text)
    file.close()


def ocr_pytesseract_img_to_text(image_name, OUT_File_Name):
    file = open(OUT_File_Name, "a")  # Open file

    text = ocr_detection_pytesseract(image_name, "greyscale_img")

    text = text.replace('-\n', '')
    file.write(text)
    file.close()


def ocr_textract_img_to_text(image_name, OUT_File_Name):
    file = open(OUT_File_Name, "a")  # Open file

    text = ocr_detection_textract(image_name, "greyscale_img")

    text = text.replace('-\n', '')
    file.write(text)
    file.close()


def is_ascii(s):
    return all(ord(c) < 128 for c in s)

# Creating a text file to write the output

# outfile1 = "out_file/out_pyocr.txt"
# outfile2 = "out_file/out_pytesseract.txt"
# outfile3 = "out_file/out_textract.txt"
#
# ocr_pyocr_img_to_text("crop_img/im_crop_right.jpg", outfile1)
# ocr_pytesseract_img_to_text("image_save/page_1.jpg", outfile2)
# ocr_textract_img_to_text("image_save/page_1.jpg", outfile3)
