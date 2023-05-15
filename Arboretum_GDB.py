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
out_folder_path = "H:/Data" 
out_name = "Arboretum1.gdb"
FeatureName = "Trees_Shrubs"
# Creating a spatial reference object nad 83 utm zone 17 n


# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, out_name)

time.sleep(20)

sr = arcpy.SpatialReference(26917)

try:
# Set the workspace (to avoid having to type in the full path to the data        every time)
    arcpy.env.workspace = "h:/data"
     
        
    
# Set local parameters
    domName = "Scientific_N"
    domName2 = "Common_N"
    domName3 = "Family_N"
    domName4 = "Accession_Num"
    gdb = "Arboretum.gdb"
    inFeatures = "Arboretum1.gdb/Trees_Shrubs"
    Field_Name = "Scientific_N"
    Field_Name2 = "Common_N"
    Field_Name3 = "Family_N"
    Field_Name4 = "Accession_Num"
    #inFeatures = "Montgomery.gdb/Water/Distribmains"
    #inField = "Material"
     

# Process: Create the coded value domain
    arcpy.CreateDomain_management(gdb, domName, "Scientific Name","TEXT", "CODED") 
    
    arcpy.CreateDomain_management(gdb, domName2, "Common Name","TEXT", "CODED")   
    
    arcpy.CreateDomain_management(gdb, domName3, "Family Name","TEXT", "CODED")    
    
    arcpy.CreateDomain_management(gdb, domName4, "Accession Num","TEXT", "CODED")    
   
    time.sleep(10)
# Process: Create the coded value domain
#arcpy.CreateDomain_management("UPDM.gdb", domName, "Gas Systems", "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the  "key" and the
# domain description as the "value" (domDict[code])
    domDict = {"Abies_balsamea": "Abies balsamea", \
                "Acer_nigrum": "Acer nigrum", \
                "Acer_pensylvanicum": "Acer pensylvanicum", \
                "Acer_platanoides": "Acer platanoides", \
                "Acer_pseudoplatanus": "Acer pseudoplatanus", \
                "Acer_rubrum": "Acer rubrum", \
                "Acer_saccharinum": "Acer saccharinum", \
                "Acer_saccharum": "Acer saccharum", \
                "Acer_spicatum": "Acer spicatum", \
                "Acer_x_Freemanii": "Acer x Freemanii", \
                "Aesculus_glabra": "Aesculus glabra", \
                "Aesculus_hippocastanum ": "Aesculus hippocastanum ", \
                "Amelanchier_sanguinea": "Amelanchier sanguinea", \
                "Asimina triloba": "Asimina triloba", \
                "Betula_alleghaniensis": "Betula alleghaniensis", \
                "Betula_nigra": "Betula nigra", \
                "Betula_papyrifera": "Betula papyrifera", \
                "Betula_populifolia": "Betula populifolia", \
                "Carpinus_caroliniana": "Carpinus caroliniana", \
                "Castanea_dentata": "Castanea dentata", \
                "Castanea_dentata_x_mollissima": "Castanea dentata x mollissima", \
                "Catalpa_speciosa": "Catalpa speciosa", \
                "Celtis_occidentalis": "Celtis occidentalis", \
                "Celtis_tenuifolia": "Celtis tenuifolia", \
                "Cercis_canadensis": "Cercis canadensis", \
                "Cornus_alternifolia": "Cornus alternifolia", \
                "Cornus_amomum": "Cornus amomum", \
                "Cornus_racemosa": "Cornus racemosa", \
                "Cornus_sericea": "Cornus sericea", \
                "Dirca_palustris": "Dirca palustris", \
                "Fagus_grandifolia": "Fagus grandifolia", \
                "Fraxinus_americana": "Fraxinus americana", \
                "Fraxinus_nigra": "Fraxinus nigra", \
                "Fraxinus_profunda": "Fraxinus profunda", \
                "Fraxinus_quadrangluata": "Fraxinus quadrangluata", \
                "Ginkgo_biloba": "Ginkgo biloba", \
                "Gleditsia_triacanthos": "Gleditsia triacanthos", \
                "Gymnocladus_dioicus": "Gymnocladus dioicus", \
                "Hammelis_virginiana": "Hammelis virginiana", \
                "Heptacodium_miconioides": "Heptacodium miconioides", \
                "Juglans_cinerea": "Juglans cinerea", \
                "Juglans_nigra": "Juglans nigra", \
                "Juniperus_virginiana": "Juniperus virginiana", \
                "Larix_laricina": "Larix laricina", \
                "Liquidambar_styraciflua": "Liquidambar styraciflua", \
                "Liriodendron_tulipifera": "Liriodendron tulipifera", \
                "Magnolia_acuminata": "Magnolia acuminata", \
                "Metasequoia_glyptostroboides": "Metasequoia glyptostroboides", \
                "Morus_rubra": "Morus rubra", \
                "Nyssa_sylvatica": "Nyssa sylvatica", \
                "Ostrya_virginiana": "Ostrya virginiana", \
                "Phellodendron_amurense": "Phellodendron amurense", \
                "Picea_glauca": "Picea glauca", \
                "Picea_mariana": "Picea mariana", \
                "Pinus_resinosa": "Pinus resinosa", \
                "Pinus_strobus": "Pinus strobus", \
                "Platanus_occidentalis": "Platanus occidentalis", \
                "Platanus_x_acerifolia": "Platanus x acerifolia", \
                "Populus_balsamifera": "Populus balsamifera", \
                "Populus_grandidentata": "Populus grandidentata", \
                "Populus_tremuloides": "Populus tremuloides", \
                "Prunus_pensylvanica": "Prunus pensylvanica", \
                "Prunus_serotina": "Prunus serotina", \
                "Prunus_virginiana": "Prunus virginiana", \
                "Quercus_ellipsoidalis": "Quercus ellipsoidalis", \
                "Quercus_ilicifolia": "Quercus ilicifolia", \
                "Quercus_muehlenbergii": "Quercus muehlenbergii", \
                "Quercus_palustris": "Quercus palustris", \
                "Quercus_prinoides": "Quercus prinoides", \
                "Quercus_rubra": "Quercus rubra", \
                "Quercus_shumardii": "Quercus shumardii", \
                "Quercus_velutina": "Quercus velutina", \
                "Rhus_aromatica": "Rhus aromatica", \
                "Rhus_typhina": "Rhus typhina", \
                "Robinia_pseudoacacia": "Robinia pseudoacacia", \
                "Sambucus_canadensis ": "Sambucus canadensis ", \
                "Sambucus_pubens ": "Sambucus pubens ", \
                "Staphylea_trifolia": "Staphylea trifolia", \
                "Thuja_occidentalis": "Thuja occidentalis", \
                "Tilia_americana": "Tilia americana", \
                "Tsuga_canadensis": "Tsuga canadensis", \
                "Ulmus_americana": "Ulmus americana", \
                "Ulmus_thomasii": "Ulmus thomasii", \
                "Viburnum_dentatum": "Viburnum dentatum", \
                "Viburnum_lantanoides": "Viburnum lantanoides", }

                
    for code in domDict:
        arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])

    domDict2 = {"American_Beech": "American Beech", \
                "American_Bladdernut": "American Bladdernut", \
                "American_Chestnut ": "American Chestnut ", \
                "American_Sycamore": "American Sycamore", \
                "Amur_Corktree": "Amur Corktree", \
                "Arrowwood": "Arrowwood", \
                "Balsam_Fir": "Balsam Fir", \
                "Balsam_Poplar": "Balsam Poplar", \
                "Basswood": "Basswood", \
                "Baumann_Horsechestnut": "Baumann Horsechestnut", \
                "Bear_Oak": "Bear Oak", \
                "Black_Ash": "Black Ash", \
                "Black_Cherry": "Black Cherry", \
                "Black_Elderberry": "Black Elderberry", \
                "Black_Locust": "Black Locust", \
                "Black_Maple": "Black Maple", \
                "Black_Oak": "Black Oak", \
                "Black_Spruce": "Black Spruce", \
                "Black_Walnut": "Black Walnut", \
                "Black-gum": "Black-gum", \
                "Blue_ash": "Blue ash", \
                "Blue-beech": "Blue-beech", \
                "Butternut": "Butternut", \
                "Chinquapin_Oak": "Chinquapin Oak", \
                "Choke_Cherry": "Choke Cherry", \
                "Cucumber-Tree": "Cucumber-Tree", \
                "Dawn_Redwood": "Dawn Redwood", \
                "Dwarf_Chinkapin_Oak": "Dwarf Chinkapin Oak", \
                "Dwarf_Hackberry": "Dwarf Hackberry", \
                "Eastern_Hemlock": "Eastern Hemlock", \
                "Eastern_redbud": "Eastern redbud", \
                "Eastern_Redcedar": "Eastern Redcedar", \
                "Eastern_White_Pine": "Eastern White Pine", \
                "Eastern_White-cedar": "Eastern White-cedar", \
                "Exclamation_Plane-tree": "Exclamation Plane-tree", \
                "Fragrant_sumac": "Fragrant sumac", \
                "Freeman's_Maple": "Freeman's Maple", \
                "Gray_Birch": "Gray Birch", \
                "Gray_Dogwood": "Gray Dogwood", \
                "Hackberry": "Hackberry", \
                "Hobblebush": "Hobblebush", \
                "Honey-locust": "Honey-locust", \
                "Ironwood": "Ironwood", \
                "Kentucky_Coffeetree": "Kentucky Coffeetree", \
                "Largetooth_Aspen": "Largetooth Aspen", \
                "Leatherwood": "Leatherwood", \
                "Maidenhair-tree": "Maidenhair-tree", \
                "Mountain_Maple": "Mountain Maple", \
                "Northern_Catalpa": "Northern Catalpa", \
                "Northern_Pin_Oak": "Northern Pin Oak", \
                "Norway_Maple": "Norway Maple", \
                "Ohio_Buckeye": "Ohio Buckeye", \
                "Pagoda_Dogwood": "Pagoda Dogwood", \
                "Pawpaw": "Pawpaw", \
                "Pin_Cherry": "Pin Cherry", \
                "Pin_Oak": "Pin Oak", \
                "Pumpkin_ash": "Pumpkin ash", \
                "Red_Elderberry": "Red Elderberry", \
                "Red_Maple": "Red Maple", \
                "Red_Mulberry": "Red Mulberry", \
                "Red_Oak": "Red Oak", \
                "Red_Pine": "Red Pine", \
                "Red-osier_Dogwood": "Red-osier Dogwood", \
                "River_Birch": "River Birch", \
                "Rock_Elm": "Rock Elm", \
                "Roundleaf_Serviceberry": "Roundleaf Serviceberry", \
                "Seven-sons_Tree": "Seven-sons Tree", \
                "Shumard's_Oak": "Shumard's Oak", \
                "Silky_Dogwood": "Silky Dogwood", \
                "Silver_Maple": "Silver Maple", \
                "Staghorn_Sumac": "Staghorn Sumac", \
                "Striped_Maple": "Striped Maple", \
                "Sugar_Maple": "Sugar Maple", \
                "Sweetgum": "Sweetgum", \
                "Sycamore_Maple": "Sycamore Maple", \
                "Tamarack": "Tamarack", \
                "Trembling_Aspen": "Trembling Aspen", \
                "Tulip_Tree": "Tulip Tree", \
                "White_Ash": "White Ash", \
                "White_Birch": "White Birch", \
                "White_Elm": "White Elm", \
                "White_Spruce": "White Spruce", \
                "Witch-hazel": "Witch-hazel", \
                "Yellow_Birch": "Yellow Birch", }
    
    for code in domDict2:
        arcpy.AddCodedValueToDomain_management(gdb, domName2, code, domDict2[code])               
                        
                
    domDict3 = {"Aceraceae": "Aceraceae", \
                "Adoxaceae": "Adoxaceae", \
                "Anacardiaceae": "Anacardiaceae", \
                "Annonaceae": "Annonaceae", \
                "Betulaceae": "Betulaceae", \
                "Bignoniaceae": "Bignoniaceae", \
                "Caesalpiniaceae": "Caesalpiniaceae", \
                "Caprifoliaceae": "Caprifoliaceae", \
                "Cornaceae": "Cornaceae", \
                "Cupressaceae": "Cupressaceae", \
                "Fabaceae": "Fabaceae", \
                "Fagaceae": "Fagaceae", \
                "Ginkgoaceae": "Ginkgoaceae", \
                "Hamamelidaceae": "Hamamelidaceae", \
                "Hippocastanaceae": "Hippocastanaceae", \
                "Juglandaceae": "Juglandaceae", \
                "Magnoliaceae": "Magnoliaceae", \
                "Moraceae": "Moraceae", \
                "Oleaceae": "Oleaceae", \
                "Pinaceae": "Pinaceae", \
                "Platanaceae": "Platanaceae", \
                "Rosaceae": "Rosaceae", \
                "Salicaceae": "Salicaceae", \
                "Staphyleaceae": "Staphyleaceae", \
                "Thymelaeaceae": "Thymelaeaceae", \
                "Tiliaceae": "Tiliaceae", \
                "Ulmaceae": "Ulmaceae", }

                
    for code in domDict3:
        arcpy.AddCodedValueToDomain_management(gdb, domName3, code, domDict3[code])
                            
    domDict4 = {"2018-01": "2018-01", \
                    "2018-02": "2018-02", \
                    "2018-03": "2018-03", \
                    "2018-04": "2018-04", \
                    "2018-05": "2018-05", \
                    "2018-06": "2018-06", \
                    "2018-07": "2018-07", \
                    "2018-08": "2018-08", \
                    "2018-09": "2018-09", \
                    "2018-10": "2018-10", \
                    "2018-11": "2018-11", \
                    "2018-12A": "2018-12A", \
                    "2018-12B": "2018-12B", \
                    "2018-13": "2018-13", \
                    "2018-14": "2018-14", \
                    "2018-15": "2018-15", \
                    "2018-16": "2018-16", \
                    "2018-17": "2018-17", \
                    "2018-18A": "2018-18A", \
                    "2018-18B": "2018-18B", \
                    "2018-19A": "2018-19A", \
                    "2018-19B": "2018-19B", \
                    "2018-20": "2018-20", \
                    "2018-21": "2018-21", \
                    "2018-22": "2018-22", \
                    "2018-23A": "2018-23A", \
                    "2018-23B": "2018-23B", \
                    "2018-24": "2018-24", \
                    "2018-25": "2018-25", \
                    "2018-26": "2018-26", \
                    "2018-27": "2018-27", \
                    "2018-28": "2018-28", \
                    "2018-29A": "2018-29A", \
                    "2018-29B": "2018-29B", \
                    "2018-30": "2018-30", \
                    "2018-31": "2018-31", \
                    "2018-32A": "2018-32A", \
                    "2018-32B": "2018-32B", \
                    "2018-33A": "2018-33A", \
                    "2018-33B": "2018-33B", \
                    "2018-34A": "2018-34A", \
                    "2018-34B": "2018-34B", \
                    "2018-35A": "2018-35A", \
                    "2018-35B": "2018-35B", \
                    "2018-36": "2018-36", \
                    "2018-37": "2018-37", \
                    "2018-38": "2018-38", \
                    "2018-39": "2018-39", \
                    "2018-40": "2018-40", \
                    "2018-41": "2018-41", \
                    "2018-42": "2018-42", \
                    "2018-43": "2018-43", \
                    "2018-44": "2018-44", \
                    "2018-45": "2018-45", \
                    "2018-46": "2018-46", \
                    "2018-47": "2018-47", \
                    "2018-48": "2018-48", \
                    "2018-49": "2018-49", \
                    "2018-50": "2018-50", \
                    "2018-51A": "2018-51A", \
                    "2018-51B": "2018-51B", \
                    "2018-51C": "2018-51C", \
                    "2018-52": "2018-52", \
                    "2018-53": "2018-53", \
                    "2018-54": "2018-54", \
                    "2018-55": "2018-55", \
                    "2018-56": "2018-56", \
                    "2018-57": "2018-57", \
                    "2018-58": "2018-58", \
                    "2018-59": "2018-59", \
                    "2018-60": "2018-60", \
                    "2018-61": "2018-61", \
                    "2018-62": "2018-62", \
                    "2018-63": "2018-63", \
                    "2018-64": "2018-64", \
                    "2018-65": "2018-65", \
                    "2018-66": "2018-66", \
                    "2018-67": "2018-67", \
                    "2018-68": "2018-68", \
                    "2018-69": "2018-69", \
                    "2018-70": "2018-70", \
                    "2018-71": "2018-71", \
                    "2018-72": "2018-72", \
                    "2018-73A": "2018-73A", \
                    "2018-73B": "2018-73B", \
                    "2018-74A": "2018-74A", \
                    "2018-74B": "2018-74B", \
                    "2018-75A": "2018-75A", \
                    "2018-75B": "2018-75B", \
                    "2018-76A": "2018-76A", \
                    "2018-76B": "2018-76B", \
                    "2018-76C": "2018-76C", \
                    "2018-77": "2018-77", \
                    "2018-78A": "2018-78A", \
                    "2018-78B": "2018-78B", \
                    "2018-79": "2018-79", \
                    "2018-80": "2018-80", \
                    "2018-81": "2018-81", \
                    "2018-82A": "2018-82A", \
                    "2018-82B": "2018-82B", \
                    "2018-82C": "2018-82C", \
                    "2018-82D": "2018-82D", \
                    "2018-82E": "2018-82E", \
                    "2018-82F": "2018-82F", \
                    "2018-83": "2018-83", \
                    "2018-84A": "2018-84A", \
                    "2018-84B": "2018-84B", \
                    "2018-85A": "2018-85A", \
                    "2018-85B": "2018-85B", \
                    "2018-86A": "2018-86A", \
                    "2018-86B": "2018-86B", \
                    "2018-87A": "2018-87A", \
                    "2018-87B": "2018-87B", \
                    "2018-88A": "2018-88A", \
                    "2018-88B": "2018-88B", \
                    "2018-89A": "2018-89A", \
                    "2018-89B": "2018-89B", \
                    "2018-90": "2018-90", \
                    "2018-91": "2018-91", \
                    "2018-92": "2018-92", }
  
    for code in domDict4:
        arcpy.AddCodedValueToDomain_management(gdb, domName4, code, domDict4[code])
                             
# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
    
   


except Exception as err:
            print(err.args[0])
