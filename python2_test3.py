import PIL
import qrcode


def aspect_ratio(ox,oy):
    x, y = ox, oy
    while y:
        x, y = y, x % y
    return (ox/x, oy/x)


def print_img_size(img):
    width, height = img.size
    print('横:', width)
    print('縦:', height)
    print('アスペクト比:',aspect_ratio(width,height))
    

print_img_size(qrcode.make("http://a-force.biz"))