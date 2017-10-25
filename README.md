# Image Analyzer based on pearson correlation
Image Analyzer using pearson-correlation and cross-correlation
### Requirements:
	Operating System:
		Windows
	python:
		version 2.5
	libs:
	
		python 2.5 
		NUMPY 
		SCIPY
		VideoCapture
		PIL (a videoCapture precisa dessa)
PS:
the file analisador.py must be kept on python's folder (i.e.: C:\Python25)
1. Open the prompt;
2. start the interpreter
3. import the file: import analisador

Yayy!! take your pics and start to play! =)

### How it works
The application takes images using the webcam of your laptop;

An image is an array, or a matrix, of square pixels (picture elements) arranged in columns and rows. The app gets these pixels and convert them to values such as black and white.

After this convertion, we apply the pearson correlation coefficient to generate an index for each image.

All images taken by the camera are compared to the first image taken. The correlation is generated based on this comparison made between each image and the first one.

After that, the images are stored in a vector sorted by descending order.

The sorted vector is divided into 3 parts, storing the images in 3 folders.

The first folder has the images with more correlation;

The second folder has the images with intermediary correlation;

The third folder has the images with less correlation.


### Output
The app will create a folder named IA, inside python's path and an HTML will be generated, which you can open to check the results in the browser.

PS:
If you want to run this code again you need to rename this folder or exclude it.

## Authors

* **Sergio Vinícius de Sá Lucena** - [sergioviniciuss](https://github.com/sergioviniciuss)
* **André Furquim** - [macand](https://github.com/mcand)
* **Heloisa Medeiros**

## Acknowledgments

* This code was written as part of an Artificial Intelligence study to evaluate the efficiency of pearson correlation to 
* **Detailed explanation** - [slideshare - portuguese](https://pt.slideshare.net/sergioviniciuss/analisador-de-imagens-usando-o-coeficiente-de-correlao)

