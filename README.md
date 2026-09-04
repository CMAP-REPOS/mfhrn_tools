# MFHRN Tools
This repository contains tools (ArcPy toolboxes) for working with 
CMAP's Master Highway Network. The code in this repository is based on 
the code in the [mfhrn_programs](https://github.com/CMAP-REPOS/mfhrn_programs) 
repository.

## Setup:
To use the tools in this toolbox you should first clone this repo locally with:

```shell
git clone https://github.com/CMAP-REPOS/mfhrn_tools.git
```

Then, in ArcGIS from the Catalog you should import the toolbox by right clicking
on "Toolboxes" and selecting "Add toolbox". This will bring up a window where you can
select the toolbox to add. In this window, navigate to: `PATH\TO\mfhrn_tools\src\toolbox`
and select "MfhrnTools.pyt" (which should have a toolbox icon next to it).
You can then now use the MfhrnTools toolbox from the geoprocessing tools list!


## Usage:
The MfhrnTools toolbox contains the following five tools:
1. Export Future Highway Network
*Creates a seperate Geodatabase for each of the chosen scenario years*
2. Generate EMME Highway Files
*Creates the necessary highway files for EMME for each scenario year*
3. Create Bus Layers
*Creates a seperate Geodatabase for each scenario year containing*
*layers for each of the four times of day*
4. Generate Transit Files
*Creates the EMME transit itinerary files from the bus network files*
5. Import Highway Project Coding
*Updates the project coding for the MHN as specified by the input*
*hwyproj_coding_table (see [mfhrn_programs wiki entry on import_hwyproj_coding](https://github.com/CMAP-REPOS/mfhrn_programs/blob/working/aaron/wiki/scripts/import_hwyproj_coding.md))*

Before using any of tools 2 through 4, you must run Export Future Highway Network 
first, as the result is an input to the other tools. Additionally, to run the
`Generate Transit Files` tool, you must first run the `Create Bus Layers` tool.
Usage instructions for each of the above tools is provided below.

### Export Future Highway Network
The `Export Future Highway Network` tool takes an exisiting MHN Geodatabase
and exports new geodatabases representing the state of the Highway network
for each provided scenario year (which projects will be completed, etc.).

#### Prerequisites
*N/A*

#### Notes
Network Years implicitly includes 2015 as a year to export a future highway
network for.

#### Parameters
- Master Highway Network (MHN) Geodatabase
*The MHN Geodatabase to export future highway networks from.*
- Network Years
*A list of years to export future highway networks for*
- Output Folder
*The folder in which to output the resulting highway network geodatabases*
*as well as the log files*.


### Generate EMME Highway Files
The `Generate EMME Highway Files` tool converts the geodatabases created by
the `Export Future Highway Network` tool into EMME highway files.

#### Prerequisites
- Already ran `Export Future Highway Network` tool

#### Notes
When running this tool, you need to make sure that your "Netowrk Years and EMME Scenarios"
parameter contains "2015" as the first `Network Year` value, with the respective `EMME Scenario` 
value being set to "100" (NOTE: You may be able to select any value here?).

#### Parameters
- Combined Highway Network Geodatabase (MHN_all.gdb)
*The `MHN_all.gdb` geodatabase created when you ran `Export Future Highway Network`*
- Network Years and EMME Scenarios
*The years to export to EMME highway files, with the EMME scenario number to use for each*
*(NOTE: I believe you must use the same years you used when running `Export Future Highway Network`?)*
- Highway Output Folder
*The folder in which to create the folders containing EMME files for each scenario.*
*Note that each scenario will get it's own folder* ***within*** *the output folder.*

### Create Bus Layers
The `Create Bus Layers` tool exports the bus network from the MHN 
geodatabase created by the `Export Future Highway Network` tool 
into seperate geodatabases for each of the specified scenario years.

#### Prerequisites
- Already ran `Export Future Highway Network` tool.

#### Notes
When running this tool, you need to make sure that your "Netowrk Years and EMME Scenarios"
parameter contains "2015" as the first `Network Year` value, with the respective `EMME Scenario` 
value being set to "100" (NOTE: You may be able to select any value here?).

#### Parameters
- Master Highway Network (MHN) Geodatabase
*The original MHN geodatabase you used as the input to `Export Future Highway Network`.*
- Combined Highway Network Geodatabase (MHN_all.gdb)
*The `MHN_all.gdb` geodatabase created when you ran `Export Future Highway Network`.*
- Network Years and EMME Scenarios
*The years to create bus geodatabases for, with the EMME scenario number to use for each*
*(NOTE: I believe you must use the same years you used when running `Export Future Highway Network`?)*
- Bus Network Output Folder
*The folder in which to create the folders containing EMME files for each scenario.*
*Note that each scenario will get it's own folder* ***within*** *the output folder.*

### Generate Transit Files
The `Geneerate Transit Files` tool exports the bus network from the MHN 
geodatabases created by the `Create Bus Layers` tool into EMME Bus Itinerary
files for each of the specified years.

#### Prerequisites
- Already ran `Export Future Highway Network` tool ***AND***
- Already ran `Create Bus Layers` tool.

#### Notes
When running this tool, you need to make sure that your "Netowrk Years and EMME Scenarios"
parameter contains "2015" as the first `Network Year` value, with the respective `EMME Scenario` 
value being set to "100" (NOTE: You may be able to select any value here?).

#### Parameters
- Bus Network Folder
*The folder containing the bus network geodatabases that were created by*
*the `Create Bus Layers` tool (i.e., the Bus Network Output Folder*
*you selected when running `Create Bus Layers`.*
- Network Years and EMME Scenarios
*The years to create itineraries for, with the EMME scenario number to use for each.*
*(NOTE: I believe you must use the same years you used when running `Export Future Highway Network`?)*
- Transit Output Folder
*The folder in which to create the folders containing EMME files for each scenario.*

### Import Highway Project Coding
The `Import Highway Project Coding` tool updates project coding in the MHN
according to the provided Input Project Coding Table.

#### Prerequisites
- Imported Excel/CSV project coding table into ArcGIS as a Table.

#### Notes
When using this tool, be sure to remember that it expects different things
than the `mhn_programs` equivalent tool did. Read more at
[on the wiki](https://github.com/CMAP-REPOS/mfhrn_programs/blob/working/aaron/wiki/scripts/import_hwyproj_coding.md) 
or [see an example MFHRN project coding table](https://github.com/CMAP-REPOS/mfhrn_programs/blob/working/aaron/templates/import_hwyproj_coding_template.xlsx).

#### Parameters
- Master Highway Network (MHN) Geodatabase
*The MHN Geodatabase to update the highway project coding for.*
- Input Project Coding Table
*An ArcGIS table that contains the desired changes to the MHN*
*geodatabase's project coding.*
- Output Folder
*The folder in which to log issues, etc.*

## Time Estimates
You can expect the tools to take roughly the following amounts of time 
(based on 5 scenarios).

- Export Future Highway Network
**~5 mins.**
I believe time complexity is O(n * m) where n is number of distinct scenarios
and m is the total number of years covered by the scenarios (e.g., 
for 2015-2050, m = 35). So expect longer times for a larger range, 
as well as more scenarios.
- Generate EMME Highway Files
**~2.5 mins.**
- Create Bus Layers
**~10.5 mins.**
- Generate Transit Files
**~0.5 mins.**
- Import Highway Project Coding
**~2 mins.**
With a small number of edits to make?

