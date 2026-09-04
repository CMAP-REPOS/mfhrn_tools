"""
Implementation for the Export Future Highway Network tool.
"""

"""
Author: Aaron Rumph
Updated: 09/01/2026
Notes: This is a translation/adaptation of Cindy's original code in `mfhrn_programs`
"""

# SECTION: Internal dependencies
from highway_network import HighwayNetwork

# SECTION: Constants


# SECTION: Functions
def export_future_highways(
    mhn_gdb_path: str, years: list[int], output_dir_path: str
) -> None:
    """
    The main function used by the Export Future Highway Network tool.
    Exports the MHN to a geodatabase for each specified network year.

    Parameters
    ----------
    mhn_gdb_path : str
        The path to the Master Highway Network GeoDatabase to export features from.
    years : list[int]
        The list of years to export features for. Will be used to select based on project
        completion date
    output_dir_path : str
        The directory in which to create the output geodatabases.
    """
    mhn = HighwayNetwork(
        mhn_gdb_path=mhn_gdb_path, output_dir_path=output_dir_path
    )
    mhn.create_base_hwy()
    mhn.check_hwy_fcs()
    mhn.check_hwyproj_coding_table()
    mhn.build_future_hwys(years=years)
