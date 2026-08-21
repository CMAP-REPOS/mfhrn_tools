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

# for fc -> df conversion
from arcgis.features import GeoAccessor, GeoSeriesAccessor

# SECTION: Internal dependencies

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


# SECTION: Functions
