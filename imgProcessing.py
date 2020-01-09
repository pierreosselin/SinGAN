from PIL import Image
import numpy as np

def resizeImage(filePath, width, height = 0): ## Size in Pixels
    im = Image.open(filePath)
    if height:
        im = im.resize((width, height))
    else:
        rwidth, rheight = im.size
        im = im.resize((width, int((rheight/rwidth)*width)))
    im.save(filePath[:-4] + 'Resized' + filePath[-4:])


def glueObjectComputeMask(path_object, path_background, index): #index = couple place to glue
    background = Image.open(path_background)
    t = np.array(background)
    s = t.shape
    print(s)
    size = background.size
    if s[2] == 3:
        text_img = Image.new('RGB', size, (0, 0, 0))
    elif s[2] == 4:
        text_img = Image.new('RGBA', size, (0, 0, 0, 0))
    obj = Image.open(path_object)
    text_img.paste(background, (0,0))
    backTest = np.array(text_img)
    text_img.paste(obj, index, mask=obj)
    text_img.save(path_background[:-4] + 'paste' + path_background[-4:])
    ## Compute Mask
    back = np.array(text_img)
    mask = np.logical_or(np.logical_or((back - backTest)[:,:,0] != 0, (back - backTest)[:,:,1] != 0  ), (back - backTest)[:,:,2] != 0)
    mask = np.tile(mask[:,:,None], (1,s[2]))
    print(mask.shape)
    Image.fromarray((mask*255).astype(np.uint8)).save(path_object[:-4] + 'mask' + path_object[-4:])
