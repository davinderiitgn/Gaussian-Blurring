'''Author - Davinder Singh'''
import cv2
import numpy as np
import math

img = cv2.imread("butterfly.jpg",0)


## Initialize Gaussiand Filters Matrix
gauss_1 = np.zeros((11,11))
gauss_2 = np.zeros((11,11))

k = 5
## Standard deviations
sigma_1 = 4
sigma_2 = 2

## Initialize Normalization Factors for the Gaussian Filters
norm_factor_1 = 0
norm_factor_2 = 0

## Computing the values of Gaussian Filter/Kernel
for i in range(11):
       for j in range(11):
              gauss_1[i][j] = math.exp(-float(((i-k)**2+(j-k)**2))/(2*sigma_1*sigma_1))
              gauss_2[i][j] = math.exp(-float(((i-k)**2+(j-k)**2))/(2*sigma_2*sigma_2))
              norm_factor_1 += gauss_1[i][j] #Accumulating the values of the kernel to be divided in the end to normalize
              norm_factor_2 += gauss_2[i][j] #Accumulating the values of the kernel to be divided in the end to normalize
DoG_filter = gauss_1/norm_factor_1 - gauss_2/norm_factor_2

print DoG_filter

blurred_img = np.zeros(img.shape)      #new blurred image

padded_image = cv2.copyMakeBorder(img,5,5,5,5,cv2.BORDER_CONSTANT,value=0)   #image is padded with zeros

print "Will take a few seconds, please wait!"

for y in range(0,img.shape[1]):
	for x in range(0,img.shape[0]):
		val_x_y = 0
		for i in range(0,11): 
			for j in range(0,11):
				val_x_y += DoG_filter[i][j]*padded_image[i+x][y+j]
		blurred_img[x][y] = val_x_y


Zero_Crossings = np.zeros(img.shape, dtype = np.uint8)      #array representing zero crossings each crossing point has value 1 and rest have value 0


for i in range(img.shape[0]-1):
       for j in range(img.shape[1]-1):
              if blurred_img[i][j]>0:
                     if blurred_img[i-1][j]<0 or blurred_img[i+1][j]<0 or blurred_img[i][j-1]<0 or blurred_img[i][j+1]<0:
                            Zero_Crossings[i][j] = 255
                            
cv2.imwrite("Blurred_image.jpg", blurred_img)
cv2.imwrite("Binary_Image.jpg", Zero_Crossings)

print("Done!")
cv2.imshow('Blurred Image',blurred_img)
cv2.imshow('Original Image',img)
cv2.imshow('ZeroCrossings', Zero_Crossings)
cv2.waitKey(0)
cv2.destroyAllWindows()

