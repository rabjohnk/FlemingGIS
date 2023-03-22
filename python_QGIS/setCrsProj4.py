proj4 = "+proj=utm +zone=17 +ellps=GRS80 +datum=NAD83 +units=m +no_defs"
crs = QgsCoordinateReferenceSystem()
crs.createFromProj4(proj4)
QgsProject.instance().setCrs(crs)