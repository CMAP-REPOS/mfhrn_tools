# -*- coding: utf-8 -*-
r"""Generated ArcPy wrappers for the MFHRN Python toolbox."""
from __future__ import annotations

__all__ = [
    "CreateBusLayers",
    "ExportFutureHighwayNetwork",
    "GenerateEmmeHighwayFiles",
    "GenerateTransitFiles",
]
__alias__ = "MfhrnTools"

from arcpy.geoprocessing._base import gptooldoc, gp, gp_fixargs
from arcpy.arcobjects.arcobjectconversion import convertArcObjectToPythonObject
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from arcpy.typing.gp import Result


@gptooldoc("ExportFutureHighwayNetwork_MfhrnTools", None)
def ExportFutureHighwayNetwork(
    Mhn_Gdb_Path=None, Years_To_Export=None, Output_Folder=None
) -> Result:
    """Build year-specific highway geodatabases and MHN_all.gdb."""
    try:
        return convertArcObjectToPythonObject(
            gp.ExportFutureHighwayNetwork_MfhrnTools(
                *gp_fixargs(
                    (Mhn_Gdb_Path, Years_To_Export, Output_Folder), True
                )
            )
        )
    except Exception as error:
        raise error


@gptooldoc("GenerateEmmeHighwayFiles_MfhrnTools", None)
def GenerateEmmeHighwayFiles(
    Mhn_All_Gdb_Path=None, Scenario_Years=None, Output_Folder=None
) -> Result:
    """Generate EMME highway files from MHN_all.gdb."""
    try:
        return convertArcObjectToPythonObject(
            gp.GenerateEmmeHighwayFiles_MfhrnTools(
                *gp_fixargs(
                    (Mhn_All_Gdb_Path, Scenario_Years, Output_Folder), True
                )
            )
        )
    except Exception as error:
        raise error


@gptooldoc("CreateBusLayers_MfhrnTools", None)
def CreateBusLayers(
    Mhn_Gdb_Path=None,
    Mhn_All_Gdb_Path=None,
    Scenario_Years=None,
    Output_Folder=None,
) -> Result:
    """Create bus layers for each EMME scenario and transit time period."""
    try:
        return convertArcObjectToPythonObject(
            gp.CreateBusLayers_MfhrnTools(
                *gp_fixargs(
                    (
                        Mhn_Gdb_Path,
                        Mhn_All_Gdb_Path,
                        Scenario_Years,
                        Output_Folder,
                    ),
                    True,
                )
            )
        )
    except Exception as error:
        raise error


@gptooldoc("GenerateTransitFiles_MfhrnTools", None)
def GenerateTransitFiles(
    Bus_Network_Folder=None, Scenario_Years=None, Output_Folder=None
) -> Result:
    """Generate EMME bus itinerary files."""
    try:
        return convertArcObjectToPythonObject(
            gp.GenerateTransitFiles_MfhrnTools(
                *gp_fixargs(
                    (Bus_Network_Folder, Scenario_Years, Output_Folder), True
                )
            )
        )
    except Exception as error:
        raise error


del gptooldoc, gp, gp_fixargs, convertArcObjectToPythonObject, annotations, TYPE_CHECKING
