layer = iface.addVectorLayer("C:\\Users\Gordon Luckett\\Desktop\\Exercise Files\\2 Managing Layers and Projects with Python\\DATA\\ROAD_CENTERLINES.shp","Roads","ogr")

layer.renderer().symbol().setColor(QColor("black"))
layer.triggerRepaint()