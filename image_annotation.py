import cv2
import matplotlib.pyplot as plt

image_path='fruits.jpg'
image=cv2.imread(image_path)

image_rgb=cv2.cvtColor(image,cv2COLOR_BGR2RGB)

height, width, _=image_rgb.shape

rect1_width, rect1_height=150,150
topleft1=(20,20)
bottomright1=(topleft[0]+rect1_width, topleft1[1]+rect1_height)
cv2.rectangle(image_rgb,topleft1,bottom_right1,(0,255,255),3)

rect2_width, rect2_height=200,150
topleft2=(width-rect2_width-20, height-rect2_height-20)
bottom_right2=(topleft2[0]+rect2_width, topleft2[1]+rect2_height)
cv2.rectangle(image_rgb,topleft2,bottom_right2,(255,0,255),3)

center1_x=topleft1[0]+rect1_width // 2
center1_y=topleft1[1]+rect1_height // 2
center2_x=topleft2[0]+rect2_width // 2
center2_y=topleft2[1]+rect2_height // 2
cv2.circle(image_rgb,(center1_x,center1_y),15,(0,255,0),-1)
cv2.circle(image_rgb,(center2_x,center2_y),15,(0,0,255),-1)

cv2.line(image_rgb,(center1_x,center1_y),(center2_x,center2_y),15,(0,255,0),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb,'Region 1',(topleft1[0],topleft1[1]-10), font,0.7,(0,255,0))
cv2.putText(image_rgb,'Region 2',(topleft2[0],topleft2[1]-10), font,0.7,(255,0,255))
cv2.putText(image_rgb,'Center 1',(center1_x-40,center1_y+40), font,0.6,(0,255,0),2)
cv2.putText(image_rgb,'Center 2',(center2_x-40,center2_y+40), font,0.6,(0,0,255),2)

arrow_start=(widrh-50,20)
arrow_end=(width-50,height-20)

cv2.arrowedLine(image_rgb,arrow_start,arrow_end,(255,255,0),3,tipLength=0.05)
cv2.arrowedLine(image_rgb,arrow_end,arrow_start,(255,255,0),3,tipLength=0.05)

plst.figure(figsize=(12,8))
plt.imshow(image_rgb)
plt.title("Annotated Image")
plt.axis("off")
plt.show()