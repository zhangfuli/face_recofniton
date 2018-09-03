import face_recognition
import cv2
import os

def recognition_from_folder_webcam(path = './', videoId = 0):
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
	    
	    cv2.imshow('Video', frame)
	    if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
    video_capture.release()
    cv2.destroyAllWindows()


# def romance_video(path, ):
# 	input_movie = cv2.VideoCapture("VI.avi")
# length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
 
# # Create an output movie file (make sure resolution/frame rate matches input video!)
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# output_movie = cv2.VideoWriter('output.avi', fourcc, 25, (720, 404))  #帧数 大小
 

# #lmm_image = face_recognition.load_image_file("lin-manuel-miranda.png")
# #lmm_face_encoding = face_recognition.face_encodings(lmm_image)[0]
 
# #al_image = face_recognition.load_image_file("alex-lacamoire.png")
# #al_face_encoding = face_recognition.face_encodings(al_image)[0]

# reporter_image = face_recognition.load_image_file("face.png")
# reporter_encoding = face_recognition.face_encodings(reporter_image)[0]

 
# known_faces = [
#     #lmm_face_encoding,
#     #al_face_encoding
#     reporter_encoding
# ]
 
# face_locations = []
# face_encodings = []
# face_names = []
# frame_number = 0
# import datetime
 
# starttime = datetime.datetime.now()
# print(starttime)
 
# while True:
#     # Grab a single frame of video
#     ret, frame = input_movie.read()
#     frame_number += 1
 
#     # Quit when the input video file ends
#     if not ret:
#         break
 
#     # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
#     rgb_frame = frame[:, :, ::-1]
 
#     # Find all the faces and face encodings in the current frame of video
#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
 
#     face_names = []
#     for face_encoding in face_encodings:
#         # See if the face is a match for the known face(s)
#         match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)
 
#         # If you had more than 2 faces, you could make this logic a lot prettier
#         # but I kept it simple for the demo
#         name = None
#         if match[0]:
#             name = "reporter"
#         # elif match[1]:
#         #     name = "Alex Lacamoire"
 
#         face_names.append(name)
 
#     # Label the results
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         if not name:
#             continue
 
#         # Draw a box around the face
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
# 	#crop the frame
# 	#cropImg = cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
# 	#cv2.imwrite('test.png',cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2))
# 	#print('test.png')
	
# 	#image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
#         #cv2.imwrite(img_name, image,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])
# 	#cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
#         #if there is a face in frame,intercept the face from frame and save to image
#         testImg = frame[top:bottom,left:right]
#         #output the img to  local
#         cv2.imwrite('test.png', testImg,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])
# 	#cv2.imwrite('test.png',cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2))
# 	#cv2.imwrite('test.png',cropImg)
# 	#cv2.imshow(cropImg)
# 	#print("test.png")
#         # Draw a label with a name below the face
#         cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
#         font = cv2.FONT_HERSHEY_DUPLEX
#         cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
 
#     # Write the resulting image to the output video file
#     #print("Writing frame {} / {}".format(frame_number, length))
#     output_movie.write(frame)
 
# # All done!
# endtime = datetime.datetime.now()
# print(endtime)
# print((endtime - starttime).seconds)
# input_movie.release()
# cv2.destroyAllWindows()



