import cv2
import ocr_detection

def adaptive_threshold(plates):

    for i, plate in enumerate(plates):
        img = cv2.imread(plate)

        gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        # cv2.imshow('gray', gray)

        ret, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
        # cv2.imshow('thresh', thresh)

        threshMean = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)
        # cv2.imshow('threshMean', threshMean)

        threshGauss = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 27)
        # cv2.imshow('threshGauss', threshGauss)
        cv2.imwrite("processed/plate{}.png".format(i), threshGauss)

        cv2.waitKey(0)


# img = cv2.imread("crop_img/im_crop_right.jpg")
# img = cv2.medianBlur(img, 5)
# img = cv2.medianBlur(img, 5)
#
# gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
# cv2.imshow('gray', gray)
#
# blur = cv2.GaussianBlur(gray, (5, 5), 0)
# ret3, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
# cv2.imshow("th3", thresh)
#
# threshGauss = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 51, 27)
# cv2.imshow('threshGauss', threshGauss)
#
# cv2.imwrite("adpt_img.jpg", threshGauss)

# text = ocr_detection.ocr_detection_pyocr("crop_img/im_crop_right.jpg", "greyscale_img")
# print("pyocr \n------\n", text)
# text = ocr_detection.ocr_detection_pytesseract("crop_img/im_crop_right.jpg", "greyscale_img")
# print("pytesseract \n------\n", text)
# text = ocr_detection.ocr_detection_textract("crop_img/im_crop_right.jpg", "greyscale_img")
# print("textract \n------\n", text)

cv2.waitKey(0)