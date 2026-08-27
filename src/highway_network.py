"""
Module containing the 'HighwayNetwork' class and associated
functions and methods.
"""

"""
Author: Aaron Rumph
Updated: 08/19/2026
Notes:
"""

# SECTION: External dependencies
import os
import pandas as pd

pd.set_option("display.max_columns", None)

from pprint import pprint

# for fc -> df conversion
from arcgis.features import GeoAccessor, GeoSeriesAccessor

# SECTION: Internal dependencies
from datatypes import _spatial_df_from_table

# SECTION: Constants

# SECTION: Classes


class HighwayNetwork:
    def __init__(self, mhn_gdb_path: str):
        """
        Constructor for the HighwayNetwork class.
        """

        # NOTE: Below are all the attributes for the HighwayNetwork class.
        # Gives handles to all tables, relationship classes, feature classes.
        # Attribute suffixes correspond to type (_table, _rc, _fc, etc)
        self.mhn_gdb_path = mhn_gdb_path

        # Feature clases
        self.mhn_baselinks_fc = os.path.join(f"{self.mhn_gdb_path}", "mhn_baselinks")

        self.hwynet_fc = os.path.join(f"{self.mhn_gdb_path}", "hwynet")
        self.hwynet_arc_fc = os.path.join(f"{self.hwynet_fc}", "hwynet_arc")
        self.hwynet_node_fc = os.path.join(f"{self.hwynet_fc}", "hwynet_node")
        self.hwyproj_fc = os.path.join(f"{self.hwynet_fc}", "hwyproj")

        self.bus_base_fc = os.path.join(f"{self.hwynet_fc}", "bus_base")
        self.bus_current_fc = os.path.join(f"{self.hwynet_fc}", "bus_current")
        self.bus_future_fc = os.path.join(f"{self.hwynet_fc}", "bus_future")

        # Tables
        self.hwyproj_coding_table = os.path.join(
            f"{self.mhn_gdb_path}", "hwyproj_coding"
        )
        self.parknride_table = os.path.join(f"{self.mhn_gdb_path}", "parknride")
        self.bus_base_itin_table = os.path.join(f"{self.mhn_gdb_path}", "bus_base_itin")
        self.bus_current_itin_table = os.path.join(
            f"{self.mhn_gdb_path}", "bus_current_itin"
        )
        self.bus_future_itin_table = os.path.join(
            f"{self.mhn_gdb_path}", "bus_future_itin"
        )

        ## Relationship classes
        self.arcs_to_bus_base_itin_rc = os.path.join(
            f"{self.mhn_gdb_path}", "rel_arcs_to_bus_base_itin"
        )
        self.arcs_to_bus_current_itin_rc = os.path.join(
            f"{self.mhn_gdb_path}", "rel_arcs_to_bus_current_itin"
        )
        self.arcs_to_bus_future_itin_rc = os.path.join(
            f"{self.mhn_gdb_path}", "rel_arcs_to_bus_future_itin"
        )

        self.arcs_to_hwyproj_coding_rc = os.path.join(
            f"{self.mhn_gdb_path}", "rel_arcs_to_hwyproj_coding"
        )
        self.hwyproj_to_hwyproj_coding_rc = os.path.join(
            f"{self.mhn_gdb_path}", "rel_hwyproj_to_coding"
        )

        self.bus_base_to_bus_base_itin_rc = os.path.join(
            f"{self.mhn_gdb_path}", "rel_bus_base_to_itin"
        )
        self.bus_current_to_bus_current_itin_rc = os.path.join(
            f"{self.mhn_gdb_path}", "rel_bus_current_to_itin"
        )
        self.bus_future_to_bus_future_itin_rc = os.path.join(
            f"{self.mhn_gdb_path}", "rel_bus_future_to_itin"
        )

        self.hwynet_nodes_to_parknride = os.path.join(
            f"{self.mhn_gdb_path}", "rel_nodes_to_parknride"
        )

        self.mhn_baselinks_fc_df = _spatial_df_from_table(self.mhn_baselinks_fc)

        self.hwynet_fc_df = _spatial_df_from_table(self.hwynet_fc)
        self.hwynet_arc_fc_df = _spatial_df_from_table(self.hwynet_arc_fc)
        self.hwynet_node_fc_df = _spatial_df_from_table(self.hwynet_node_fc)
        self.hwyproj_fc_df = _spatial_df_from_table(self.hwyproj_fc)

        self.bus_base_fc_df = _spatial_df_from_table(self.bus_base_fc)
        self.bus_current_fc_df = _spatial_df_from_table(self.bus_current_fc)
        self.bus_future_fc_df = _spatial_df_from_table(self.bus_future_fc)

    def check_feature_classes(self):
        """
        Checks that feature classes meet all the invariants
        for a well formed Master Highway Network.
        """
        # TODO: Check feature classes

        # NOTE: AR: I have intentionally made this method a pretty
        # shallow wrapper that just calls other methods that do the
        # actual validation that a given feature class/table is
        # well formed. This keeps the code more modular, and easier
        # to change how individual fcs are checked.

        self.check_hwylink_feature_class()
        self.check_hwynode_feature_class()
        self.check_hwyproj_feature_class()

    def check_hwynode_feature_class():
        # TODO: check hwynode feature class/table
        pass

    def check_hwylink_feature_class():
        # TODO: Check hwylink feature class/tabel
        pass

    def check_hwyproj_feature_class():
        # TODO: Check hwyproj feature class/table
        pass

    def create_gdb_for_year(year: int, output_dir: str) -> None:
        pass


# SECTION: Functions

# SECTION: Main
if __name__ == "__main__":
    # NOTE: AR: this is an area I'm just using for quick
    # print debugging
    local_mhn_path = r"C:\Users\arumph\MasterHighway\mhn_c26q2.gdb"
    mhn = HighwayNetwork(mhn_gdb_path=local_mhn_path)

    # print attrs of MHN
    pprint(vars(mhn))

    df_props = [df for df in vars(mhn).keys() if str(df).endswith("df")]
    for df in df_props:
        print(df_props)
