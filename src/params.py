"""
Module containing functions for working with arcpy parameters
"""

"""
Author: Aaron Rumph
Updated: 08/19/2026
Notes: N/A
"""

# SECTION: External dependencies
import arcpy

# SECTION: Internal dependencies


# SECTION: Functions
def parse_years(parameter: arcpy.Parameter) -> list[int]:
    """
    Helper function: parses incoming arcpy year(s) parameter and returns a
    list of specified years.
    """
    unparsed_years = parameter.valueAsText

    # split on ';'
    parsed_years = unparsed_years.split(";")

    # cast to int
    parsed_years = [int(year) for year in parsed_years]
    return parsed_years


def _debug_params(param: arcpy.Parameter, messages):
    """
    Helper function: Quick and dirty debugging function for
    viewing information about parameters as received by Arc toolbox
    """
    messages.addMessage(f"Display Name: {param.displayName}")
    messages.addMessage(f"Internal Name: {param.name}")
    messages.addMessage(f"Data Type: {param.dataType}")
    messages.addMessage(f"Direction: {param.direction}")
    messages.addMessage(f"Parameter Type: {param.parameterType}\n")
    messages.addMessage(f"Value!!!: {param.valueAsText}")
