# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 07:23:29 2019

@author: krabjohn
"""

# Import system modules
import arcpy
import time

# Set workspace
arcpy.env.workspace = "h:/data"

# Set local variables
out_path = "h:/data/Greenspace1.gdb"
out_name = "Tree"
geometry_type = "POINT"
template = "DISABLED"
has_m = "DISABLED"
has_z = "DISABLED"
# Set local parameters
domName = "DBH_"
domName2 = "Species"
domName3 = "Condition"
domName4 = "GrowSpace"
gdb = "Greenspace1.gdb"
inFeatures = "h:/data/Greenspace1.gdb/Tree"
Field_Name = "DBH_"
Field_Name2 = "Species"
Field_Name3 = "Condition"
Field_Name4 = "GrowSpace"
field_precision = "9"
field_domain = "Species"
field_alias="DBH"
field_is_nullable="NULLABLE"

# Use Describe to get a SpatialReference object
#sr = arcpy.SpatialReference(26917)

# Execute CreateFeatureclass
#arcpy.CreateFeatureclass_management(out_path, out_name, geometry_type, spatial_reference = sr)

#time.sleep(60)

#arcpy.AddField_management(inFeatures, Field_Name2, "TEXT", field_precision,
   #                       "", "",field_domain)
                          
 arcpy.AddField_management(inFeatures, Field_Name2, "TEXT", "", "",field_domain)                         
#arcpy.AddField_management(inFeatures, fieldName2, "TEXT", field_length=fieldLength)