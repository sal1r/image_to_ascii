from PIL import Image
import sys

def main():
    # chars = list(' ░▒▓█')
    chars = list(' .-*+=%$&@#ШЖ')

    def get_brightness(color: tuple):
        return 0.299*color[0] + 0.587*color[1] + 0.114*color[2]

    if len(sys.argv) != 2:
        raise RuntimeError("Error. You must input file name!")

    im = Image.open(sys.argv[1])
    im = im.resize((300, 100))
    out = []

    for y in range(im.height):
        for x in range(im.width):
            col = im.getpixel((x, y))
            br = get_brightness(col)
            
            br_proc = br / 255
            step = 255 / len(chars)
            char = chars[int((len(chars)-1) * br_proc)]
            out.append(char)

    for y in range(im.height):
        string = ''
        for x in range(im.width):
            string += out[y * im.width + x]
        print(string)

if __name__ == '__main__':
    main()