from ij import IJ
from ij import Prefs
from java.io import File
from ij.measure import ResultsTable

# configuration
folder = "C:/structure/code/IMPRS-programming-course/day3_Fiji_Python/data";

# access to the folder and the files in it
directory = File(folder);
listOfFilesInFolder = directory.listFiles();

for file in listOfFilesInFolder:
	if (file.toString().endswith(".tif")):
		# load image and show it
		imp = IJ.openImage(file.toString());
		imp.show();
	
		# apply a threshold to detect objects (cells, nuclei,...)
		IJ.setAutoThreshold(imp, "Otsu");
		Prefs.blackBackground = False;
		IJ.run(imp, "Convert to Mask", "");
		
		# analyse objects and put results in table
		IJ.run("Set Measurements...", "area display redirect=None decimal=5");
		IJ.run(imp, "Analyze Particles...", "display exclude");

# save the table
table = ResultsTable.getResultsTable();
table.show("Results");
table.save(folder + "results.xls");
table.reset()
		

	





