# Toolbox README

This directory contains geoprocessing toolbox files 
so that the Python toolbox [`../MfhrnTools.pyt`] can be
imported into ArcGIS Pro and run as a Geoprocessing tool.

The majority of the files in this directory are generated using
a tool provided by Esri for converting Python toolboxes (.pyt) into
geoprocessing GUI tools. The tool can be run with the following 
command from the root directory:
```shell
# if using conda
conda activate arcpy

# if using mamba and arcpy env is visibile to mamba
mamba activate arcpy

# running the tool
python -c "import arcpy; arcpy.gp.createtoolboxsupportfiles(r'src\toolbox\MfhrnTools.pyt')"
```
