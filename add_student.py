import cv2
import os

# Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Ask user for enrollment and name
enrollment = input("Enter Enrollment ID: ")
name = input("Enter Name: ")
folder_name = f"known_faces/{enrollment}_{name}"
os.makedirs(folder_name, exist_ok=True)

# Start webcam
cap = cv2.VideoCapture(0)
img_count = 0
max_images = 10

print(f"\n📸 Capturing {max_images} images. Look at the camera...")

while img_count < max_images:
    ret, frame = cap.read()
    if not ret:
        print("❌ Failed to capture frame")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_img = frame[y:y+h, x:x+w]
        img_path = os.path.join(folder_name, f"{name}_{img_count}.jpg")
        cv2.imwrite(img_path, face_img)
        img_count += 1
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.putText(frame, f"Images Captured: {img_count}/{max_images}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Capturing Faces", frame)
    cv2.waitKey(1)

print(f"\n✅ Done! {img_count} face images saved in '{folder_name}'")

cap.release()
cv2.destroyAllWindows()
