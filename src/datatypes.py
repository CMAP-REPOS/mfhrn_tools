"""
This module contains functions etc. for working with various
ArcPy datatypes
"""

"""
Author: Aaron Rumph
Updated: 08/19/2026
Notes:
"""

# SECTION: External dependencies
import pandas as pd
import arcpy
from arcgis.features import GeoAccessor, GeoSeriesAccessor

# SECTION: Internal dependencies

# SECTION: Constants


# SECTION: Functions
def _spatial_df_from_table(fc_or_table: str) -> pd.DataFrame:
    """
    Helper function: returns a spatial dataframe from the given feature class.
    Mostly exists for readibility

    Parameters
    ----------
    fc_or_table : str
        The table or feature class to convert into a DataFrame.

    Returns
    -------
    A pd.DataFrame corresponding to the table or feature class provided.
    """
    fields = [field.name for field in arcpy.ListFields]
    np_arrar = arcpy.da.TableToNumPyArray(fc_or_table, fields)
