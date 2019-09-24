# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:01:18 2019

@author: krabjohn
"""


# Import system modules
import arcpy
from arcpy import env

# Set environment settings
env.workspace = "h:/data"
 
# Set local variables
inFeatures = "schools"
fieldName1 = "ref_ID"
fieldPrecision = 9
fieldAlias = "refcode"
fieldName2 = "status"
fieldLength = 10

# Set local variables
out_dataset_path = "h:/data/brownspace2.gdb" 
FDC_name = "Growth"
FC_Name = "TREES"

# Creating a spatial reference object nad 83 utm zone 17 n
sr = arcpy.SpatialReference(26917)

# Create a FileGDB for the fds
arcpy.CreateFileGDB_management("h:/data", "brownspace2.gdb")

# Execute CreateFeaturedataset 
arcpy.CreateFeatureDataset_management(out_dataset_path, FDC_name, sr)

arcpy.CreateFeatureclass_management(out_dataset_path, FC_Name, "POINT")
# CreateFeatureclass_management (out_path, out_name, {geometry_type}, {template}, {has_m}, {has_z}, {spatial_reference}, {config_keyword}, {spatial_grid_1}, {spatial_grid_2}, {spatial_grid_3})
 
# # Execute AddField twice for two new fields
# arcpy.AddField_management(inFeatures, fieldName1, "LONG", fieldPrecision,
#                           field_alias=fieldAlias, field_is_nullable="NULLABLE")
                          
# arcpy.AddField_management(inFeatures, fieldName2, "TEXT", field_length=fieldLength)

