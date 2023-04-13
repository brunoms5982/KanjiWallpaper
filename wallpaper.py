from kanjis import get_learn_kanjis, joyou_to_dict, get_review_kanjis
from PIL import Image, ImageFont, ImageDraw 
import numpy as np
from tqdm import tqdm
import os
import random
import cv2

all_kanjis = joyou_to_dict() #List
learn_kanjis = get_learn_kanjis() #List
review_dict_kanjis = get_review_kanjis() #Dictionary
review_list_kanjis = list(review_dict_kanjis.keys())
def kanji_found(kanji,kanji_list):
    if (kanji_list.count(kanji) != 0):
        return kanji
    else:
        return -1
def create_wallpaper():
    width = 1920
    height = 1080
    img = Image.new('RGB', (width, height), color='black')
    imgDraw = ImageDraw.Draw(img)
    line = 1
    column = 0
    linespace = 31
    columnspace = 30.5
    for count, value in enumerate(tqdm(all_kanjis)):
        message = value
        font = ImageFont.truetype("Meiryo.ttf", size=28)
        learn_found = kanji_found(value,learn_kanjis)
        review_found = kanji_found(value,review_list_kanjis)            
        if column <= 62:
            if learn_found!= -1:
                    #imgDraw.text((column*columnspace, 17+line*linespace), message, fill=(19, 61, 128),font=font) #Azul
                    imgDraw.text((column*columnspace, 17+line*linespace), message, fill=(255, 255, 255),font=font)
            elif review_found!= -1:
                    interval = review_dict_kanjis[review_found]
                    if interval <= 4:
                        imgDraw.text((column*columnspace, 17+line*linespace), message, fill=(242, 240, 104),font=font) #Amarelo
                    if interval > 4 and interval <= 30:
                        imgDraw.text((column*columnspace, 17+line*linespace), message, fill=(242, 134, 39),font=font) #Laranja
                    if interval > 30:
                        imgDraw.text((column*columnspace, 17+line*linespace), message, fill=(212, 21, 21),font=font) # Vermelho
                    #imgDraw.text((column*columnspace, 17+line*linespace), message, fill=(181, 0, 174),font=font) #Roxo
            else:
                #imgDraw.text((column*columnspace, 17+line*linespace), message, fill=(181, 174, 174),font=font) Cinza Claro
                imgDraw.text((column*columnspace, 17+line*linespace), message, fill=(41, 40, 40),font=font) #Cinza Escuro
            column+=1
        else:
            column = 0
            line += 1
            img.save('wallpaper.png', quality = 100)
        pass
        #gsettings set org.gnome.desktop.background picture-uri 'file:///home/user/Pictures/wallpapers/apple.jpg'
create_wallpaper()
    
    
source_path = 'wallpaper.png'
img = cv2.imread(source_path)
# Convert the image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the lower and upper bounds for the magenta color
lower_magenta = np.array([150, 100, 100])
upper_magenta = np.array([180, 255, 255])

# Define the lower and upper bounds for the blue color
lower_blue = np.array([100, 100, 100])
upper_blue = np.array([130, 255, 255])

# Create masks for the desired colors
mask_magenta = cv2.inRange(hsv_img, lower_magenta, upper_magenta)
mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)

value_added = 50
hsv_img[:,:,2][mask_blue!=0] += value_added
hsv_img[:,:,2][mask_magenta!=0] += value_added
merged_mask = cv2.bitwise_or(mask_blue, mask_magenta)

# Apply the mask to the original image
bgr_img = cv2.cvtColor(hsv_img, cv2.COLOR_HSV2BGR)
cv2.imwrite('wallpaper2.png', bgr_img)
