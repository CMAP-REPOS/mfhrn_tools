"""
Python toolbox for ArcGIS containing MFHRN tools.
"""

"""
Author: Aaron Rumph
Updated: 09/01/2026
Notes:
    The tool classes below provide ArcGIS Pro interfaces for the travel
    scripts adapted from `mfhrn_programs`.
"""

# SECTION: External dependencies
import os
import sys

import arcpy

# SECTION: Internal dependencies

# NOTE: AR: Python toolboxes are not imported as packages, so the src
# directory has to be added to sys.path before importing the tool code.
_toolbox_dir = os.path.dirname(__file__)
_src_dir = os.path.abspath(os.path.join(_toolbox_dir, ".."))
if _src_dir not in sys.path:
    sys.path.insert(0, _src_dir)

from create_bus_layers import BusNetwork
from export_future_highway_network import export_future_highways
from generate_emme_highway_files import EmmeHighwayNetwork
from generate_transit_files import EmmeTransitNetwork
from params import parse_scenario_years, parse_years


# SECTION: Classes
class Toolbox:
    """
    Tools for working with CMAP's Master Highway Network (MHN).
    """

    def __init__(self):
        """
        Toolbox setup.
        """
        self.label = "MFHRN Tools"
        self.alias = "MfhrnTools"
        self.tools = [
            ExportFutureHighwayNetwork,
            GenerateEmmeHighwayFiles,
            CreateBusLayers,
            GenerateTransitFiles,
        ]


class ExportFutureHighwayNetwork:
    """
    Creates a MHN geodatabase for each specified network year and a
    combined MHN_all geodatabase for the other travel tools.
    """

    def __init__(self):
        """
        Tool definition and metadata.
        """
        self.label = "Export Future Highway Network"
        self.description = (
            "Export future highway network states into a new "
            "geodatabase for each specified network year."
        )
        self.canRunInBackground = True

    def getParameterInfo(self):
        """
        Parameter definitions for the tool.
        """

        # Param 0: GDB containing the full MHN
        param_mhn_gdb_path = arcpy.Parameter(
            displayName="Master Highway Network (MHN) Geodatabase",
            name="Mhn_Gdb_Path",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        # Param 1: years to build highway networks for
        param_export_years = arcpy.Parameter(
            displayName="Network Years",
            name="Years_To_Export",
            datatype="GPLong",
            parameterType="Required",
            direction="Input",
            multiValue=True,
        )

        # Param 2: folder for the year GDBs and MHN_all.gdb
        param_output_folder = arcpy.Parameter(
            displayName="Output Folder",
            name="Output_Folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input",
        )

        params = [
            param_mhn_gdb_path,
            param_export_years,
            param_output_folder,
        ]
        return params

    def execute(self, parameters, messages):
        """
        Run the Export Future Highway Network tool.
        """
        mhn_gdb_path = parameters[0].valueAsText
        export_years = parse_years(parameters[1])
        output_folder = parameters[2].valueAsText

        messages.addMessage("Exporting future highway networks...")
        export_future_highways(
            mhn_gdb_path=mhn_gdb_path,
            years=export_years,
            output_dir_path=output_folder,
        )


class GenerateEmmeHighwayFiles:
    """
    Generates EMME highway files from MHN_all.gdb.
    """

    def __init__(self):
        """
        Tool definition and metadata.
        """
        self.label = "Generate EMME Highway Files"
        self.description = (
            "Generate EMME highway files from the combined highway "
            "network geodatabase."
        )
        self.canRunInBackground = True

    def getParameterInfo(self):
        """
        Parameter definitions for the tool.
        """

        # Param 0: combined GDB made by Export Future Highway Network
        param_mhn_all_gdb_path = arcpy.Parameter(
            displayName="Combined Highway Network Geodatabase (MHN_all.gdb)",
            name="Mhn_All_Gdb_Path",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        # Param 1: network year and EMME scenario lookup
        param_scenario_years = arcpy.Parameter(
            displayName="Network Years and EMME Scenarios",
            name="Scenario_Years",
            datatype="GPValueTable",
            parameterType="Required",
            direction="Input",
        )
        param_scenario_years.columns = [
            ["GPLong", "Network Year"],
            ["GPLong", "EMME Scenario"],
        ]

        # Param 2: folder for the EMME highway files
        param_output_folder = arcpy.Parameter(
            displayName="Highway Output Folder",
            name="Output_Folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input",
        )

        params = [
            param_mhn_all_gdb_path,
            param_scenario_years,
            param_output_folder,
        ]
        return params

    def execute(self, parameters, messages):
        """
        Run the Generate EMME Highway Files tool.
        """
        mhn_all_gdb_path = parameters[0].valueAsText
        scenario_years = parse_scenario_years(parameters[1])
        output_folder = parameters[2].valueAsText

        messages.addMessage("Generating EMME highway files...")
        network = EmmeHighwayNetwork(
            mhn_all_gdb_path=mhn_all_gdb_path,
            scenario_years=scenario_years,
            output_folder=output_folder,
        )
        network.generate_hwy_files()


class CreateBusLayers:
    """
    Creates a bus-network geodatabase for each EMME scenario. Each
    geodatabase contains a feature dataset for each transit time of day.
    """

    def __init__(self):
        """
        Tool definition and metadata.
        """
        self.label = "Create Bus Layers"
        self.description = (
            "Collapse bus routes and create bus layers for each EMME "
            "scenario and transit time of day."
        )
        self.canRunInBackground = True

    def getParameterInfo(self):
        """
        Parameter definitions for the tool.
        """

        # Param 0: GDB containing the full MHN and bus route data
        param_mhn_gdb_path = arcpy.Parameter(
            displayName="Master Highway Network (MHN) Geodatabase",
            name="Mhn_Gdb_Path",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        # Param 1: combined GDB made by Export Future Highway Network
        param_mhn_all_gdb_path = arcpy.Parameter(
            displayName="Combined Highway Network Geodatabase (MHN_all.gdb)",
            name="Mhn_All_Gdb_Path",
            datatype="DEWorkspace",
            parameterType="Required",
            direction="Input",
        )

        # Param 2: network year and EMME scenario lookup
        param_scenario_years = arcpy.Parameter(
            displayName="Network Years and EMME Scenarios",
            name="Scenario_Years",
            datatype="GPValueTable",
            parameterType="Required",
            direction="Input",
        )
        param_scenario_years.columns = [
            ["GPLong", "Network Year"],
            ["GPLong", "EMME Scenario"],
        ]

        # Param 3: folder for the bus-network geodatabases
        param_output_folder = arcpy.Parameter(
            displayName="Bus Network Output Folder",
            name="Output_Folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input",
        )

        params = [
            param_mhn_gdb_path,
            param_mhn_all_gdb_path,
            param_scenario_years,
            param_output_folder,
        ]
        return params

    def execute(self, parameters, messages):
        """
        Run the Create Bus Layers tool.
        """
        mhn_gdb_path = parameters[0].valueAsText
        mhn_all_gdb_path = parameters[1].valueAsText
        scenario_years = parse_scenario_years(parameters[2])
        output_folder = parameters[3].valueAsText

        messages.addMessage("Creating bus layers...")
        network = BusNetwork(
            mhn_gdb_path=mhn_gdb_path,
            mhn_all_gdb_path=mhn_all_gdb_path,
            scenario_years=scenario_years,
            output_folder=output_folder,
        )
        network.create_bn_folder()
        network.collapse_bus_routes()
        network.create_bus_layers()


class GenerateTransitFiles:
    """
    Generates EMME transit files from the bus-network geodatabases.
    """

    def __init__(self):
        """
        Tool definition and metadata.
        """
        self.label = "Generate Transit Files"
        self.description = (
            "Generate EMME transit files from the bus-network "
            "geodatabases."
        )
        self.canRunInBackground = True

    def getParameterInfo(self):
        """
        Parameter definitions for the tool.
        """

        # Param 0: folder made by Create Bus Layers
        param_bus_network_folder = arcpy.Parameter(
            displayName="Bus Network Folder",
            name="Bus_Network_Folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input",
        )

        # Param 1: network year and EMME scenario lookup
        param_scenario_years = arcpy.Parameter(
            displayName="Network Years and EMME Scenarios",
            name="Scenario_Years",
            datatype="GPValueTable",
            parameterType="Required",
            direction="Input",
        )
        param_scenario_years.columns = [
            ["GPLong", "Network Year"],
            ["GPLong", "EMME Scenario"],
        ]

        # Param 2: folder for the EMME transit files
        param_output_folder = arcpy.Parameter(
            displayName="Transit Output Folder",
            name="Output_Folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input",
        )

        params = [
            param_bus_network_folder,
            param_scenario_years,
            param_output_folder,
        ]
        return params

    def execute(self, parameters, messages):
        """
        Run the Generate Transit Files tool.
        """
        bus_network_folder = parameters[0].valueAsText
        scenario_years = parse_scenario_years(parameters[1])
        output_folder = parameters[2].valueAsText

        messages.addMessage("Generating EMME transit files...")
        network = EmmeTransitNetwork(
            bus_network_folder=bus_network_folder,
            scenario_years=scenario_years,
            output_folder=output_folder,
        )
        network.generate_transit_files()
