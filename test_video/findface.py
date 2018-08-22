import face_recognition
import cv2


input_movie = cv2.VideoCapture("video.mp4")
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))
 
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_movie = cv2.VideoWriter('output.avi', fourcc, 25, (1280, 720))  #帧数 大小

# Initialize some variables
face_locations = []
frame_number = 0
import datetime
 
starttime = datetime.datetime.now()
print(starttime)


while True:
    ret, frame = input_movie.read()
    frame_number += 1
 
    rgb_frame = frame[:, :, ::-1]
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
    for top, right, bottom, left in face_locations:
 
        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    #crop the frame
    #cropImg = cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    #cv2.imwrite('test.png',cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2))
    #print('test.png')
    
    #image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
        #cv2.imwrite(img_name, image,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    #cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
        #if there is a face in frame,intercept the face from frame and save to image
        testImg = frame[top:bottom,left:right]
        #output the img to  local
        cv2.imwrite('test.png', testImg,[int(cv2.IMWRITE_PNG_COMPRESSION), 9])
    #cv2.imwrite('test.png',cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2))
    #cv2.imwrite('test.png',cropImg)
    #cv2.imshow(cropImg)
    #print("test.png")
        # Draw a label with a name below the face
       
    output_movie.write(frame)
 
endtime = datetime.datetime.now()
print(endtime)
print((endtime - starttime).seconds)
input_movie.release()
cv2.destroyAllWindows()