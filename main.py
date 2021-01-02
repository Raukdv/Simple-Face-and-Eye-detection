import cv2 as cv


eye_cascade = cv.CascadeClassifier(cv.data.haarcascades+"haarcascade_eye.xml")
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")

#Another OS?
#cap = cv.VideoCapture(0)

#Windows solution
cap = cv.VideoCapture(0, cv.CAP_DSHOW)

while(1):
	_, frame = cap.read()
	grayscale = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

	faces = face_cascade.detectMultiScale(grayscale, 1.1, 4)

	for (x, y , w, h) in faces:
		cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
		roi_gray = grayscale[y:y+h, x:x+w]
		roi_color = frame[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)

	for (ex,ey,ew,eh) in eyes:
		cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

	cv.imshow('frame', frame)
	#Si se preciosa espacio, se cerrara el programa:

	k = cv.waitKey(32) & 0xFF
	if k == 32:
		break

cap.release()
cv.destroyAllWindows()






#Si tienes problemas con el numpy usa en la terminal: 
#python -c "import numpy;print(numpy.__version__);print(numpy.__file__)";
#Si tu version es de 1.19.4, desintalala e isntala pip install numpy==1.19.3
#Esto mitiga el siguiente error: 
#numpy fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information
