from ij import IJ
from ij import Prefs

# load image and show it
imp = IJ.openImage("C:/structure/code/IMPRS-programming-course/day3_Fiji_Python/data/blobs.tif");
imp.show();

# apply a threshold to detect objects (cells, nuclei,...)
IJ.setAutoThreshold(imp, "Otsu");
Prefs.blackBackground = False;
IJ.run(imp, "Convert to Mask", "");


