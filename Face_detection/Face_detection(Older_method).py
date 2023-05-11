import  cv2 as c
# for multiple face size is 900,650
cascade=c.CascadeClassifier('cascade_file/haarcascade_frontalface_alt.xml')
# image=c.imread('image/IMG_0494.JPG')
# image=c.resize(image,(900,650))
# imagegray=c.cvtColor(image,c.COLOR_BGR2GRAY)
# face=cascade.detectMultiScale(image,1.2,2)
# for(x,y,w,h) in face:
#     c.rectangle(image,(x,y),(x+w,y+h),(0,0,255),1)
# c.imshow('Detection',image)
# while True:


video=c.VideoCapture(0)
video.set(3,900)
video.set(4,650)
while True:
    sc,im=video.read()
    face = cascade.detectMultiScale(im, 1.2, 2)
    for (x, y, w, h) in face:
     c.rectangle(im,(x,y),(x+w,y+h),(0,0,255),1)
    c.imshow('Video',im)
    if(c.waitKey(1) & 0xFF==ord('z')):
        break;
