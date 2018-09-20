import sys
import getopt
from facere import * 

if __name__ == "__main__":
	# 从电脑自带摄像头实时识别
    recognition_from_folder_webcam("./imgs/", 0)

    # 将视频渲染
    #romance_video("./imgs/", "./video.mp4", 25, 1280, 720)