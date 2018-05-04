""" Import an image file , generate the skeleton, save as image"""


##collection of algorithms for image processing
from skimage import io
from skimage.morphology import skeletonize
from skimage.transform import  resize
from skimage import img_as_bool, color
#plotting package for 2D/3d ploting
###https://matplotlib.org/api/index.html
import matplotlib.pyplot as plt
#Scientific computing package for python ...we use the misc module to export the manipulated data 
##https://docs.scipy.org/doc/scipy/reference/misc.html
import scipy.misc 
# python module with time-related functions
###https://docs.python.org/2/library/time.html#module-time
import time





##1 # Image as Boolean...Reading the values of True False
    #Load an image from file.
    #Compute luminance of an RGB image/although b/w...values are RGB
    #luminance to True/False
image = img_as_bool(color.rgb2gray(io.imread('0109_Panel.bmp')))


##1.1#Optinal##/resize image for more detailed skeleton
image_resized = resize(image, (image.shape[0] / 0.1, image.shape[1] / 0.1),mode='constant')


##2# skeletonize
    ###reduces binary objects to 1 pixel wide representations
    ###returns a matrix containing the thinned image
skeleton = skeletonize(image)

#3## display original image and result

#Create a figure and a set of subplots
    # nrows, ncols -> Number of rows/columns of the subplot grid.
    #sharex,sharey ->sharing of properties among x (sharex) or y (sharey) axes
    #subplot_kw->keywords passed to the add_subplot() call 
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(20, 12),
                         sharex=True, sharey=True,subplot_kw={'adjustable': 'box-forced'} )


ax = axes.ravel()

ax[0].imshow(image, cmap=plt.cm.gray)#
ax[0].axis('off')
ax[0].set_title('original_Binary', fontsize=10)

ax[1].imshow(skeleton, cmap=plt.cm.gray)
ax[1].axis('off')
ax[1].set_title('skeleton', fontsize=10)

fig.tight_layout()# tight borders plot
plt.show()

#4## save skeleton result
timestr = time.strftime("%Y%m%d_%H%M%S")
scipy.misc.imsave(timestr+'skel .jpg', skeleton)
scipy.misc.imsave(timestr+'bin .jpg', image)
scipy.misc.imsave(timestr+'millipede .jpg', io.imread('0109_Panel.bmp'))

