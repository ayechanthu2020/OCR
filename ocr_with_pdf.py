from PIL import Image
import pytesseract
from pdf2image import convert_from_path
import pyocr
import pyocr.builders
import textract

# Path of the pdf
PDF_file = "pdf_file/2.pdf"

''' 
Part #1 : Converting PDF to images 
'''

# Store all the pages of the PDF in a variable
pages = convert_from_path(PDF_file, 500)

# Counter to store images of each page of PDF to image
image_counter = 1

# Iterate through all the pages stored above
for page in pages:
    # Declaring filename for each page of PDF as JPG
    # For each page, filename will be:
    # PDF page 1 -> page_1.jpg
    # PDF page 2 -> page_2.jpg
    # PDF page 3 -> page_3.jpg
    # ....
    # PDF page n -> page_n.jpg
    filename = "image_save/page_" + str(image_counter) + ".jpg"

    # Save the image of the page in system
    page.save(filename, 'JPEG')

    # Increment the counter to update filename
    image_counter = image_counter + 1


''' 
Part #2 - Recognizing text from the images using OCR 
'''

# Variable to get count of total number of pages
filelimit = image_counter - 1

# Creating a text file to write the output
outfile1 = "out_file/out_text1.txt"
outfile2 = "out_file/out_text2.txt"
outfile3 = "out_file/out_text3.txt"

# Open the file in append mode so that
# All contents of all images are added to the same file
f1 = open(outfile1, "a")
f2 = open(outfile2, "a")
f3 = open(outfile3, "a")

# Iterate from 1 to total number of pages
for i in range(1, filelimit + 1):
    # Set filename to recognize text from
    # Again, these files will be:
    # page_1.jpg
    # page_2.jpg
    # ....
    # page_n.jpg
    filename = "image_save/page_" + str(i) + ".jpg"

    img = Image.open(filename)
    img = img.convert('L')
    img.save(filename)

    # Recognize the text as string in image using pytesserct
    # text = str(((pytesseract.image_to_string(Image.open(filename)))))

    text1 = str(pytesseract.image_to_string(Image.open(filename)))
    text2 = str(textract.process(filename, encoding='ascii',
                            method='tesseract'))

    tools = pyocr.get_available_tools()[0]
    text3 = str(tools.image_to_string(Image.open(filename),
                                 builder=pyocr.builders.DigitBuilder()))

    # The recognized text is stored in variable text
    # Any string processing may be applied on text
    # Here, basic formatting has been done:
    # In many PDFs, at line ending, if a word can't
    # be written fully, a 'hyphen' is added.
    # The rest of the word is written in the next line
    # Eg: This is a sample text this word here GeeksF-
    # orGeeks is half on first line, remaining on next.
    # To remove this, we replace every '-\n' to ''.

    text1 = text1.replace('-\n', '')
    f1.write(text1)
    text2 = text2.replace('-\n', '')
    f2.write(text2)
    text3 = text3.replace('-\n', '')
    f3.write(text3)

# Close the file after writing all the text.
f1.close()
f2.close()
f3.close()
