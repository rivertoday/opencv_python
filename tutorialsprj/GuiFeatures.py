def ImageBasic(pic_name):
    import cv2 as cv

    # Load an color image in grayscale
    if pic_name == '':
        pic_name = 'pics/lena.jpg'

    fullpath = pic_name.split("/", 1) #分割成两部分
    savefilename = fullpath[0] + "/gray" + fullpath[1]

    img = cv.imread(pic_name, cv.IMREAD_COLOR)

    imggray = cv.imread(pic_name, cv.IMREAD_GRAYSCALE)#or 0
    cv.namedWindow('imagegray', cv.WINDOW_NORMAL)
    cv.namedWindow('image', cv.WINDOW_NORMAL)
    cv.imshow('imagegray', imggray)
    cv.imshow('image', img)
    k = cv.waitKey(0)
    if k == 27:  # wait for ESC key to exit
        cv.destroyAllWindows()
    elif k == ord('s'):  # wait for 's' key to save and exit
        cv.imwrite(savefilename, imggray)
        cv.destroyAllWindows()

def MatplotTest(pic_name):
    import cv2 as cv
    from matplotlib import pyplot as plt

    # Load an color image in grayscale
    if pic_name == '':
        pic_name = 'pics/lena.jpg'

    img = cv.imread(pic_name, 0)
    plt.imshow(img, cmap='gray', interpolation='bicubic')
    plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
    plt.show()

def VideoOperations():
    import cv2 as cv
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Our operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # Display the resulting frame
        cv.namedWindow('frame', cv.WINDOW_NORMAL)
        cv.namedWindow('gray', cv.WINDOW_NORMAL)
        cv.imshow('frame', frame)
        cv.imshow('gray', gray)
        k = cv.waitKey(1)
        if (k == 27) or (k == ord('q')):  # wait for ESC key to exit
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()

def PlayVideo():
    import cv2 as cv
    cap = cv.VideoCapture('videos/video.avi')
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

def SaveVideo():
    import cv2 as cv
    cap = cv.VideoCapture(0)
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('videos/output1.avi', fourcc, 20.0, (640, 480))
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        #frame = cv.flip(frame, 0)
        # write the flipped frame
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows()