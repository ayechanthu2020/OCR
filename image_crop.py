from PIL import Image, ImageOps
import ocr_detection


def image_to_data(imagePath, count):
    # Opens a image in RGB mode
    img = Image.open(imagePath)

    im_crop_graph = img.crop((0, 283, 3488, 1936))  # left, top, right, bottom
    im_crop_bottom_graph = img.crop((0, 2543, 5848, 2881))  # left, top, right, bottom

    im_crop_refIndex = img.crop((5062, 1439, 5500, 1520))  # left, top, right, bottom
    im_crop_acqRange = img.crop((5062, 1582, 5500, 1670))  # left, top, right, bottom
    im_crop_lastData = img.crop((5062, 1738, 5500, 1819))  # left, top, right, bottom
    im_crop_sampleReso = img.crop((5062, 1813, 5500, 1890))  # left, top, right, bottom
    im_crop_pulsWidth = img.crop((5062, 1890, 5500, 1962))  # left, top, right, bottom

    im_crop_xkm_div = img.crop((944, 1920, 1700, 2009))  # left, top, right, bottom
    im_crop_distance = img.crop((446, 2762, 859, 2843))  # left, top, right, bottom

    im_crop_graph.save("crop_img/im_crop_graph.jpg")
    im_crop_bottom_graph.save("crop_img/im_crop_bottom_graph.jpg")

    im_crop_refIndex.save("crop_img/im_crop_refIndex.jpg")
    im_crop_acqRange.save("crop_img/im_crop_acqRange.jpg")
    im_crop_lastData.save("crop_img/im_crop_lastData.jpg")
    im_crop_sampleReso.save("crop_img/im_crop_sampleReso.jpg")
    im_crop_pulsWidth.save("crop_img/im_crop_pulsWidth.jpg")

    im_crop_xkm_div.save("crop_img/im_crop_xkm_div.jpg")
    im_crop_distance.save("crop_img/im_crop_distance.jpg")

    resize_border_firstImg("crop_img/im_crop_graph.jpg", count)
    resize_border_secondImg("crop_img/im_crop_bottom_graph.jpg", count)

    ref_index_txt = ocr_detection.ocr_detection_pyocr("crop_img/im_crop_refIndex.jpg", "greyscale_img")
    acq_range_txt = ocr_detection.ocr_detection_pyocr("crop_img/im_crop_acqRange.jpg", "greyscale_img")
    last_data_txt = ocr_detection.ocr_detection_pyocr("crop_img/im_crop_lastData.jpg", "greyscale_img")
    sampleReso_txt = ocr_detection.ocr_detection_pyocr("crop_img/im_crop_sampleReso.jpg", "greyscale_img")
    puls_width_txt = ocr_detection.ocr_detection_pyocr("crop_img/im_crop_pulsWidth.jpg", "greyscale_img")
    xkm_div_txt = ocr_detection.ocr_detection_pyocr("crop_img/im_crop_xkm_div.jpg", "greyscale_img")
    distance_txt = ocr_detection.ocr_detection_pyocr("crop_img/im_crop_distance.jpg", "greyscale_img")

    # print("ref_index =>", ref_index_txt)
    # print("acq_range =>", acq_range_txt)
    # print("last_data =>", last_data_txt)
    # print("sample_resolution =>", sampleReso_txt)
    # print("puls_width =>", puls_width_txt)
    # print("xkm_div_txt =>", xkm_div_txt)
    # print("distance_txt =>", distance_txt)

    return ref_index_txt, acq_range_txt, last_data_txt, sampleReso_txt, puls_width_txt, xkm_div_txt, distance_txt

def resize_border_firstImg(imgPath, count):
    # Resize Image
    img_name = Image.open(imgPath)
    width = 640
    height = 245
    dim = (width, height)
    resizeImg = img_name.resize(dim)
    img_with_border = ImageOps.expand(resizeImg, border=1, fill='black')
    img_with_border.save('first_graph_img/firstImg_' + str(count) + '.jpg')


def resize_border_secondImg(imgPath, count):
    # Resize Image
    img_name = Image.open(imgPath)
    width = 920  # 640
    height = 65  # 245
    dim = (width, height)
    resizeImg = img_name.resize(dim)
    img_with_border = ImageOps.expand(resizeImg, border=1, fill='black')
    img_with_border.save('second_graph_img/secondImg_' + str(count) + '.jpg')


# data = image_to_data("image_save/page_2.jpg")
# print(data)