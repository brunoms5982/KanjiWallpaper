from kanjis import get_kanjis, joyou_to_dict
from PIL import Image, ImageFont, ImageDraw 
from tqdm import tqdm
import os

all_kanjis = joyou_to_dict()
kanjis = get_kanjis()
def kanji_found(kanji):
    if (kanjis.count(kanji) != 0):
        return True
    else:
        return False
def create_wallpaper():
    width = 1920
    height = 1080
    img = Image.new('RGB', (width, height), color='black')
    imgDraw = ImageDraw.Draw(img)
    line = 1
    column = 1
    for count, value in enumerate(tqdm(all_kanjis)):
        message = value
        font = ImageFont.truetype("HanaMinA.ttf", size=25)
        
        if (kanji_found(value)):
            color = 0
        else:
            color = 174
            
        if column <= 62:
            imgDraw.text((column*30, 15+line*30), message, fill=(181, color, 174),font=font)
            column+=1
        else:
            column = 1
            line += 1
            img.save('result.png', quality = 100)
        pass
    #os.system("gsettings set org.gnome.desktop.background picture-uri '/home/USER/Documents/KanjiWallpaper/result.png'")
create_wallpaper()
    
    
