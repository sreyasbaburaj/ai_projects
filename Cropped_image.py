import cv2
import matplotlib.pyplot as plt

image=cv2.imread("fruits.jpg")

rgb_img=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.title("RGB Image")
plt.show()

grayscale_img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.imshow(grayscale_img)
plt.title("Grayscale Image")
plt.show()

cropped_img=image[100:200,200:400]
cropped_rgb=cv2.cvtColor(cropped_img, cv2.COLOR_BGR2RGB)
plt.imshow(cropped_rgb)
plt.title("Cropped Image")
plt.show()