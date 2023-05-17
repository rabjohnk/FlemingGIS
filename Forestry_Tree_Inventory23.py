# -*- coding: utf-8 -*-

# Description: Create a file GDB

# Import system modules
import arcpy
import time

# Set local variables
out_folder_path = "H:\data\Forestry23\\data" 
out_path = "H:\data\Forestry23\\data"
out_dataset_path = "H:\data\Forestry23\\data\Treeinventory2023a.gdb"
gdb = "Treeinventory2023a.gdb"
out_Feature_name = "Trees"
geometry_type = "POINT"
template = "DISABLED"
#domName = "Student_Name"
domNTreeNum = "Tree_Number"
domTreeName = "Tree_Name"
domNameArb = "Arboretum_Tag"
domNameBark = "Bark_Stage"
domNameCondition = "Condition"
domnameCavity = "Cavity"
domNameMast = "Mast"
domNameGrowing = "Growing_Stock"
domNameMajor1 = "Major_Defect1"
domNameMajor2 = "Major_Defect2"
domNameMajor3 = "Major_Defect3"
domMod1 = "Moderate_Defect1"
domMod2 = "Moderate_Defect2"
domMod3 = "Moderate_Defect3"
domMin1 = "Minor_Defect1"
domMin2 = "Minor_Defect2"
domMin3 = "Minor_Defect3"
domPatho1 = "Other_Pathagens1"
domPatho2 = "Other_Pathagens2"
domPatho3 = "Other_Pathagens3"
domWork1 = "Work1"
domWork2 = "Work2"
domWork3 = "Work3"
domNotes = "Notes"

inFeatures = "H:\data\Forestry23\\data\Treeinventory2023a.gdb\Trees"
#Field_Name = "Student_Name"
Field_Tree = "Tree_Number"
Field_DBH = "DBH"
Field_TreeName = "Scientific_N"
Field_NameSpec = "Species_Not_Listed"
Field_Arb = "Arboretum_Tag"
Field_Bark = "Bark_Stage"
Field_Condition = "Condition"
Field_Cavity = "Cavity"
Field_Mast = "Mast"
Field_Growing = "Growing_Stock"
FieldMajor1 = "Major_Defect1"
FieldMajor2 = "Major_Defect2"
FieldMajor3 = "Major_Defect3"
FieldMod1 = "Moderate_Defect1"
FieldMod2 = "Moderate_Defect2"
FieldMod3 = "Moderate_Defect3"
FieldMin1 = "Minor_Defect1"
FieldMin2 = "Minor_Defect2"
FieldMin3 = "Minor_Defect3"
FieldPatho1 = "Other_Pathagens1"
FieldPatho2 = "Other_Pathagens2"
FieldPatho3 = "Other_Pathagens3"
FieldWork1 = "Work1"
FieldWork2 = "Work2"
FieldWork3 = "Work3"
Field_Notes = "Notes"
field_length = 30
Field_Name_Length = 125
Notes_Length = 125
    


# Execute CreateFileGDB
arcpy.CreateFileGDB_management(out_folder_path, gdb)

#time.sleep(20)

sr = arcpy.SpatialReference(3857)


# Set the workspace (to avoid having to type in the full path to the data        every time)
arcpy.env.workspace = "H:\data\Forestry23\\data"
     
  # Execute CreateFeatureclass

arcpy.CreateFeatureclass_management(out_dataset_path, out_Feature_name, geometry_type, spatial_reference = sr)      
    
# Set local parameters
   
     

# Process: Create the coded value domain

arcpy.CreateDomain_management(gdb, domTreeName, "Tree_Name", "TEXT", "CODED") 

arcpy.CreateDomain_management(gdb, domNameArb, "Arboretum_Tag","TEXT", "CODED")   
        
arcpy.CreateDomain_management(gdb, domNameBark, "Bark_Stage","TEXT", "CODED")    
        
arcpy.CreateDomain_management(gdb, domNameCondition, "Condition","TEXT", "CODED") 
        
arcpy.CreateDomain_management(gdb, domnameCavity, "Cavity","TEXT", "CODED")

arcpy.CreateDomain_management(gdb, domNameMast, "Mast","TEXT", "CODED")

arcpy.CreateDomain_management(gdb, domNameGrowing, "Growing_Stock","TEXT", "CODED")

arcpy.CreateDomain_management(gdb, domNameMajor1, "Major_Defect1","TEXT", "CODED")

arcpy.CreateDomain_management(gdb, domNameMajor2, "Major_Defect2","TEXT", "CODED")

arcpy.CreateDomain_management(gdb, domNameMajor3, "Major_Defect3","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domMod1, "Moderate_Defect1","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domMod2, "Moderate_Defect2","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domMod3, "Moderate_Defect3","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domMin1, "Minor_Defect1","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domMin2, "Minor_Defect2","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domMin3, "Minor_Defect3","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domPatho1, "Other_Pathagens1","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domPatho2, "Other_Pathagens2","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domPatho3, "Other_Pathagens3","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domWork1, "Work1","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domWork2, "Work2","TEXT", "CODED")
arcpy.CreateDomain_management(gdb, domWork3, "Work3","TEXT", "CODED")


    
#arcpy.CreateDomain_management(gdb, domName6, "Notes","TEXT")
   
#time.sleep(10)
# Process: Create the coded value domain
#arcpy.CreateDomain_management("UPDM.gdb", domName, "Gas Systems", "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the  "key" and the
# domain description as the "value" (domDict[code])
#domDict01 = {"Tree_Number": "Tree Number", }

#for code in domDict01:
        #arcpy.AddCodedValueToDomain_management(gdb, domName01, code, domDict01[code])
        
        #arcpy.SortCodedValueDomain_management(gdb, domName01, "CODE", "ASCENDING")

domDict = {"Abies_balsamea": "Abies balsamea", \
                "Abies_concolor": "Abies concolor", \
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
                "Aegopodium_podagraria": "Aegopodium podagraria", \
                "Aesculus_glabra": "Aesculus glabra", \
                "Aesculus_hippocastanum": "Aesculus hippocastanum", \
                "Ailanthus_altissima": "Ailanthus altissima", \
                "Alnus_glutinosa": "Alnus glutinosa", \
                "Alnus_incana_ssp_rugosa": "Alnus incana ssp. rugosa", \
                "Amelanchier_spp": "Amelanchier spp", \
                "Aralia_elata": "Aralia elata", \
                "Betula_alleghaniensis": "Betula alleghaniensis", \
                "Betula_nigra": "Betula nigra", \
                "Betula_papyrifera": "Betula papyrifera", \
                "Betula_pendula": "Betula pendula", \
                "Callitropsis_nootkatensis_Xanthocyparis_nootkatensis": "Callitropsis nootkatensis/Xanthocyparis nootkatensis", \
                "Carpinus_caroliniana": "Carpinus caroliniana", \
                "Carya_cordiformis": "Carya cordiformis", \
                "Carya_ovata": "Carya ovata", \
                "Castanea_dentata": "Castanea dentata", \
                "Catalpa_speciosa": "Catalpa speciosa", \
                "Celastrus_scandens": "Celastrus scandens", \
                "Celtis_occidentalis": "Celtis occidentalis", \
                "Cercidiphyllum_japonicum": "Cercidiphyllum japonicum", \
                "Cercis_canadensis": "Cercis canadensis", \
                "Chaenomeles_japonica": "Chaenomeles japonica", \
                "Chaenomeles_speciosa": "Chaenomeles speciosa", \
                "Cladrastis_kentukea": "Cladrastis kentukea", \
                "Cornus alba": "Cornus alba", \
                "Cornus_alternifolia": "Cornus alternifolia", \
                "Cornus florida": "Cornus florida", \
                "Cornus_kousa": "Cornus kousa", \
                "Cornus_mas": "Cornus mas", \
                "Cornus_rugosa": "Cornus rugosa", \
                "Cornus_sericea": "Cornus sericea", \
                "Corylus_americana": "Corylus americana", \
                "Corylus_avellana": "Corylus avellana", \
                "Corylus_colurna": "Corylus colurna", \
                "Corylus_cornuta": "Corylus cornuta", \
                "Cotinus_coggygria": "Cotinus coggygria", \
                "Cotoneaster_apiculatus": "Cotoneaster apiculatus", \
                "Cotoneaster_dammeri" : "Cotoneaster dammeri", \
                "Cotoneaster_horizontalis" : "Cotoneaster horizontalis", \
                "Crataegus_spp" : "Crataegus spp", \
                "Diervilla_lonicera" : "Diervilla lonicera", \
                "Dirca_palustris" : "Dirca palustris", \
                "Elaeagnus_angustifolia" : "Elaeagnus angustifolia", \
                "Eleagnus_umbellata" : "Eleagnus umbellata", \
                "Euonymus_alatus" : "Euonymus alatus", \
                "Fagus_grandifolia" : "Fagus grandifolia", \
                "Fagus_sylvatica" : "Fagus sylvatica", \
                "Forsythia_ovata" : "Forsythia ovata", \
                "Forsythia_x" : "Forsythia x intermedia", \
                "Fraxinus_americana" : "Fraxinus americana", \
                "Fraxinus_excelsior" : "Fraxinus excelsior", \
                "Fraxinus_nigra" : "Fraxinus nigra", \
                "Fraxinus_pennsylvanica" : "Fraxinus pennsylvanica", \
                "Ginkgo_biloba" : "Ginkgo biloba", \
                "Gleditsia_triacanthos" : "Gleditsia triacanthos", \
                "Gymnocladus_dioicus" : "Gymnocladus dioicus", \
                "Hamamelis_mollis" : "Hamamelis mollis", \
                "Hamamelis_vernalis" : "Hamamelis vernalis", \
                "Hamamelis_virginiana" : "Hamamelis virginiana", \
                "Hamamelis_x" : "Hamamelis x intermedia", \
                "Heptacodium_miconoides" : "Heptacodium miconoides", \
                "Hibiscus_syriacus" : "Hibiscus syriacus", \
                "Hippophae_rhamnoides" : "Hippophae rhamnoides", \
                "Juglans_cinerea" : "Juglans cinerea", \
                "Juglans_nigra" : "Juglans nigra", \
                "Juniperus_communis" : "Juniperus communis var. depressa", \
                "Juniperus_horizontalis" : "Juniperus horizontalis", \
                "Juniperus_virginiana" : "Juniperus virginiana", \
                "Larix_decidua" : "Larix decidua", \
                "Larix_kaempferi" : "Larix kaempferi", \
                "Larix_laricina" : "Larix laricina", \
                "Liquidambar_styraciflua" : "Liquidambar styraciflua", \
                "Liriodendron_tulipifera" : "Liriodendron tulipifera", \
                "Lonicera_tartaricum" : "Lonicera tartaricum", \
                "Magnolia_acuminata" : "Magnolia acuminata", \
                "Magnolia_spp." : "Magnolia spp.", \
                "Magnolia_x" : "Magnolia x soulangiana", \
                "Malus_sp." : "Malus sp.", \
                "Metasequoia_glyptostroboides" : "Metasequoia glyptostroboides", \
                "Morus_alba" : "Morus alba", \
                "Morus_rubra" : "Morus rubra", \
                "Muscari_armeniacum" : "Muscari armeniacum", \
                "Nicotiana_alata" : "Nicotiana alata", \
                "Osteospermum_x" : "Osteospermum x hybrida", \
                "Ostrya_virginiana" : "Ostrya virginiana", \
                "Parthenocissus_spp." : "Parthenocissus spp.", \
                "Parthenocissus_vitacea" : "Parthenocissus vitacea", \
                "Phellodendron_amurense" : "Phellodendron amurense", \
                "Picea_abies" : "Picea abies", \
                "Picea_glauca" : "Picea glauca", \
                "Picea_mariana" : "Picea mariana", \
                "Picea_omorika" : "Picea omorika", \
                "Picea_pungens" : "Picea pungens", \
                "Pinus_banksiana" : "Pinus banksiana", \
                "Pinus_cembra" : "Pinus cembra", \
                "Pinus_mugo" : "Pinus mugo", \
                "Pinus_nigra" : "Pinus nigra", \
                "Pinus_ponderosa" : "Pinus ponderosa", \
                "Pinus_resinosa" : "Pinus resinosa", \
                "Pinus_rigida" : "Pinus rigida", \
                "Pinus_strobus" : "Pinus strobus", \
                "Pinus_sylvestris" : "Pinus sylvestris", \
                "Platanus_occidentalis" : "Platanus occidentalis", \
                "Platanus_x" : "Platanus x acerifolia", \
                "Populus_alba" : "Populus alba", \
                "Populus_balsamifera" : "Populus balsamifera", \
                "Populus_deltoides" : "Populus deltoides", \
                "Populus_grandidentata" : "Populus grandidentata", \
                "Populus_nigra" : "Populus nigra var. italica", \
                "Populus_tremuloides" : "Populus tremuloides", \
                "Populus_x" : "Populus x canadensis", \
                "Prunus_nigra" : "Prunus nigra", \
                "Prunus_pensylvanica" : "Prunus pensylvanica", \
                "Prunus_serotina" : "Prunus serotina", \
                "Prunus_virginiana" : "Prunus virginiana", \
                "Pseudotsuga_menziesii" : "Pseudotsuga menziesii", \
                "Ptelea_trifoliata" : "Ptelea trifoliata", \
                "Pyrus_calleryana" : "Pyrus calleryana", \
                "Quercus_alba" : "Quercus alba", \
                "Quercus_macrocarpa" : "Quercus macrocarpa", \
                "Quercus_muehlenbergii" : "Quercus muehlenbergii", \
                "Quercus_palustris" : "Quercus palustris", \
                "Quercus_robur" : "Quercus robur", \
                "Quercus_rubra" : "Quercus rubra", \
                "Quercus_velutina" : "Quercus velutina", \
                "Rhamnus_cathartica" : "Rhamnus cathartica", \
                "Rhododendron_tomentosum" : "Rhododendron tomentosum", \
                "Rhus_typhina" : "Rhus typhina", \
                "Ribes_spp." : "Ribes spp.", \
                "Robinia_pseudoacacia" : "Robinia pseudoacacia", \
                "Rubus_occidentalis" : "Rubus occidentalis", \
                "Rubus_odoratus" : "Rubus odoratus", \
                "Rubus_sachalinensis" : "Rubus sachalinensis var. sachalinensis/Rubus idaeus", \
                "Salix_alba" : "Salix alba 'tristis'", \
                "Salix_fragilis" : "Salix fragilis", \
                "Salix_nigra" : "Salix nigra", \
                "Sambucus_racemosa" : "Sambucus racemosa var. pubens/Sambucus pubens", \
                "Sassafras_albidum" : "Sassafras albidum", \
                "Sorbus_spp." : "Sorbus spp.", \
                "Syringa_reticulata" : "Syringa reticulata", \
                "Syringa_vulgaris" : "Syringa vulgaris", \
                "Taxus_canadensis" : "Taxus canadensis", \
                "Taxus_x" : "Taxus x media", \
                "Thuja_occidentalis" : "Thuja occidentalis", \
                "Tilia_americana" : "Tilia americana", \
                "Tilia_cordata" : "Tilia cordata", \
                "Toxicodendron_radicans" : "Toxicodendron radicans", \
                "Tsuga_canadensis" : "Tsuga canadensis", \
                "Ulmus_americana" : "Ulmus americana", \
                "Ulmus_glabra" : "Ulmus glabra", \
                "Ulmus_pumila" : "Ulmus pumila", \
                "Ulmus_rubra" : "Ulmus rubra", \
                "Ulmus_thomasii" : "Ulmus thomasii", \
                "Viburnum_acerifolium" : "Viburnum acerifolium", \
                "Viburnum_lantana" : "Viburnum lantana", \
                "Viburnum_lantanoides" : "Viburnum lantanoides ", \
                "Viburnum_lentago" : "Viburnum lentago", \
                "Viburnum_opulus" : "Viburnum opulus var. americanum/Viburnum trilobum", \
                "Vitis_spp." : "Vitis spp.", \
                "Zanthoxylum_americanum" : "Zanthoxylum americanum", \
                "Zelkova_serrata" : "Zelkova serrata", }
                 
for code in domDict:
                arcpy.management.AddCodedValueToDomain(gdb, domTreeName, code, domDict[code])
        
                arcpy.management.SortCodedValueDomain(gdb, domTreeName, "CODE", "ASCENDING")
        

domDictArb = {"a_Yes": "Yes", \
                "b_No": "No", \
                "c_Missing": "Missing", }
                    
for code in domDictArb:
        arcpy.AddCodedValueToDomain_management(gdb, domNameArb, code, domDictArb[code])   

        arcpy.SortCodedValueDomain_management(gdb, domNameArb, "CODE", "ASCENDING")   


domDictBark = {"a_Juvenile" : "Juvenile", \
                "b_Mature" : "Mature",\
                "c_J-M" : "J-M", }

for code in domDictBark:
        arcpy.AddCodedValueToDomain_management(gdb, domNameBark, code, domDictBark[code])   

        arcpy.SortCodedValueDomain_management(gdb, domNameBark, "CODE", "ASCENDING")   
                
domDictCondition = {"a_Excellent": "Excellent", \
                "b_Good": "Good", \
                "c_Fair": "Fair", \
                "d_Poor": "Poor", \
                "e_Dead": "Dead", \
                "f_Stump": "Stump", }

                
for code in domDictCondition:
        arcpy.AddCodedValueToDomain_management(gdb, domNameCondition, code, domDictCondition[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domNameCondition, "CODE", "ASCENDING")
                            
domDictCavity = {"a_C1": "C1", \
                  "b_C2": "C2", }
  
for code in domDictCavity:
        
        arcpy.AddCodedValueToDomain_management(gdb, domnameCavity, code, domDictCavity[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domnameCavity, "CODE", "ASCENDING")
   


domDictMast = {"a_M1": "M1", \
                "b_M2": "M2", }
  
for code in domDictMast:
        
        arcpy.AddCodedValueToDomain_management(gdb, domNameMast, code, domDictMast[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domNameMast, "CODE", "ASCENDING")

domDictGrowing = {"a_AGS": "AGS", \
                "b_UGS": "UGS", }
  
for code in domDictGrowing:
        
        arcpy.AddCodedValueToDomain_management(gdb, domNameGrowing, code, domDictGrowing[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domNameGrowing, "CODE", "ASCENDING")

domDictMajor1 = {"Artist's Conk": "Artist's Conk", \
                "Beech Bark Disease": "Beech Bark Disease", \
                "Black Bark": "Black Bark", \
                "Butt Flare": "Butt Flare", \
                "Butternut Canker": "Butternut Canker", \
                "Clinker Fungus": "Clinker Fungus", \
                "Coal Fungus": "Coal Fungus", \
                "Eutypella Canker": "Eutypella Canker", \
                "False Tinder Fungus": "False Tinder Fungus", \
                "Fire Scar": "Fire Scar", \
                "Large Dark-faced Scar": "Large Dark-faced Scar", \
                "Nectria Canker": "Nectria Canker", \
                "Punk Knot": "Punk Knot", \
                "Shoestring Root Rot": "Shoestring Root Rot", \
                "Spine Tooth Fungus": "Spine Tooth Fungus", \
                "Yellow Cap Fungus": "Yellow Cap Fungus", }
  
for code in domDictMajor1:
        
        arcpy.AddCodedValueToDomain_management(gdb, domNameMajor1, code, domDictMajor1[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domNameMajor1, "CODE", "ASCENDING") 

domDictMajor2 = {"Artist's Conk": "Artist's Conk", \
                "Beech Bark Disease": "Beech Bark Disease", \
                "Black Bark": "Black Bark", \
                "Butt Flare": "Butt Flare", \
                "Butternut Canker": "Butternut Canker", \
                "Clinker Fungus": "Clinker Fungus", \
                "Coal Fungus": "Coal Fungus", \
                "Eutypella Canker": "Eutypella Canker", \
                "False Tinder Fungus": "False Tinder Fungus", \
                "Fire Scar": "Fire Scar", \
                "Large Dark-faced Scar": "Large Dark-faced Scar", \
                "Nectria Canker": "Nectria Canker", \
                "Punk Knot": "Punk Knot", \
                "Shoestring Root Rot": "Shoestring Root Rot", \
                "Spine Tooth Fungus": "Spine Tooth Fungus", \
                "Yellow Cap Fungus": "Yellow Cap Fungus", }
  
for code in domDictMajor2:
        
        arcpy.AddCodedValueToDomain_management(gdb, domNameMajor2, code, domDictMajor2[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domNameMajor2, "CODE", "ASCENDING") 

domDictMajor3 = {"Artist's Conk": "Artist's Conk", \
                "Beech Bark Disease": "Beech Bark Disease", \
                "Black Bark": "Black Bark", \
                "Butt Flare": "Butt Flare", \
                "Butternut Canker": "Butternut Canker", \
                "Clinker Fungus": "Clinker Fungus", \
                "Coal Fungus": "Coal Fungus", \
                "Eutypella Canker": "Eutypella Canker", \
                "False Tinder Fungus": "False Tinder Fungus", \
                "Fire Scar": "Fire Scar", \
                "Large Dark-faced Scar": "Large Dark-faced Scar", \
                "Nectria Canker": "Nectria Canker", \
                "Punk Knot": "Punk Knot", \
                "Shoestring Root Rot": "Shoestring Root Rot", \
                "Spine Tooth Fungus": "Spine Tooth Fungus", \
                "Yellow Cap Fungus": "Yellow Cap Fungus", }
  
for code in domDictMajor3:
        
        arcpy.AddCodedValueToDomain_management(gdb, domNameMajor3, code, domDictMajor3[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domNameMajor3, "CODE", "ASCENDING") 

domDictMod1 = {"Black_Knot": "Black Knot",\
                "Frost_Crack": "Frost Crack",\
                "Lean_10": "Lean > 10%",\
                "Mossy_Top": "Mossy Top Fungus",\
                "Small_Dark-faced": "Small Dark-faced Scar",\
                "Spiral_seam": "Spiral seam",\
                "Sugar_Maple_ Dark-faced": "Sugar Maple Borer - Dark-faced, large",\
                "Sugar_Maple_White-faced": "Sugar Maple Borer - White-faced, small",\
                "Sunscald": "Sunscald",}               

for code in domDictMod1:
        
        arcpy.AddCodedValueToDomain_management(gdb, domMod1, code, domDictMod1[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domMod1, "CODE", "ASCENDING") 

domDictMod2 = {"Black_Knot": "Black Knot",\
                "Frost_Crack": "Frost Crack",\
                "Lean_10": "Lean > 10%",\
                "Mossy_Top": "Mossy Top Fungus",\
                "Small_Dark-faced": "Small Dark-faced Scar",\
                "Spiral_seam": "Spiral seam",\
                "Sugar_Maple_ Dark-faced": "Sugar Maple Borer - Dark-faced, large",\
                "Sugar_Maple_White-faced": "Sugar Maple Borer - White-faced, small",\
                "Sunscald": "Sunscald",}                 

for code in domDictMod2:
        
        arcpy.AddCodedValueToDomain_management(gdb, domMod2, code, domDictMod2[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domMod2, "CODE", "ASCENDING") 

domDictMod3 = {"Black_Knot": "Black Knot",\
                "Frost_Crack": "Frost Crack",\
                "Lean_10": "Lean > 10%",\
                "Mossy_Top": "Mossy Top Fungus",\
                "Small_Dark-faced": "Small Dark-faced Scar",\
                "Spiral_seam": "Spiral seam",\
                "Sugar_Maple_ Dark-faced": "Sugar Maple Borer - Dark-faced, large",\
                "Sugar_Maple_White-faced": "Sugar Maple Borer - White-faced, small",\
                "Sunscald": "Sunscald",}

                 

for code in domDictMod3:
        
        arcpy.AddCodedValueToDomain_management(gdb, domMod3, code, domDictMod3[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domMod3, "CODE", "ASCENDING") 


domDictMin1 = {"Burl_": "Burl",\
                "Crook_and": "Crook and Sweep",\
                "Epicormic_Branching": "Epicormic Branching",\
                "White-faced_scar": "White-faced scar",}         

for code in domDictMin1:
        
        arcpy.AddCodedValueToDomain_management(gdb, domMin1, code, domDictMin1[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domMin1, "CODE", "ASCENDING") 

domDictMin2 = {"Burl_": "Burl",\
                "Crook_and": "Crook and Sweep",\
                "Epicormic_Branching": "Epicormic Branching",\
                "White-faced_scar": "White-faced scar",}         

for code in domDictMin2:
        
        arcpy.AddCodedValueToDomain_management(gdb, domMin2, code, domDictMin2[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domMin2, "CODE", "ASCENDING") 

domDictMin3 = {"Burl_": "Burl",\
                "Crook_and": "Crook and Sweep",\
                "Epicormic_Branching": "Epicormic Branching",\
                "White-faced_scar": "White-faced scar",}         

for code in domDictMin3:
        
        arcpy.AddCodedValueToDomain_management(gdb, domMin3, code, domDictMin3[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domMin3, "CODE", "ASCENDING") 

domDictPath1 = {"Adelgid_":"Adelgid",\
                "Animal_Damage,": "Animal Damage, porcupine",\
                "Animal_Damage,": "Animal Damage, rodent",\
                "Borer,_Bronze": "Borer, Bronze Birch",\
                "Borer,_Emerald": "Borer, Emerald Ash",\
                "Borer,_Sugar": "Borer, Sugar Maple",\
                "Compaction_": "Compaction",\
                "DED_": "DED",\
                "Dieback_>": "Dieback > 25%",\
                "Diplodia_": "Diplodia",\
                "Eastern_Tent": "Eastern Tent",\
                "Fall_Webworm": "Fall Webworm",\
                "Frost_Crack": "Frost Crack",\
                "Gall,_spindle/bladder": "Gall, spindle/bladder",\
                "Girdling_Root": "Girdling Root Suspected",\
                "Hypoxylon_": "Hypoxylon",\
                "Inclusion_": "Inclusion",\
                "Mechanical_Damage": "Mechanical Damage",\
                "Needlecast_": "Needlecast",\
                "Skeletonizer_": "Skeletonizer",\
                "Sooty_Mould": "Sooty Mould",\
                "Split_Gill": "Split Gill ",\
                "Spongy_Moth": "Spongy Moth",\
                "Tar_Spot": "Tar Spot",\
                "Thyronectria_": "Thyronectria",\
                "Tinder_Polypore": "Tinder Polypore",\
                "Witches'_Broom": "Witches' Broom",}         

for code in domDictPath1:
        
        arcpy.AddCodedValueToDomain_management(gdb, domPatho1, code, domDictPath1[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domPatho1, "CODE", "ASCENDING") 

domDictPath2 = {"Adelgid_": "Adelgid",\
                "Animal_Damage,": "Animal Damage, porcupine",\
                "Animal_Damage,": "Animal Damage, rodent",\
                "Borer,_Bronze": "Borer, Bronze Birch",\
                "Borer,_Emerald": "Borer, Emerald Ash",\
                "Borer,_Sugar": "Borer, Sugar Maple",\
                "Compaction_": "Compaction",\
                "DED_": "DED",\
                "Dieback_>": "Dieback > 25%",\
                "Diplodia_": "Diplodia",\
                "Eastern_Tent": "Eastern Tent",\
                "Fall_Webworm": "Fall Webworm",\
                "Frost_Crack": "Frost Crack",\
                "Gall,_spindle/bladder": "Gall, spindle/bladder",\
                "Girdling_Root": "Girdling Root Suspected",\
                "Hypoxylon_": "Hypoxylon",\
                "Inclusion_": "Inclusion",\
                "Mechanical_Damage": "Mechanical Damage",\
                "Needlecast_": "Needlecast",\
                "Skeletonizer_": "Skeletonizer",\
                "Sooty_Mould": "Sooty Mould",\
                "Split_Gill": "Split Gill ",\
                "Spongy_Moth": "Spongy Moth",\
                "Tar_Spot": "Tar Spot",\
                "Thyronectria_": "Thyronectria",\
                "Tinder_Polypore": "Tinder Polypore",\
                "Witches'_Broom": "Witches' Broom",}         

for code in domDictPath2:
        
        arcpy.AddCodedValueToDomain_management(gdb, domPatho2, code, domDictPath2[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domPatho2, "CODE", "ASCENDING") 

domDictPath3 = {"Adelgid_": "Adelgid",\
                "Animal_Damage,": "Animal Damage, porcupine",\
                "Animal_Damage,": "Animal Damage, rodent",\
                "Borer,_Bronze": "Borer, Bronze Birch",\
                "Borer,_Emerald": "Borer, Emerald Ash",\
                "Borer,_Sugar": "Borer, Sugar Maple",\
                "Compaction_": "Compaction",\
                "DED_": "DED",\
                "Dieback_>": "Dieback > 25%",\
                "Diplodia_": "Diplodia",\
                "Eastern_Tent": "Eastern Tent",\
                "Fall_Webworm": "Fall Webworm",\
                "Frost_Crack": "Frost Crack",\
                "Gall,_spindle/bladder": "Gall, spindle/bladder",\
                "Girdling_Root": "Girdling Root Suspected",\
                "Hypoxylon_": "Hypoxylon",\
                "Inclusion_": "Inclusion",\
                "Mechanical_Damage": "Mechanical Damage",\
                "Needlecast_": "Needlecast",\
                "Skeletonizer_": "Skeletonizer",\
                "Sooty_Mould": "Sooty Mould",\
                "Split_Gill": "Split Gill ",\
                "Spongy_Moth": "Spongy Moth",\
                "Tar_Spot": "Tar Spot",\
                "Thyronectria_": "Thyronectria",\
                "Tinder_Polypore": "Tinder Polypore",\
                "Witches'_Broom": "Witches' Broom",}         

for code in domDictPath3:
        
        arcpy.AddCodedValueToDomain_management(gdb, domPatho3, code, domDictPath3[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domPatho3, "CODE", "ASCENDING")  

domDictwork1 = {"PHC,_Air": "PHC, Air Spade",\
                "PHC,_Inject": "PHC, Inject",\
                "Prune_": "Prune",\
                "Release_": "Release",\
                "Remove_": "Remove",\
                "Stump_Grind": "Stump Grind",}

for code in domDictwork1:
        
        arcpy.AddCodedValueToDomain_management(gdb, domWork1, code, domDictwork1[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domWork1, "CODE", "ASCENDING")  

domDictwork2 = {"PHC,_Air": "PHC, Air Spade",\
                "PHC,_Inject": "PHC, Inject",\
                "Prune_": "Prune",\
                "Release_": "Release",\
                "Remove_": "Remove",\
                "Stump_Grind": "Stump Grind",}

for code in domDictwork2:
        
        arcpy.AddCodedValueToDomain_management(gdb, domWork2, code, domDictwork2[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domWork2, "CODE", "ASCENDING")     

domDictwork3 = {"PHC,_Air": "PHC, Air Spade",\
                "PHC,_Inject": "PHC, Inject",\
                "Prune_": "Prune",\
                "Release_": "Release",\
                "Remove_": "Remove",\
                "Stump_Grind": "Stump Grind",}

for code in domDictwork3:
        
        arcpy.AddCodedValueToDomain_management(gdb, domWork3, code, domDictwork3[code])
        
        arcpy.SortCodedValueDomain_management(gdb, domWork3, "CODE", "ASCENDING")                             

# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
time.sleep(5)

#Add Fields to Feature Class
arcpy.AddField_management(inFeatures, Field_Tree, "LONG", field_length=field_length,)
arcpy.AddField_management(inFeatures, Field_TreeName, "TEXT", field_length=Field_Name_Length,)
arcpy.AddField_management(inFeatures, Field_NameSpec, "TEXT", field_length=Field_Name_Length,) 
arcpy.AddField_management(inFeatures, Field_DBH, "FLOAT", field_length=field_length,)                      
arcpy.AddField_management(inFeatures, Field_Arb, "TEXT", field_length=field_length,)  
arcpy.AddField_management(inFeatures, Field_Bark, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, Field_Condition, "Text", field_length=field_length,)
arcpy.AddField_management(inFeatures, Field_Cavity, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, Field_Mast, "TEXT", field_length=Notes_Length,)
arcpy.AddField_management(inFeatures, Field_Growing, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldMajor1, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldMajor2, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldMajor3, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldMod1, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldMod2, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldMod3, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldMin1, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldMin2, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldMin3, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldPatho1, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldPatho2, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldPatho3, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldWork1, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldWork2, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, FieldWork3, "TEXT", field_length=field_length,)
arcpy.AddField_management(inFeatures, Field_Notes, "TEXT", field_length=Notes_Length,)

time.sleep(5)

#assign domain to field 
#arcpy.AssignDomainToField_management(inFeatures, inField, domName)
#arcpy.AssignDomainToField_management(inFeatures, Field_Name01, domName01)
arcpy.AssignDomainToField_management(inFeatures, Field_TreeName, domTreeName)
arcpy.AssignDomainToField_management(inFeatures, Field_Arb, domNameArb)
arcpy.AssignDomainToField_management(inFeatures, Field_Bark, domNameBark)
arcpy.AssignDomainToField_management(inFeatures, Field_Condition, domNameCondition)
arcpy.AssignDomainToField_management(inFeatures, Field_Cavity, domnameCavity)
arcpy.AssignDomainToField_management(inFeatures, Field_Mast, domNameMast)
arcpy.AssignDomainToField_management(inFeatures, Field_Growing, domNameGrowing)
arcpy.AssignDomainToField_management(inFeatures, FieldMajor1, domNameMajor1)
arcpy.AssignDomainToField_management(inFeatures, FieldMajor2, domNameMajor2)
arcpy.AssignDomainToField_management(inFeatures, FieldMajor3, domNameMajor3)
arcpy.AssignDomainToField_management(inFeatures, FieldMod1, domMod1)
arcpy.AssignDomainToField_management(inFeatures, FieldMod2, domMod2)
arcpy.AssignDomainToField_management(inFeatures, FieldMod3, domMod3)
arcpy.AssignDomainToField_management(inFeatures, FieldMin1, domMin1)
arcpy.AssignDomainToField_management(inFeatures, FieldMin2, domMin2)
arcpy.AssignDomainToField_management(inFeatures, FieldMin3, domMin3)
arcpy.AssignDomainToField_management(inFeatures, FieldPatho1, domPatho1)
arcpy.AssignDomainToField_management(inFeatures, FieldPatho2, domPatho2)
arcpy.AssignDomainToField_management(inFeatures, FieldPatho3, domPatho3)
arcpy.AssignDomainToField_management(inFeatures, FieldWork1, domWork1)
arcpy.AssignDomainToField_management(inFeatures, FieldWork2, domWork2)
arcpy.AssignDomainToField_management(inFeatures, FieldWork3, domWork3)

arcpy.EnableAttachments_management(inFeatures)