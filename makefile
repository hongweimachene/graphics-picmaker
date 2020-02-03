all: picmaker.py
	python picmaker.py
	convert image.ppm image.png
