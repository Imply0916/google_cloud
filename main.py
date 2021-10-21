from PIL import Image, ImageFilter
import threading


try:
    original = Image.open("ori.jpg")
except FileNotFoundError:
    print("Файл не найден")

def blurring(photo,name):
    blurred = photo.filter(ImageFilter.BLUR)
    #photo.show()
    blurred.show()
    blurred.save("blurred.jpg")



t3=threading.Thread(target=blurring,name='Thread3',args=(Image.open('ori.jpg'),'Thread3'))
t3.start()
#pip install --upgrade google-cloud-storage