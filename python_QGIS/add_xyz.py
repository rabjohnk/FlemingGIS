params = "type=xyz&url=https://tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0"
layer = QgsRasterLayer(params,"OSM","wms")
QgsProject.instance().addMapLayer(layer,False)

layerTree=iface.layerTreeCanvasBridge().rootGroup()
layerTree.insertChildNode(-1,QgsLayerTreeLayer(layer))