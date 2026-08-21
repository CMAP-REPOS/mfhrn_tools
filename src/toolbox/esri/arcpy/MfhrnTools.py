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
def CreateBusLayers(Mhn_Gdb_Path=None, Scenario_Years=None, Output_Dir=None,) -> Result:
    """CreateBusLayers_MfhrnTools(Mhn_Gdb_Path, Scenario_Years;Scenario_Years..., Output_Dir)

     INPUTS:
      Mhn_Gdb_Path (Workspace):
          MHN GeoDatabase
      Scenario_Years (Long):
          Scenario Years
      Output_Dir (Folder):
          Output folder"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.CreateBusLayers_MfhrnTools(*gp_fixargs((Mhn_Gdb_Path, Scenario_Years, Output_Dir), True)))
        return retval
    except Exception as e:
        raise e

@gptooldoc('ExportFutureHighwayNetwork_MfhrnTools', None)
def ExportFutureHighwayNetwork(Mhn_Gdb_Path=None, Years_To_Export=None, Output_Dir_Path=None,) -> Result:
    """ExportFutureHighwayNetwork_MfhrnTools(Mhn_Gdb_Path, Years_To_Export;Years_To_Export..., Output_Dir_Path)

     INPUTS:
      Mhn_Gdb_Path (Workspace):
          Master Highway Network (MHN) GeoDatabase
      Years_To_Export (String):
          Export Years
      Output_Dir_Path (Folder)"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.ExportFutureHighwayNetwork_MfhrnTools(*gp_fixargs((Mhn_Gdb_Path, Years_To_Export, Output_Dir_Path), True)))
        return retval
    except Exception as e:
        raise e

@gptooldoc('GenerateEmmeHighwayFiles_MfhrnTools', None)
def GenerateEmmeHighwayFiles(Mhn_Gdb_Path=None, Output_Folder=None, Base_Scenario_Year=None, Future_Scenario_Years=None,) -> Result:
    """GenerateEmmeHighwayFiles_MfhrnTools(Mhn_Gdb_Path, Output_Folder, Base_Scenario_Year, Future_Scenario_Years;Future_Scenario_Years...)

     INPUTS:
      Mhn_Gdb_Path (Workspace):
          MHN GeoDatabase
      Output_Folder (Folder):
          Output Folder
      Base_Scenario_Year (Long):
          Base scenario year
      Future_Scenario_Years (Long):
          Future scenario year(s)"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateEmmeHighwayFiles_MfhrnTools(*gp_fixargs((Mhn_Gdb_Path, Output_Folder, Base_Scenario_Year, Future_Scenario_Years), True)))
        return retval
    except Exception as e:
        raise e

@gptooldoc('GenerateTransitFiles_MfhrnTools', None)
def GenerateTransitFiles(Mhn_Gdb_Path=None, Years_To_Export=None,) -> Result:
    """GenerateTransitFiles_MfhrnTools(Mhn_Gdb_Path, Years_To_Export)

     INPUTS:
      Mhn_Gdb_Path (Workspace):
          MHN GeoDatabase
      Years_To_Export (String):
          Years to export"""
    from arcpy.geoprocessing._base import gp, gp_fixargs
    from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
    try:
        retval = convertArcObjectToPythonObject(gp.GenerateTransitFiles_MfhrnTools(*gp_fixargs((Mhn_Gdb_Path, Years_To_Export), True)))
        return retval
    except Exception as e:
        raise e


# End of generated toolbox code
del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject, annotations, TYPE_CHECKING