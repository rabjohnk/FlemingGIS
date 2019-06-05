# -*- coding: utf-8 -*-


#Import system modules
import arcpy

try:
# Set the workspace (to avoid having to type in the full path to the data        every time)
    arcpy.env.workspace = "h:/data"

    #I want to make a change to this

# Set local parameters
    domName = "Species"
    gdb = "Campus_Tree.gdb"

# Process: Create the coded value domain
#arcpy.CreateDomain_management("UPDM.gdb", domName, "Gas Systems", "TEXT", "CODED")

# Store all the domain values in a dictionary with the domain code as the  "key" and the
# domain description as the "value" (domDict[code])
    domDict = {"Cercis_canadensis": "Cercis canadensis", \
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

# Process: Add valid material types to the domain
# use a for loop to cycle through all the domain codes in the dictionary
    for code in domDict:
        arcpy.AddCodedValueToDomain_management(gdb, domName, code, domDict[code])

except Exception as err:
            print(err.args[0])

