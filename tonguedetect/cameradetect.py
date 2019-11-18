import cv2
import time

def MyCameraDetect():
    # 加载人脸分类器
    faceCascade = cv2.CascadeClassifier('cascades/cascade.xml')
    # 调用摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    # 设置图片尺寸
    # cap.set(3, 640) # set Width
    # cap.set(4, 480) # set Height
    # 循环抓取图片
    while True:
        # 获取视频一帧图像
        ret, img = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # 将图像转换为灰度图像
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        tongues = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.25, #1.38
            minNeighbors=5,
            minSize=(20, 20)
        )
        if len(tongues) > 0 :
            count = 0
            for tongueRect in tongues:
                x, y, w, h = tongueRect
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 69, 255), 2)
                count += 1
                if (count == len(tongues)):
                    font = cv2.FONT_HERSHEY_PLAIN
                    cv2.putText(img, 'Count:%d/1 %d' % (count, len(tongues)), (x + 10, y + 20), font, 0.8, (226, 43, 138), 2)
                    print("We detected one tongue! %s" % time.time())
                    break
                    # cv2.imwrite('img/%s.png' % time.time(), img)
        else:
            font = cv2.FONT_HERSHEY_PLAIN
            cv2.putText(img, 'Not found!' , (10, 20), font, 0.8, (226, 43, 138), 2)

        cv2.imshow('video', img)

        k = cv2.waitKey(1)  # 控制相机拍照间隔
        if k == 27:  # press 'ESC' to quit
            break

    cap.release()
    cv2.destroyAllWindows()
