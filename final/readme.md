### face_recognition函数封装

### 使用说明
###### 首先安装face_recognition
	pip install face_recognition

###### 采集照片时, 人脸信息完整, 推荐使用windows自带相机采集相片, 当出现蓝框时照片正常(见imgs/example.png)


### 函数说明
##### recognition_from_folder_webcam(path, videoId)
###### 参数：path  图片文件夹路径, 默认当前路径; videoId 摄像头号, 默认0
###### 从文件夹下读取照片并对文件夹内的图片, 进行实时识别并根据文件夹中图片名进行标示, 并生成日志文件recognition_from_folder_webcam.log
###### 例子： recognition_from_folder_webcam("./imgs", 0)


##### romance_video(imgPath, videoPath, frames, framesWidth, framesHeight)
###### 参数：imgPath图片文件夹路径, videoPath视频路径, frames帧数, framesWidth帧宽度, framesHeight帧高度
###### 读取视频，并根据图片文件加夹中的图片进行识别在视频中渲染，结果在output文件夹, 并生成日志文件romance_video.log
###### 例子：romance_video("./imgs/", "./video.mp4", 25, 1280, 720)


### 代码实例
###### 见main.py