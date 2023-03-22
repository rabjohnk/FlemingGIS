myInstance = QgsProject.instance()

road_layer = myInstance.mapLayersByName('ROAD_CENTERLINES')[0]

root = myInstance.layerTreeRoot()

myLayer=root.findLayer(road_layer.id())


QgsLayerDefinition().exportLayerDefinition("H:\\FlemingGIS\\python_QGIS\\test.qlr",[myLayer])