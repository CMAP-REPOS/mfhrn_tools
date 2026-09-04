"""
Implementation for the Import Highway Project Coding tool.
"""

"""
Author: Aaron Rumph
Updated: 09/04/2026
Notes: This is a translation/adaptation of Cindy's original code in `mfhrn_programs`
"""

# SECTION: Internal dependencies
from highway_network import HighwayNetwork

# SECTION: Constants


# SECTION: Functions
def import_highway_project_coding(
    mhn_gdb_path: str, coding_table_path: str, output_dir_path: str
) -> None:
    """
    The main function used by the Import Highway Project Coding tool.

    Parameters
    ----------
    mhn_gdb_path : str
        The path to the Master Highway Network GeoDatabase to export features from.
    coding_table_path : str
        The path to the excel table to use for highway project coding
    output_dir_path : str
        The directory in which to create the output error files as well
        as the base highway network gdb(?)
    """
    mhn = HighwayNetwork(mhn_gdb_path=mhn_gdb_path, output_dir_path=output_dir_path)
    mhn.create_base_hwy()
    mhn.check_hwy_fcs()
    mhn.import_hwyproj_coding()
    mhn.finalize_hwy_data()
    mhn.add_rcs()

    # NOTE: AR: This is a very quick and dirty function, literally copy pasted
    # Cindy's code here, but will test. I think this should work.
