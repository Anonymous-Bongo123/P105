import os
import cv2
path="Images"
image=[]
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        image.append(file_name)
print(len(image))
count = len(image)
frame=cv2.imread(image[0])
height, width, channels = frame.shape
size=(width, height)
output=cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"DIVX"), 0.8, size)
for i in range(count-1, 0, -1):
    frame=cv2.imread(image[i])
    output.write(frame)
output.release()