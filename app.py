import cv2
import easygui
from pathlib import Path

select_file = True
while select_file:
	# allowed file types
	allowed_file_types = ['.png', '.jpg', '.jpeg']

	# open file manager to select file
	file = easygui.fileopenbox()
	path = Path(file)

	try:
		# check if file is an image
		if path.suffix in allowed_file_types:
			# get file name
			file_name = path.stem
			# set new file name for sketch
			sketch_file_name = f"{file_name}-sketch.png"
			# end loop and prevent file manager from opening again
			select_file = False
			
	except Exception as e:
		print("please select an image")
		break


# function to turn the image to a sketch
def make_sketch(file):
	image = cv2.imread(file)

	grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	invert = cv2.bitwise_not(grey_image)
	blur = cv2.GaussianBlur(invert, (21, 21), 0)
	invertedblur = cv2.bitwise_not(blur)

	# draw the sketch and save
	sketch = cv2.divide(grey_image, invertedblur, scale=256.0)

	cv2.imwrite(sketch_file_name, sketch)

make_sketch(file)