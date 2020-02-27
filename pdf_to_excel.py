import pdf_to_image
import image_crop
import shutil
import openpyxl

import datetime
now = datetime.datetime.now()
currentTime = now.strftime("%Y-%m-%d_%H:%M:%S")


sourceExcelFile = 'excel_original/format_file.xlsx'
destinationExcelFile = 'excel_outfile/outfile_'+ currentTime + '.xlsx'
shutil.copy(sourceExcelFile, destinationExcelFile )

excelFileName = destinationExcelFile
book = openpyxl.load_workbook(excelFileName)

pdf_to_image.pdf_to_image("pdf_file/2.pdf", "image_save")

# for i in range(1, 13):
i = 1
for sheet in book.worksheets:
    print(str(sheet.title))

    ref_index_txt, acq_range_txt, last_data_txt, sampleReso_txt, puls_width_txt, xkm_div_txt, distance_txt = image_crop.image_to_data(
        "image_save/page_" + str(i) + ".jpg", i)

    str_meter = sampleReso_txt
    str_meter = str_meter.split('m')
    str_centimeter = float(str_meter[0]) * 100
    # print(str(int(str_centimeter)) + " cm")

    sheet['D4'] = str(round(float(distance_txt), 3)) + " km"
    sheet['F25'] = xkm_div_txt
    sheet['K25'] = "SMP: " + str(int(str_centimeter)) + " cm"
    sheet['L25'] = last_data_txt
    sheet['D28'] = acq_range_txt
    sheet['D29'] = puls_width_txt
    sheet['D32'] = ref_index_txt

    img_name = 'first_graph_img/firstImg_' + str(i) + '.jpg'
    img = openpyxl.drawing.image.Image(img_name)
    img.anchor = 'C12'  # Or whatever cell location you want to use.
    sheet.add_image(img)

    img_name = 'second_graph_img/secondImg_' + str(i) + '.jpg'
    img = openpyxl.drawing.image.Image(img_name)
    img.anchor = 'A36'  # Or whatever cell location you want to use.
    sheet.add_image(img)

    i += 1


book.save(excelFileName)
# print("page_" + str(i) + ".jpg" , data)
