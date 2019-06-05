# -*- coding: utf-8 -*-


#Import system modules
import arcpy

try:
# Set the workspace (to avoid having to type in the full path to the data        every time)
    arcpy.env.workspace = "h:/data"

# Set local parameters
    domName = "Species"
    gdb = "Campus_Tree.gdb"

# Process: Create the coded value domain
#arcpy.CreateDomain_management("UPDM.gdb", domName, "Gas Systems", "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the  "key" and the
# domain description as the "value" (domDict[code])
    domDict = {"Alnus_glutinosa":"Alnus glutinosa", \
                "Alnus_rugosa": "Alnus rugosa", \
                "Betula_alleghaniensis": "Betula alleghaniensis", \
                "Betula_nigra": "Betula nigra", \
                "Betula_papyrifera": "Betula papyrifera", \
                "Betula_pendula": "Betula pendula", \
                "Carpinus_caroliniana": "Carpinus caroliniana", \
                "Carya_cordiformis": "Carya cordiformis", \
                "Carya_ovata": "Carya ovata", \
                "Castanea_dentata": "Castanea dentata", \
                "Catalpa_speciosa": "Catalpa speciosa", \
                "Celtis_occidentalis": "Celtis occidentalis", \
                "Cercidiphyllum_japonicum": "Cercidiphyllum japonicum",}

# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
    for code in domDict:
        arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])

except Exception as err:
            print(err.args[0])

