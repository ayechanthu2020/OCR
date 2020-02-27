from pdf2image import convert_from_path


# Return total image count
def pdf_to_image(PDF_file, OUT_img_folder):
    """
    Part #1 : Converting PDF to images
    """
    try:
        print("Reading PDF File ...........")
        # Store all the pages of the PDF in a variable
        pages = convert_from_path(PDF_file, 500)

        # Counter to store images of each page of PDF to image
        image_counter = 1
        total_img = None

        # Iterate through all the pages stored above
        for page in pages:
            # Declaring filename for each page of PDF as JPG
            # For each page, filename will be:
            # PDF page 1 -> page_1.jpg
            # PDF page 2 -> page_2.jpg
            # PDF page 3 -> page_3.jpg
            # ....
            # PDF page n -> page_n.jpg
            filename = str(OUT_img_folder) + "/page_" + str(image_counter) + ".jpg"

            # Save the image of the page in system
            page.save(filename, 'JPEG')
            print(filename + " , Save ......")
            # Increment the counter to update filename
            image_counter = image_counter + 1

    except:
        print("PDF reader error....")
        return total_img

    total_img = image_counter - 1
    return total_img


# pdf_to_image("pdf_file/1.pdf", "image_save")
