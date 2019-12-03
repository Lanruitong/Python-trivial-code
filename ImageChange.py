from PIL import Image


def produceImage(file_in, width, height, file_out):
    image = Image.open(file_in)
    resized_image = image.resize((width, height), Image.ANTIALIAS)
    resized_image.save(file_out)


if __name__ == '__main__':
    file_in = 'D:/wuziqi.jpg'
    width = 500
    height = 500
    file_out = 'D:/wuziqi1.jpg'
    produceImage(file_in, width, height, file_out)
