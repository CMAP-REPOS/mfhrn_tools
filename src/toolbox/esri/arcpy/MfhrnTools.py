# -*- coding: utf-8 -*-
r""""""
from __future__ import annotations
__all__ = ['CreateBusLayers', 'ExportFutureHighwayNetwork', 'GenerateEmmeHighwayFiles', 'GenerateTransitFiles']
__alias__ = 'MfhrnTools'
from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal
    from arcpy import RecordSet, FeatureSet
    from arcpy._mp import Layer, Table
    from arcpy.typing.gp import Result, Result1, Result2, Result3

# Tools
@gptooldoc('CreateBusLayers_MfhrnTools', None)
def CreateBusLayers(Mhn_Gdb_Path=None, Mhn_All_Gdb_Path=None, Scenario_Years=None, Output_Folder=None,) -> Result:
    """CreateBusLayers_MfhrnTools(Mhn_Gdb_Path, Mhn_All_Gdb_Path, Scenario_Years;Scenario_Years..., Output_Folder)

     INPUTS:
      Mhn_Gdb_Path (Workspace):
          Master Highway Network (MHN) Geodatabase
      Mhn_All_Gdb_Path (Workspace):
          Combined Highway Network Geodatabase (MHN_all.gdb)
      Scenario_Years (Value Table):
          Network Years and EMME Scenarios
      Output_Folder (Folder):
          Bus Network Output Folder"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateBusLayers_MfhrnTools(*gp_fixargs((Mhn_Gdb_Path, Mhn_All_Gdb_Path, Scenario_Years, Output_Folder), True)))
        return retval
    except Exception as e:
        raise e

@gptooldoc('ExportFutureHighwayNetwork_MfhrnTools', None)
def ExportFutureHighwayNetwork(Mhn_Gdb_Path=None, Years_To_Export=None, Output_Folder=None,) -> Result:
    """ExportFutureHighwayNetwork_MfhrnTools(Mhn_Gdb_Path, Years_To_Export;Years_To_Export..., Output_Folder)

     INPUTS:
      Mhn_Gdb_Path (Workspace):
          Master Highway Network (MHN) Geodatabase
      Years_To_Export (Long):
          Network Years
      Output_Folder (Folder):
          Output Folder"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportFutureHighwayNetwork_MfhrnTools(*gp_fixargs((Mhn_Gdb_Path, Years_To_Export, Output_Folder), True)))
        return retval
    except Exception as e:
        raise e

@gptooldoc('GenerateEmmeHighwayFiles_MfhrnTools', None)
def GenerateEmmeHighwayFiles(Mhn_All_Gdb_Path=None, Scenario_Years=None, Output_Folder=None,) -> Result:
    """GenerateEmmeHighwayFiles_MfhrnTools(Mhn_All_Gdb_Path, Scenario_Years;Scenario_Years..., Output_Folder)

     INPUTS:
      Mhn_All_Gdb_Path (Workspace):
          Combined Highway Network Geodatabase (MHN_all.gdb)
      Scenario_Years (Value Table):
          Network Years and EMME Scenarios
      Output_Folder (Folder):
          Highway Output Folder"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateEmmeHighwayFiles_MfhrnTools(*gp_fixargs((Mhn_All_Gdb_Path, Scenario_Years, Output_Folder), True)))
        return retval
    except Exception as e:
        raise e

@gptooldoc('GenerateTransitFiles_MfhrnTools', None)
def GenerateTransitFiles(Bus_Network_Folder=None, Scenario_Years=None, Output_Folder=None,) -> Result:
    """GenerateTransitFiles_MfhrnTools(Bus_Network_Folder, Scenario_Years;Scenario_Years..., Output_Folder)

     INPUTS:
      Bus_Network_Folder (Folder):
          Bus Network Folder
      Scenario_Years (Value Table):
          Network Years and EMME Scenarios
      Output_Folder (Folder):
          Transit Output Folder"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateTransitFiles_MfhrnTools(*gp_fixargs((Bus_Network_Folder, Scenario_Years, Output_Folder), True)))
        return retval
    except Exception as e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject, annotations, TYPE_CHECKING