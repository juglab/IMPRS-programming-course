from ij import IJ
from ij import Prefs
from java.io import File
from ij.measure import ResultsTable
from ij.plugin.frame import RoiManager
from ij.plugin import Duplicator

# configuration
folder = "C:/structure/code/IMPRS-programming-course/day3_Fiji_Python/data";


# reset the table at the beginning
table = ResultsTable.getResultsTable();
table.reset()

# reset the ROI manager
manager = RoiManager.getRoiManager();
manager.reset();


IJ.run("Close All", "");



# access to the folder and the files in it
directory = File(folder);
listOfFilesInFolder = directory.listFiles();

for file in listOfFilesInFolder:
	if (file.toString().endswith(".tif")):
		# load image and show it
		imp = IJ.openImage(file.toString());
		imp.show();

		copy = Duplicator().run(imp);
	
		# apply a threshold to detect objects (cells, nuclei,...)
		IJ.setAutoThreshold(imp, "Otsu");
		Prefs.blackBackground = False;
		IJ.run(imp, "Convert to Mask", "");
		
		# analyse objects and put results in table
		IJ.run("Set Measurements...", "area display redirect=None decimal=5");
		IJ.run(imp, "Analyze Particles...", "exclude add");

		manager = RoiManager.getRoiManager();
		manager.runCommand("Save", file.toString() + ".RoiSet.zip");

		for roi in manager.getRoisAsArray():
			copy.setRoi(roi);
			copy.show();
			IJ.run(copy, "Enlarge...", "enlarge=-2");
			
			# analyse the image
			statistics = copy.getStatistics();
			print("mean: " + str(statistics.mean));
			print("area:" +  str(statistics.area));

			# write the analysed valurs in a table
			table = ResultsTable.getResultsTable();
			table.incrementCounter();
			table.addValue("filename", file.toString());
			table.addValue("mean_robert", statistics.mean);
			table.addValue("area", statistics.area);
			table.addValue("total instensity", statistics.mean * statistics.area);
			table.show("Results");

			# dirty hack to make the program stop here:
			# x = 1 / 0


# save the table
table = ResultsTable.getResultsTable();
table.show("Results");
table.save(folder + "results.xls");
table.reset()
		

	
IJ.run("Close All", "");





