# Edited from the https://blog.csdn.net/Shea1992/article/details/83592899
from imagedetect import MyImageDetect
from cameradetect import MyCameraDetect
import sys

def main():
    print
    'The command line arguments are:'
    for i in sys.argv:
        print(i)
    # Image detect
    srcfile = sys.argv[1]
    MyImageDetect(srcfile)

    # Camera detect
    #MyCameraDetect()


if __name__ == '__main__':
    main()
