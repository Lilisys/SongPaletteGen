from PIL import Image

def colorGen(rgb0, rgb1, rgb2):
	im = Image.new("RGB", (2000, 3000), "white")

	#box points for each color
	c0 = [100, 2600, 200, 2700]
	c1 = [100, 2700, 200, 2800]
	c2 = [100, 2800, 200, 2900]

	#box points for second color
	box0 = (c0[0], c0[1], c0[2], c0[3])
	box1 = (c1[0], c1[1], c1[2], c1[3])
	box2 = (c2[0], c2[1], c2[2], c2[3])

	#map the box to the rgb values
	# boxMap = {	box0: (123, 22, 31),
	# 			box1: (31, 250, 11),
	# 			box2: (100, 21, 198)
	# 		 }
	boxMap = {	box0: rgb0,
				box1: rgb1,
				box2: rgb2
			}
	for box in boxMap:
		print box
		print boxMap[box]
		region = im.crop(box)
		for i in range(region.size[0]):    # for every pixel:
			for j in range(region.size[1]):
				#im.putpixel((c1x1 + i, c1y1 + j), (123, 22, 54))
				region.putpixel((i, j), boxMap[box])
		im.paste(region, box)		
	im.show()
	outfile = "asdf.jpg"
	im.save(outfile, "JPEG")


colorGen( 	(0, 111, 231),
			(31, 250, 100),
			(222, 114, 55)
		)