import numpy as np
import cv2
from PIL import ImageGrab
forcc=cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('screenrec.avi', forcc, 10, (1366,768))

while True:
    img=ImageGrab.grab()
    img_np=np.array(img)
    frame=cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Screen',frame)
    out.write(frame)
    if cv2.waitKey(1)==27:
        break

cv2.destroyAllWindows()
