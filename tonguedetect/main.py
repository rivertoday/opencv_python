import cv2
import time
#加载人脸分类器
faceCascade = cv2.CascadeClassifier('cascades/cascade.xml')
#调用摄像头
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
#设置图片尺寸
# cap.set(3, 640) # set Width
# cap.set(4, 480) # set Height
#循环抓取图片
while True:
    # 获取视频一帧图像
    ret, img = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # 将图像转换为灰度图像
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.38,
        minNeighbors=4,
        minSize=(20, 20)
    )
    count=0
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 69, 255), 2)
        count+=1
        if(count==len(faces)):
            print("We detected one tongue! %s"%time.time())
            #cv2.imwrite('img/%s.png' % time.time(), img)
            cv2.imshow('video', img)

    k = cv2.waitKey(1) #控制相机拍照间隔
    if k == 27: # press 'ESC' to quit
        break
