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
    mhn = HighwayNetwork(mhn_gdb_path=mhn_gdb_path)
    mhn.create_base_hwy(output_dir=output_dir_path)
    mhn.check_hwyproj_coding_table(output_dir=output_dir_path)
    mhn.check_hwy_fcs()
    mhn.build_future_hwys(years=years, output_dir=output_dir_path)


# SECTION: Main entry point
def main():
    pass


if __name__ == "__main__":
    test_mhn_path = r"tests\input\mhns\base-test-mhn.gdb"
    test_output_dir = "tests/output/test-1"
    test_years = [2019, 2026, 2030, 2035, 2040, 2045, 2050]

    export_future_highways(
        mhn_gdb_path=test_mhn_path, output_dir_path=test_output_dir, years=test_years
    )
