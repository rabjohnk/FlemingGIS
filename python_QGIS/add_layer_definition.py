instance = QgsProject.instance()
root_group = QgsProject.instance().layerTreeRoot()
layer = 'C:\\Users\\Gordon Luckett\\Desktop\\Exercise Files\\2 Managing Layers and Projects with Python\\DATA\\EASEMENTS.qlr'

QgsLayerDefinition().loadLayerDefinition(layer, instance,root_group)
