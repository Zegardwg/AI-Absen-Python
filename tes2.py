from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import time
import csv

video = cv2.VideoCapture(0)
students = []

with open("eggar.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append(row[1])

print(students)

while True:
    check, frame = video.read()
    d = decode(frame)
    try:
        for obj in d:
            name = obj.data.decode()
            if name in students:
                students.remove(name)
                print(name, "telah melakukan presensi")
    except:
        print("error")

    cv2.imshow("attendance", frame)
    key = cv2.waitKey(1)
    if key == ord("q"):
        print("siswa belum presensi ", students)
        break

video.release()
cv2.destroyAllWindows()