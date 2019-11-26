import glob
from PIL import Image, ImageOps
import os

def resize_imgs(path):
	for i, img_path in enumerate(glob.glob(path)):
		if img_path.endswith("jpg"):
			im = Image.open(img_path)
			new_path = img_path.replace('jpg', 'png')
			im.save(new_path)
			os.remove(img_path)

resize_imgs("pokemon/images/images/*.jpg")