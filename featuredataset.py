# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 14:01:18 2019

@author: krabjohn
"""


# Import system modules
import arcpy

# Set environment settings
arcpy.env.workspace = "h:/data
 
# Set local variables
inFeatures = "schools"
fieldName1 = "ref_ID"
fieldPrecision = 9
fieldAlias = "refcode"
fieldName2 = "status"
fieldLength = 10

# Set local variables
out_dataset_path = "h:/data/greenspace.gdb" 
out_name = "trees"

# Creating a spatial reference object nad 83 utm zone 17 n
sr = arcpy.SpatialReference(26917)

# Create a FileGDB for the fds
#arcpy.CreateFileGDB_management("h:/data", "greenspace.gdb")

# Execute CreateFeaturedataset 
arcpy.CreateFeatureDataset_management(out_dataset_path, out_name, sr)

 

 
# Execute AddField twice for two new fields
arcpy.AddField_management(inFeatures, fieldName1, "LONG", fieldPrecision,
                          field_alias=fieldAlias, field_is_nullable="NULLABLE")
                          
arcpy.AddField_management(inFeatures, fieldName2, "TEXT", field_length=fieldLength)

