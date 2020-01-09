import imgProcessing

path = '../BibliImage/MonetResized.png'
pathObject = '../BibliImage/bananaResized.png'
#imgProcessing.resizeImage(pathObject, 250,200)
imgProcessing.glueObjectComputeMask(pathObject, path, (-20,-40))
