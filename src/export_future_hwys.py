"""
Export future highway years as seperate GDBs for each target year.
"""

"""
Author: Aaron Rumph
Updated: 08/19/2026
Notes: This is a translation/adaptation of Cindy's original code in `mfhrn_programs`
"""

# SECTION: External dependencies
import os


# SECTION: Internal dependencies
from highway_network import HighwayNetwork

# SECTION: Constants


# SECTION: Functions
def export_future_highways(
    mhn_gdb_path: str, years: list[int], output_dir_path: str
) -> None:
    """
    The main 'ExportFutureHighwayNetwork'. Exports a Master Highway Network
    GeoDatabase into the necessary files to be used with EMME.

    Parameters
    ----------
    mhn_gdb_path : str
        The path to the Master Highway Network GeoDatabase to export features from.
    years : list[int]
        The list of years to export features for. Will be used to select based on project
        completion date
    output_dir_path : str
        The directory in which to create the EMME files.
    """
    master_highway_network = HighwayNetwork(mhn_gdb_path=mhn_gdb_path)

    # NOTE: Cindy has a `create_base_hwy()` method here. From what I can tell
    # all that does is create a copy of the input MHN

    master_highway_network.check_feature_classes()

    # main loop
    for year in years:
        # TODO: impl export_year() and output_dir writing here!
        master_highway_network.export_year(year)


# SECTION: Main entry point
def main():
    pass
