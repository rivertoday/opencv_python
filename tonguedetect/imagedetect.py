import numpy as np
import cv2

def MyImageDetect(srcfile):
    faceCascade = cv2.CascadeClassifier('cascades/cascade.xml')
    img = cv2.imread(srcfile)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.38,#该参数需要根据自己训练的模型进行调参
            minNeighbors=4,#minNeighbors控制着误检测，默认值为3表明至少有3次重叠检测，我们才认为人脸确实存
            minSize=(20,20),#寻找人脸的最小区域。设置这个参数过大，会以丢失小物体为代价减少计算量。
            flags = cv2.IMREAD_GRAYSCALE
        )
    for (x, y, w, h) in faces:
        print("Found the tongue: x-%d,y-%d" % (x, y))
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cropImg = img[y:(y+h), x:(x + w)]  # 获取感兴趣区域
        cv2.imwrite(srcfile+".crop.jpg", cropImg)  # 保存到指定目录

    cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('image',img)
    cv2.namedWindow('newimage', cv2.WINDOW_AUTOSIZE)
    newimg = cv2.imread(srcfile+".crop.jpg")
    cv2.imshow('newimage', newimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
