import face_recognition
import cv2
import os
import logging

def recognition_from_folder_webcam(path = './', videoId = 0):
	logging.basicConfig(filename='recognition_from_folder_webcam.log',
                format='%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S %p',
                level=10)
	video_capture = cv2.VideoCapture(videoId)
    # 初始化
	known_face_encodings = []
	known_face_names = []

	files= os.listdir(path) #得到文件夹下的所有文件名称
	for file in files:
		img_path = path +"/"+ file
		try:
			known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(img_path))[0])
		except:
			print(file + " image not support")
			logging.error(file + " image not support")
		else:
			known_face_names.append(file.split('.')[0])

	while True:
		ret, frame = video_capture.read()
		rgb_frame = frame[:, :, ::-1]
		face_locations = face_recognition.face_locations(rgb_frame)
		face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
		
		for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
			matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
			name = "Unknown"
			if True in matches:
				first_match_index = matches.index(True)
				name = known_face_names[first_match_index]
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
			cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
			print(name)
			logging.info("from video" + str(videoId) + " find " + name)
	    
		cv2.imshow('Video', frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	video_capture.release()
	cv2.destroyAllWindows()





def romance_video(imgPath = './',videoPath = './test.vi', frames = 25, framesWidth = 720, framesHeight = 404):
	logging.basicConfig(filename='romance_video.log',
                format='%(asctime)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S %p',
                level=10)
	mkdir("./output")
	input_movie = cv2.VideoCapture(videoPath)
	length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
 
	try:
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
		output_movie = cv2.VideoWriter('./output/output.avi', fourcc, frames, (framesWidth, framesHeight))  #帧数 大小
	except:
		print("Read video fail")
	
	known_face_encodings = []
	known_face_names = []
	
	files = os.listdir(imgPath) #得到文件夹下的所有文件名称
	for file in files:
		img_path = imgPath +"/"+ file

		try:
			known_face_encodings.append(face_recognition.face_encodings(face_recognition.load_image_file(img_path))[0])
		except:
			print(file + " image not support")
			logging.error(file + " image not support")
		else:
			known_face_names.append(file.split('.')[0])

	frame_number = 0
	import datetime
	starttime = datetime.datetime.now()
	print(starttime)
	while True:
		# Grab a single frame of video
		ret, frame = input_movie.read()
		frame_number += 1
		if not ret:
			break
		rgb_frame = frame[:, :, ::-1]
		face_locations = face_recognition.face_locations(rgb_frame)
		face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
		face_names = []
		for face_encoding in face_encodings:
			matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.50)
			name = "Unknown"
			if True in matches:
				first_match_index = matches.index(True)
				name = known_face_names[first_match_index]
	 
			face_names.append(name)
	 
	    # Label the results
		for (top, right, bottom, left), name in zip(face_locations, face_names):
			if not name:
				continue
			cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
			testImg = frame[top:bottom,left:right]
			cv2.imwrite('./output/test.png', testImg,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])
			cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
			font = cv2.FONT_HERSHEY_DUPLEX
			cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
			logging.info("from video" + videoPath + " find " + name + " at " + str((datetime.datetime.now() - starttime).seconds) + " s")
		output_movie.write(frame)
	endtime = datetime.datetime.now()
	print(endtime)
	print((endtime - starttime).seconds)
	input_movie.release()
	cv2.destroyAllWindows()





def mkdir(path):
	folder = os.path.exists(path)
	if not folder:             
		os.makedirs(path)            
		print("---  new folder...  ---")
		print("---  OK  ---")
	else:
		print("---  There is this folder!  ---")
