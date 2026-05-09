import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread("fruits.jpg")

(h,w)=image.shape[:2]
CENTRE=(w//2,h//2)
m=cv2.getRotationMatrix2D(CENTRE, 60, 1.0)
rotated_img=cv2.warpAffine(image,m,(w,h))
rotated_rgb=cv2.cvtColor(rotated_img, cv2.COLOR_BGR2RGB)

plt.imshow(rotated_rgb)
plt.title("Rotated Image")
plt.show()

brightness_matrix=np.ones(image.shape,dtype="uint8")*80
brightness_img=cv2.add(image, brightness_matrix)
brightness_rgb=cv2.cvtColor(brightness_img,cv2.COLOR_BGR2RGB)
plt.imshow(brightness_rgb)
plt.title("Bright Image")
plt.show()