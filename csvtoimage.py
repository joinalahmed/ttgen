import PIL
import PIL.Image
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw

PIXEL_ON = 0  # PIL color to use for "on"
PIXEL_OFF = 255  # PIL color to use for "off"


def main():
    image = text_image('../../Desktop/test/correct_output.txt')
    image.show()
    image.save('../../Desktop/test/content.png')


def text_image(text_path, font_path=None):
    grayscale = 'L'
    with open(text_path) as text_file:
        lines = tuple(l.rstrip() for l in text_file.readlines())
    large_font = 150
    font_path = font_path or 'FreeMono.ttf'
    try:
        font = PIL.ImageFont.truetype(font_path, size=large_font,encoding="unic")
    except IOError:
        font = PIL.ImageFont.load_default()
        print('Could not use chosen font. Using default.')

    pt2px = lambda pt: int(round(pt * 96.0 / 72))
    max_width_line = max(lines, key=lambda s: font.getsize(s)[0])
    test_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    max_height = pt2px(font.getsize(test_string)[1])
    max_width = pt2px(font.getsize(max_width_line)[0])
    height = max_height * len(lines)
    width = int(round(max_width + 40))
    image = PIL.Image.new(grayscale, (width, height), color=PIXEL_OFF)
    draw = PIL.ImageDraw.Draw(image)
    vertical_position = 8
    horizontal_position = 8
    line_spacing = int(round(max_height * 1))  # reduced spacing seems better
    for line in lines:
        draw.text((horizontal_position, vertical_position),
                  line, fill=PIXEL_ON, font=font)
        vertical_position += line_spacing
    c_box = PIL.ImageOps.invert(image).getbbox()
    image = image.crop(c_box)
    return image


if __name__ == '__main__':
    main()
