"""
Python toolbox for ArcGIS containing MFHRN tools.
"""

"""
Author: Aaron Rumph
Updated: 08/19/2026
Notes:
    I am basing the toolbox code partially off of Esri's
    'LargeNetworkAnalysisTools' toolbox. Which is available under an
    Apache 2.0 License. I am mostly using Cindy's code contained within
    "scripts" dir as the basis for the actual tools themselves, using
    the 'LargeNetworkAnalysisTools' code for the template for writing
    the toolbox in the correct format. You can view that repo at:
    https://github.com/Esri/large-network-analysis-tools/tree/master.
    If you see `(Source: Esri 2023)` that is code or documentation
    attributed to Esri under the Apache 2.0 license in the
    'LargeNetworkAnalysisTools' repo.
"""

# SECTION: External dependencies
import os
import arcpy

# SECTION: Internal dependencies
from src.params import _debug_params, parse_years

# SECTION: Functions


# SECTION: Classes
class Toolbox(object):
    """
    Tools for working with CMAP's Master Highway Network (MHN).
    """

    def __init__(self):
        """
        Toolbox setup.
        """
        self.label = "MFHRN Tools"
        self.alias = "MfhrnTools"

        # TODO: once done with tool code, add tool class to list here
        self.tools = [
            ExportFutureHighwayNetwork,
            GenerateEmmeHighwayFiles,
            CreateBusLayers,
            GenerateTransitFiles,
        ]


# NOTE: AR: Each tool needs to be represented as it's own class
# with the following methods:
# [getParameterInfo, isLicensed, updateParameters, updateMessages, execute]


class ExportFutureHighwayNetwork(object):
    """
    Creates new MHN GeoDatabases representing the state
    of the highway network in all specified future years.

    # TODO: ADD Documentation
    """

    def __init__(self):
        """
        Tool definition and metadata.
        """
        self.label = "Export Future Highway Network"
        self.description = (
            "Export future highway network states into a new "
            "GeoDatabase for each specified future year."
        )
        self.canRunInBackground = True

    def getParameterInfo(self):
        """
        Parameter definitions for the tool.
        """

        # NOTE: The params below are 0-indexed in comments to make
        # it easier to find them when they're in an array

        # Param 0: Handle to the GDB containing the full MHN
        param_mhn_gdb_path = arcpy.Parameter(
            displayName="Master Highway Network (MHN) GeoDatabase",
            name="Mhn_Gdb_Path",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        # Param 1: Which years to export a future highway network for
        param_export_years = arcpy.Parameter(
            displayName="Export Years",
            name="Years_To_Export",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
            multiValue="True",
        )

        # Param 2: The directory in which to create the MHN GDBs for each target year
        param_output_dir_path = arcpy.Parameter(
            displayName="",
            name="Output_Dir_Path",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input",
        )

        # TODO: param_highway_projects_subset:
        # Add parameter for subsetting which projects to export when using
        # this tool. Should `parameterType` be "DETable"?

        # Returning params (must be in ordered array)
        params = [param_mhn_gdb_path, param_export_years, param_output_dir_path]

        return params

    def isLicensed(self):
        """Whether or not the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """
        Modify the values and properties of parameters before
        internal validation is performed. This method is called whenever
        a parameter has been changed.
        """
        # TODO: Figure out updateParameters method
        pass

    def updateMessages(self, new_msg):
        """
        Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation.
        (Source: Esri)
        """
        # TODO: Figure out updateMessages method
        pass

    def execute(self, parameters, messages):
        """
        Where the tool actually gets executed.
        """
        for param in parameters:
            _debug_params(param, messages)

        # parsing input years as may be multiple (years is 1st param)
        input_years: list[int] = parse_years(parameters[1])

        return


class GenerateEmmeHighwayFiles(object):
    """
    Generates highway files for use in EMME based on the
    input MHN gdb.

    # TODO: Add documentation
    """

    def __init__(self):
        """
        Tool definition and metadata.
        """
        self.label = "Generate Emme Highway Files"
        self.description = (
            "Generates EMME highway files based on the input MHN GeoDatabase"
        )
        self.canRunInBackground = True

    def getParameterInfo(self):
        """
        Parameter definitions for the tool.
        """

        # NOTE: The params below are 0-indexed in comments to make
        # it easier to find them when they're in an array

        # Param 0: Handle to the GDB containing the MHN to export
        # to EMME highway files
        param_mhn_gdb_path = arcpy.Parameter(
            displayName="MHN GeoDatabase",
            name="Mhn_Gdb_Path",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        # Param 1: Output directory to create EMME files/dir of
        # EMME files in
        param_output_folder = arcpy.Parameter(
            displayName="Output Folder",
            name="Output_Folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input",
        )

        # Param 2: Base scenario year
        param_base_scenario_year = arcpy.Parameter(
            displayName="Base scenario year",
            name="Base_Scenario_Year",
            datatype="GPLong",
            parameterType="Required",
            direction="Input",
        )

        # Param 3: Future scenario years (multiValue for multiple)
        param_future_scenario_years = arcpy.Parameter(
            displayName="Future scenario year(s)",
            name="Future_Scenario_Years",
            datatype="GPLong",
            parameterType="Required",
            direction="Input",
            multiValue="True",
        )

        # Returning params (must be in ordered array)
        params = [
            param_mhn_gdb_path,
            param_output_folder,
            param_base_scenario_year,
            param_future_scenario_years,
        ]

        return params

    def isLicensed(self):
        """Whether or not the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """
        Modify the values and properties of parameters before
        internal validation is performed. This method is called whenever
        a parameter has been changed.
        """
        # TODO: Figure out updateParameters method
        pass

    def updateMessages(self):
        """
        Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation.
        (Source: Esri)
        """
        # TODO: Figure out updateMessages method
        pass

    def execute(self, parameters, messages):
        """
        Where the tool actually gets executed.
        """
        # TODO: implement execute method
        pass


class CreateBusLayers(object):
    """
    Creates GeoDatabases representing the bus network for all scenario years.
    Each Geodatabase contains a seperate layer for each TOD.

    # TODO: ADD Documentation
    """

    def __init__(self):
        """
        Tool definition and metadata.
        """
        self.label = "Create Bus Layers"
        self.description = (
            "Creates GeoDatabase for the bus network for all specified "
            "scenario years, with seperate layers for each Time of Day"
        )
        self.canRunInBackground = True

    def getParameterInfo(self):
        """
        Parameter definitions for the tool.
        """

        # NOTE: The params below are 0-indexed in comments to make
        # it easier to find them when they're in an array

        # Param 0: Handle to the GDB containing the full MHN
        param_mhn_gdb_path = arcpy.Parameter(
            displayName="MHN GeoDatabase",
            name="Mhn_Gdb_Path",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        # Param 1: Which years to export a bus years for
        param_export_years = arcpy.Parameter(
            displayName="Scenario Years",
            name="Scenario_Years",
            datatype="GPLong",
            parameterType="Required",
            direction="Input",
            multiValue="True",
        )

        # Param 2: The directory in which to create the GDB containging
        # the bus layers (feature classes)
        param_output_dir = arcpy.Parameter(
            displayName="Output folder",
            name="Output_Dir",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input",
        )

        # Returning params (must be in ordered array)
        params = [param_mhn_gdb_path, param_export_years, param_output_dir]

        return params

    def isLicensed(self):
        """Whether or not the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """
        Modify the values and properties of parameters before
        internal validation is performed. This method is called whenever
        a parameter has been changed.
        """
        # TODO: Figure out updateParameters method
        pass

    def updateMessages(self):
        """
        Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation.
        (Source: Esri)
        """
        # TODO: Figure out updateMessages method
        pass

    def execute(self, parameters, messages):
        """
        Where the tool actually gets executed.
        """
        # TODO: implement execute method
        pass


class GenerateTransitFiles(object):
    """

    # TODO: ADD Documentation
    """

    def __init__(self):
        """
        Tool definition and metadata.
        """
        self.label = "Generate Transit Files"
        self.description = "Creates GeoDatabase for each specified future year."
        self.canRunInBackground = True

    def getParameterInfo(self):
        """
        Parameter definitions for the tool.
        """

        # NOTE: The params below are 0-indexed in comments to make
        # it easier to find them when they're in an array

        # Param 0: Handle to the GDB containing the full MHN
        param_mhn_gdb_path = arcpy.Parameter(
            displayName="MHN GeoDatabase",
            name="Mhn_Gdb_Path",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        # Param 1: Which years to export a future highway network for
        param_export_years = arcpy.Parameter(
            displayName="Years to export",
            name="Years_To_Export",
            datatype="GPString",
            parameterType="Required",
            direction="Input",
        )

        # Returning params (must be in ordered array)
        params = [
            param_mhn_gdb_path,
            param_export_years,
        ]

        return params

    def isLicensed(self):
        """Whether or not the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """
        Modify the values and properties of parameters before
        internal validation is performed. This method is called whenever
        a parameter has been changed.
        """
        # TODO: Figure out updateParameters method
        pass

    def updateMessages(self):
        """
        Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation.
        (Source: Esri)
        """
        # TODO: Figure out updateMessages method
        pass

    def execute(self, parameters, messages):
        """
        Where the tool actually gets executed.
        """
        # TODO: implement execute method
        pass
