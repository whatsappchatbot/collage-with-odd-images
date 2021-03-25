# importing the modules
import cv2
import numpy as np

# read all the images
# we are going to take 4 images only
image1=cv2.imread(r"C:\Users\Snehal\Desktop\TEJAS\imges\amul.jpg")
image2=cv2.imread(r"C:\Users\Snehal\Desktop\TEJAS\imges\warna.jpg")
image3=cv2.imread(r"C:\Users\Snehal\Desktop\TEJAS\imges\nandini.jpg")
image4=cv2.imread(r"C:\Users\Snehal\Desktop\TEJAS\imges\white.jpg")

# make all the images of same size 
#so we will use resize function
image1=cv2.resize(image1,(200,200))
image2=cv2.resize(image2,(200,200))
image3=cv2.resize(image3,(200,200))
image4=cv2.resize(image4,(200,200))

# Now how we will attach image with other image
# we will create a horizontal stack of images
# then we will add it to the vertical stack
# let the horizontal pair be (image1,image2)
# and (image3,image4)
# we will use numpy stack function
Horizontal1=np.hstack([image1,image2])
Horizontal2=np.hstack([image3,image4])

# Now the horizontal attachment is done
# noe vertical attachment
Vertical_attachment=np.vstack([Horizontal1,Horizontal2])

# Show the final attachment
cv2.imshow("Final Collage",Vertical_attachment)
cv2.imwrite(r"C:\Users\Snehal\Desktop\TEJAS\imges\final.jpg",Vertical_attachment)
cv2.waitKey(0)
cv2.destroyAllWindows()
