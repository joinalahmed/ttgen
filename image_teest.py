import numpy as np
import PIL
from PIL import Image
#list_im = ['4.jpg', '5.jpg', '3.jpg']
def horizon(list_im):
    #list_im = ['4.jpg', '5.jpg', '4.jpg']
    imgs = [PIL.Image.open(i) for i in list_im]
    # pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted([(np.sum(i.size), i.size) for i in imgs])[0][1]
    imgs_comb = np.hstack((np.asarray(i.resize(min_shape)) for i in imgs))
    imgs_comb = PIL.Image.fromarray( imgs_comb)
    imgs_comb.save( 'Trifecta.jpg' )
def vertical(list_im):

    imgs    = [ PIL.Image.open(i) for i in list_im ]
# pick the image which is the smallest, and resize the others to match it (can be arbitrary image shape here)
    min_shape = sorted( [(np.sum(i.size), i.size ) for i in imgs])[0][1]
    imgs_comb = np.hstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
# for a vertical stacking it is simple: use vstack
    imgs_comb = np.vstack( (np.asarray( i.resize(min_shape) ) for i in imgs ) )
    imgs_comb = PIL.Image.fromarray( imgs_comb)
    imgs_comb.save( 'Trifecta_vertical.jpg' )


# save that beautiful picture
