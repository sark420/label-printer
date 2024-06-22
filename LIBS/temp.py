import qrcode
import os
from PIL import Image,ImageFont,ImageDraw
def template(string_value,size2,string_value1):
    border_boxes = [(260, 65, 140, 120, 3, (0, 0, 0)),
                        (65,40, 150, 150, 1, (0, 0, 0)),
                        (40, 30, 400, 230, 1, (0, 0, 0)),
                        (85, 225, 300, 1, 1, (0, 0, 0))]

    img = qrcode.make(string_value)
        
    font3 = ImageFont.truetype("arial.ttf", 25)

    txt = f'{size2}'
    font = ImageFont.truetype("arial.ttf", 110)


                # Create a new image with fixed size for the QR code and space for the text
    new_img = Image.new('RGB', (188 + 112 + 180, 113 + 91 + 90), color="white")

                # Create a new ImageDraw object
    draw = ImageDraw.Draw(new_img)

                # Calculate the size of the text
    text_box_width= draw.textlength(txt, font=font)
    text_box_height = draw.textlength(txt, font=font)

                # Fixed size for the QR code
    fixed_qr_width = 180
    fixed_qr_height = 100

                # Calculate the positions based on the fixed size of the QR code
    qr_x = 50
    qr_y = 25
    txt_x = 200 + 70  # Adjust this value as needed
    txt_y = 25 + (195 - text_box_height) // 2

    if size2 == 0:
        font = ImageFont.truetype(os.path.join(os.getcwd(),"arial.ttf"), 90)
        txt = "FS"
        txt_x = 200 + 73  # Adjust this value as needed
        txt_y = 25 + (170 - text_box_height) // 2



    new_img.paste(img.resize((180, 180)), (qr_x, qr_y))
    draw.text((txt_x, txt_y), txt, font=font, fill="black")

    bordered_image = new_img

                # Create a drawing object
    draw = ImageDraw.Draw(bordered_image)

                        # Draw the border boxes
    for box in border_boxes:
                x, y, width, height, border_size, border_color = box

                            # Calculate the coordinates for the border rectangle
                x1 = x
                y1 = y
                x2 = x + width - 1
                y2 = y + height - 1

                            # Draw the border as a rectangle
                draw.rectangle([(x1, y1), (x2, y2)], outline=border_color, width=border_size)

                # Save the bordered image as a PNG file

    image = bordered_image
                    
                        # Create a drawing object
    draw = ImageDraw.Draw(image)
                        
                        # Define the text font and size
    font = ImageFont.truetype("arial.ttf", 36)
                        
                        # Get the text size
    text_width= draw.textlength(str(string_value), font)
    text_height = draw.textlength(str(string_value), font)
                
    text_width1= draw.textlength(string_value1, font)
    text_height1 = draw.textlength(string_value1, font)

    width = 500
    height = 230

    name = str(string_value)
    text_color = (0, 0, 0)  # Blue color
    font_size = 20

    font = ImageFont.truetype("arial.ttf", font_size)

    text_width= draw.textlength(name, font=font)
    text_height = draw.textlength(name, font=font)

    text_x = (width - text_width) // 2
    vertical_offset = 75  # Set the vertical offset here (in pixels)
    text_y = (height - text_height) // 2 + vertical_offset
    draw.text((text_x-10, 195), name, fill=text_color, font=font)

    name =string_value1
    font = ImageFont.truetype("arial.ttf", font_size)
    text_width= draw.textlength(name, font=font)
    text_height = draw.textlength(name, font=font)
    text_x = (width - text_width) // 2
    vertical_offset = 75  # Set the vertical offset here (in pixels)
    text_y = (height - text_height) // 2 + vertical_offset
    draw.text((text_x-12, 230), name, fill=text_color, font=font)


    logo1="                " 
    font3 = ImageFont.truetype("arial.ttf", 20)
    draw.text((220,38), logo1, font=font3, fill=(0, 0, 0))
    image.save("output.png")


    
    input_img = image
    new_width = 300
    new_height = 150  # Adjust this value as needed
    output_img = input_img.resize((int(new_width), int(new_height)))
    output_img.save("for_show_only.png")
#template('sjjjs2kks',36,'sdhhdk')