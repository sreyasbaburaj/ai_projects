import cv2
image=cv2.imread("fruits.jpg")
gray_img=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
resize_img=cv2.resize(gray_img,(224,224))
cv2.imshow("Grayscale Image", resize_img)
key=cv2.waitKey(0)
if key == ord("s"):
    cv2.imwrite("Grayscale_Img.jpg", resize_img)
    print("Image saved as Grayscale_Img.jpg")
else:
    print("Image not saved.")

cv2.destroyAllWindows()
print(f"Dimensions of processed image: {resize_img.shape}")