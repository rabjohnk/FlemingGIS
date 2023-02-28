# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Description: Create a file GDB

# Import system modules
import arcpy
import time

# Set local variables
out_folder_path = "H:/Data/Greenspace" 
out_name = "Greenspace2.gdb"
FeatureName = "Trees"
# Creating a spatial reference object nad 83 utm zone 17 n


# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, out_name)

time.sleep(20)

sr = arcpy.SpatialReference(26917)

try:
# Set the workspace (to avoid having to type in the full path to the data        every time)
    arcpy.env.workspace = "h:/data/Greenspace"
     
        
    
# Set local parameters
    domName = "Scientific_N"
    domName2 = "DBH"
    domName3 = "Condition"
    domName4 = "GrowSpace"
    domName5 = "Maintanence"
    domName6 = "Notes"
    gdb = "Greenspace.gdb"
    inFeatures = "Arboretum1.gdb/Trees_Shrubs"
    Field_Name = "Scientific_N"
    Field_Name2 = "DBH"
    Field_Name3 = "Condition"
    Field_Name4 = "GrowSpace"
    #inFeatures = "Montgomery.gdb/Water/Distribmains"
    #inField = "Material"
     

# Process: Create the coded value domain
    arcpy.CreateDomain_management(gdb, domName, "Scientific Name","TEXT", "CODED") 
    
    arcpy.CreateDomain_management(gdb, domName2, "DBH","TEXT", "CODED")   
    
    arcpy.CreateDomain_management(gdb, domName3, "Condition","TEXT", "CODED")    
    
    arcpy.CreateDomain_management(gdb, domName4, "GrowSpace","TEXT", "CODED") 
    
    arcpy.CreateDomain_management(gdb, domName5, "Maintanence","TEXT", "CODED")
    
    arcpy.CreateDomain_management(gdb, domName6, "Notes","TEXT", "CODED")
   
    time.sleep(10)
# Process: Create the coded value domain
#arcpy.CreateDomain_management("UPDM.gdb", domName, "Gas Systems", "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the  "key" and the
# domain description as the "value" (domDict[code])
    domDict = {"Abies_concolor": "Abies concolor", \
                "Acer_ginnala": "Acer ginnala", \
                "Acer_negundo": "Acer negundo", \
                "Acer_nigrum": "Acer nigrum", \
                "Acer_palmatum": "Acer palmatum", \
                "Acer_pensylvanicum": "Acer pensylvanicum", \
                "Acer_platanoides": "Acer platanoides", \
                "Acer_pseudoplatanus": "Acer pseudoplatanus", \
                "Acer_rubrum": "Acer rubrum", \
                "Acer_saccharinum": "Acer saccharinum", \
                "Acer_saccharum": "Acer saccharum", \
                "Acer_spicatum": "Acer spicatum", \
                "Acer_x_freemanii": "Acer x freemanii", \
                "Aesculus_glabra": "Aesculus glabra", \
                "Aesculus_hippocastanum": "Aesculus hippocastanum", \
                "Ailanthus_altissima": "Ailanthus altissima", \
                "Alnus_glutinosa": "Alnus glutinosa", \
                "Alnus_rugosa": "Alnus rugosa", \
                "Amelanchier": "Amelanchier", \
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
                "Cercidiphyllum_japonicum": "Cercidiphyllum japonicum", \
                "Cercis_canadensis": "Cercis canadensis", \
                "Cladrastis_kentukea": "Cladrastis kentukea", \
                "Cornus_alternifolia": "Cornus alternifolia", \
                "Cornus_sericea": "Cornus sericea", \
                "Corylus_colurna": "Corylus colurna", \
                "Corylus_cornuta": "Corylus cornuta", \
                "Crataegus_sp.": "Crataegus sp.", \
                "Elaeagnus_angustifolia": "Elaeagnus angustifolia", \
                "Fagus_grandifolia": "Fagus grandifolia", \
                "Fagus_sylvatica": "Fagus sylvatica", \
                "Fraxinus_americana": "Fraxinus americana", \
                "Fraxinus_excelsior": "Fraxinus excelsior", \
                "Fraxinus_nigra": "Fraxinus nigra", \
                "Fraxinus_pennsylvanica": "Fraxinus pennsylvanica", \
                "Ginkgo_biloba": "Ginkgo biloba", \
                "Gleditsia_triacanthos": "Gleditsia triacanthos", \
                "Gymnocladus_dioicus": "Gymnocladus dioicus", \
                "Hamamelis_virginiana": "Hamamelis virginiana", \
                "Juglans_cinerea": "Juglans cinerea", \
                "Juglans_nigra": "Juglans nigra", \
                "Juniperus_communis_var.": "Juniperus communis var. depressa", \
                "Juniperus_horizontalis": "Juniperus horizontalis", \
                "Juniperus_virginiana": "Juniperus virginiana ", \
                "Larix_decidua": "Larix decidua", \
                "Larix_kaempferi": "Larix kaempferi", \
                "Larix_laricina": "Larix laricina", \
                "Liquidambar_styraciflua": "Liquidambar styraciflua", \
                "Liriodendron_tulipifera": "Liriodendron tulipifera", \
                "Magnolia_acuminata": "Magnolia acuminata", \
                "Magnolia_x_soulangiana": "Magnolia x soulangiana", \
                "Malus_sp.": "Malus sp.", \
                "Metasequoia_glyptostroboides": "Metasequoia glyptostroboides", \
                "Morus_alba": "Morus alba", \
                "Ostrya_virginiana": "Ostrya virginiana", \
                "Parthenocissus_vitacea": "Parthenocissus vitacea", \
                "Phellodendron_amurense": "Phellodendron amurense", \
                "Picea_abies": "Picea abies", \
                "Picea_glauca": "Picea glauca", \
                "Picea_mariana": "Picea mariana", \
                "Picea_omorika": "Picea omorika", \
                "Picea_pungens": "Picea pungens", \
                "Pinus_banksiana": "Pinus banksiana", \
                "Pinus_cembra": "Pinus cembra", \
                "Pinus_mugo": "Pinus mugo", \
                "Pinus_nigra": "Pinus nigra", \
                "Pinus_ponderosa": "Pinus ponderosa", \
                "Pinus_resinosa": "Pinus resinosa", \
                "Pinus_rigida": "Pinus rigida", \
                "Pinus_strobus": "Pinus strobus", \
                "Pinus_sylvestris": "Pinus sylvestris", \
                "Platanus_x": "Platanus x acerifolia", \
                "Populus_alba": "Populus alba", \
                "Populus_balsamifera": "Populus balsamifera", \
                "Populus_grandidentata": "Populus grandidentata", \
                "Populus_nigra_var.": "Populus nigra var. italica", \
                "Populus_tremuloides": "Populus tremuloides", \
                "Populus_x_canadensis": "Populus x canadensis", \
                "Prunus_nigra": "Prunus nigra", \
                "Prunus_pensylvanica": "Prunus pensylvanica", \
                "Prunus_serotina": "Prunus serotina", \
                "Prunus_virginiana": "Prunus virginiana", \
                "Pseudotsuga_menziesii": "Pseudotsuga menziesii", \
                "Ptelea_trifoliata": "Ptelea trifoliata", \
                "Pyrus_calleryana": "Pyrus calleryana", \
                "Quercus_alba": "Quercus alba", \
                "Quercus_macrocarpa": "Quercus macrocarpa", \
                "Quercus_muehlenbergii": "Quercus muehlenbergii", \
                "Quercus_palustris": "Quercus palustris", \
                "Quercus_robur": "Quercus robur", \
                "Quercus_rubra": "Quercus rubra", \
                "Quercus_velutina": "Quercus velutina", \
                "Rhamnus_cathartica": "Rhamnus cathartica", \
                "Rhus_typhina": "Rhus typhina", \
                "Robinia_pseudoacacia": "Robinia pseudoacacia", \
                "Salix_alba_‘Tristis’": "Salix alba ‘Tristis’", \
                "Sambucus_pubens": "Sambucus pubens", \
                "Sassafras_albidum": "Sassafras albidum", \
                "Sorbus_aucuparia": "Sorbus aucuparia", \
                "Syringa_reticulata": "Syringa reticulata", \
                "Syringa_vulgaris": "Syringa vulgaris", \
                "Taxus_canadensis": "Taxus canadensis", \
                "Taxus_x_media": "Taxus x media", \
                "Thuja_occidentalis": "Thuja occidentalis", \
                "Tilia_americana": "Tilia americana", \
                "Tilia_cordata": "Tilia cordata", \
                "Toxicodendron_radicans": "Toxicodendron radicans", \
                "Tsuga_canadensis": "Tsuga canadensis", \
                "Ulmus_americana": "Ulmus americana", \
                "Ulmus_glabra": "Ulmus glabra", \
                "Ulmus_pumila": "Ulmus pumila", \
                "Ulmus_rubra": "Ulmus rubra", \
                "Ulmus_thomasii": "Ulmus thomasii", \
                "Viburnum_acerifolia": "Viburnum acerifolia", \
                "Viburnum_alnifolia": "Viburnum alnifolia", \
                "Viburnum_lentago": "Viburnum lentago", \
                "Viburnum_trilobum": "Viburnum trilobum", \
                "Vitis_riparia": "Vitis riparia", \
                "Xanthocyparis_nootkatensis": "Xanthocyparis nootkatensis", \
                "Zanthoxylum_americanum": "Zanthoxylum americanum", \
                "Zelkova_serrata": "Zelkova serrata", }

                
    for code in domDict:
        arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domName, "CODE", "ASCENDING")
        

    domDict2 = {"02": "02", \
                "04": "04", \
                "06": "06", \
                "08": "08", \
                "10": "10", \
                "12": "12", \
                "14": "14", \
                "16": "16", \
                "18": "18", \
                "20": "20", \
                "22": "22", \
                "24": "24", \
                "26": "26", \
                "28": "28", \
                "30": "30", \
                "32": "32", \
                "34": "34", \
                "36": "36", \
                "38": "38", \
                "40": "40", \
                "42": "42", \
                "44": "44", \
                "46": "46", \
                "48": "48", \
                "50": "50", \
                "52": "52", \
                "54": "54", \
                "56": "56", \
                "58": "58", \
                "60": "60", \
                "62": "62", \
                "64": "64", \
                "66": "66", \
                "68": "68", \
                "70": "70", \
                "72": "72", \
                "74": "74", \
                "76": "76", \
                "78": "78", \
                "80": "80", \
                "82": "82", \
                "84": "84", \
                "86": "86", \
                "88": "88", \
                "90": "90", \
                "92": "92", \
                "94": "94", \
                "96": "96", \
                "98": "98", \
                "100": "100", \
                "102": "102", \
                "104": "104", \
                "106": "106", \
                "108": "108", \
                "110": "110", \
                "112": "112", \
                "114": "114", \
                "116": "116", \
                "118": "118", \
                "120": "120", }
    
    for code in domDict2:
        arcpy.AddCodedValueToDomain_management(gdb, domName2, code, domDict2[code])   

        arcpy.SortCodedValueDomain_management(gdb, domName2, "CODE", "ASCENDING")            
                        
                
    domDict3 = {"a_Excellent": "Excellent", \
                "b_Good": "Good", \
                "c_Fair": "Fair", \
                "d_Poor": "Poor", \
                "e_Dead": "Dead", \
                "f_Stump": "Stump", }

                
    for code in domDict3:
        arcpy.AddCodedValueToDomain_management(gdb, domName3, code, domDict3[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domName3, "CODE", "ASCENDING")
                            
    domDict4 = {"a_Open": "Open", \
                "b_Root_Damage": "Root Damage Suspected", \
                "c_Roots_Confined": "Roots Confined", }
  
    for code in domDict4:
        
        arcpy.AddCodedValueToDomain_management(gdb, domName4, code, domDict4[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domName4, "CODE", "ASCENDING")
   


    domDict5 = {"a_Nothing": "Nothing", \
                "b_Crown_Clean": "Crown Clean", \
                "c_Elevation_Prune": "Elevation Prune", \
                "d_Juvenile_Prune": "Juvenile Prune", \
                "e_Reduce": "Reduce", \
                "f_Remove": "Remove", \
                "g_Grind_Stump": "Grind Stump", \
                "h_Plant": "Plant", }
  
    for code in domDict5:
        
        arcpy.AddCodedValueToDomain_management(gdb, domName5, code, domDict5[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domName5, "CODE", "ASCENDING")
                          
# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
    
   


except Exception as err:
            print(err.args[0])
