import cv2
import numpy as np
import math

img = cv2.imread("butterfly.jpg",1)


G1 = np.zeros((9,9)) #Gaussin Filter
G2 = np.zeros((9,9)) #Gaussin Filter
G3 = np.zeros((9,9)) #Gaussin Filter

k = 4
##            Standard Devations          ##
sigma_1 = 1  
sigma_2 = 3
sigma_3 = 20


##            Normalisation Factors to Normalize the kernel           ##
normalisation_factor_1 = 0
normalisation_factor_2 = 0
normalisation_factor_3 = 0



##             Computing The Values of Gaussian Filters  ####################################
for i in range(9):
       for j in range(9):
              G1[i][j] = math.exp(-float(((i-k)**2+(j-k)**2))/(2*sigma_1*sigma_1))
              G2[i][j] = math.exp(-float(((i-k)**2+(j-k)**2))/(2*sigma_2*sigma_2))
              G3[i][j] = math.exp(-float(((i-k)**2+(j-k)**2))/(2*sigma_3*sigma_3))
              normalisation_factor_1 += G1[i][j]
              normalisation_factor_2 += G2[i][j]
              normalisation_factor_3 += G3[i][j]

##             Normalizing the values            ##
Gaussian_filter_1 = G1/normalisation_factor_1
Gaussian_filter_2 = G2/normalisation_factor_2
Gaussian_filter_3 = G3/normalisation_factor_3

print "Gaussian filter with Standard Deviation 1 :"
print Gaussian_filter_1
print "Gaussian filter with Standard Deviation 3 :"
print Gaussian_filter_2
print "Gaussian filter with Standard Deviation 20 :"
print Gaussian_filter_3

blurred_image_1 = np.zeros(img.shape)     
blurred_image_2 = np.zeros(img.shape)
blurred_image_3 = np.zeros(img.shape)

padded_image = cv2.copyMakeBorder(img,4,4,4,4,cv2.BORDER_CONSTANT,value=0)   ## Padding the original image with zeros

print "Generating Images..."
print "Please wait! Will take some Time...."
#############Convoluting The Image with filter with standard deviation = 1 ##############
##
for y in range(0,img.shape[1]):
	for x in range(0,img.shape[0]):
		val_x_y_0 = 0
		val_x_y_1 = 0
		val_x_y_2 = 0
		for i in range(0,9): 
			for j in range(0,9):
				val_x_y_0 += Gaussian_filter_1[i][j]*padded_image[i+x][y+j][0]
				val_x_y_1 += Gaussian_filter_1[i][j]*padded_image[i+x][y+j][1]
				val_x_y_2 += Gaussian_filter_1[i][j]*padded_image[i+x][y+j][2]
		blurred_image_1[x][y][0] = val_x_y_0
		blurred_image_1[x][y][1] = val_x_y_1
		blurred_image_1[x][y][2] = val_x_y_2


#############Convoluting The Image with filter with standard deviation = 3 ##############
for y in range(0,img.shape[1]):
	for x in range(0,img.shape[0]):
		val_x_y_0 = 0
		val_x_y_1 = 0
		val_x_y_2 = 0
		for i in range(0,9): 
			for j in range(0,9):
				val_x_y_0 += Gaussian_filter_2[i][j]*padded_image[i+x][y+j][0]
				val_x_y_1 += Gaussian_filter_2[i][j]*padded_image[i+x][y+j][1]
				val_x_y_2 += Gaussian_filter_2[i][j]*padded_image[i+x][y+j][2]
		blurred_image_2[x][y][0] = val_x_y_0
		blurred_image_2[x][y][1] = val_x_y_1
		blurred_image_2[x][y][2] = val_x_y_2


#############Convoluting The Image with filter with standard deviation = 20 ##############
for y in range(0,img.shape[1]):
	for x in range(0,img.shape[0]):
		val_x_y_0 = 0
		val_x_y_1 = 0
		val_x_y_2 = 0
		for i in range(0,9): 
			for j in range(0,9):
				val_x_y_0 += Gaussian_filter_3[i][j]*padded_image[i+x][y+j][0]
				val_x_y_1 += Gaussian_filter_3[i][j]*padded_image[i+x][y+j][1]
				val_x_y_2 += Gaussian_filter_3[i][j]*padded_image[i+x][y+j][2]
		blurred_image_3[x][y][0] = val_x_y_0
		blurred_image_3[x][y][1] = val_x_y_1
		blurred_image_3[x][y][2] = val_x_y_2


blurred_image_1 = blurred_image_1.astype("uint8")
blurred_image_2 = blurred_image_2.astype("uint8")
blurred_image_3 = blurred_image_3.astype("uint8")

print("Done!")

cv2.imshow('Sigma = 1',blurred_image_1)
cv2.imshow('Sigma = 3',blurred_image_2)
cv2.imshow('Sigma = 20',blurred_image_3)
cv2.waitKey(0)
cv2.destroyAllWindows()

