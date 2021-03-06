from PIL import Image
import glob, os
dirs='/home/joy/Desktop/test/tfc/'
print dirs
os.chdir("/home/joy/Desktop/test/tfc/")
for files in glob.glob("*.jpg"):
    filename = dirs + files
    print files
    img = Image.open(filename, 'r')
    img_w, img_h = img.size
    background = Image.new('RGBA', (721, 381), (255, 255, 255, 255))
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)
    background.paste(img, offset)
    background.show()
    background.save(filename)