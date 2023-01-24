import ogr

ds = ogr.get_project('south-fed-district-latest.osm')
layer = ds.GetLayer(1) # layer 1 for ways

nameList = []
for feature in layer:
    if feature.GetField("highway") != None: 
        name = feature.GetField("name")
        if name != None and name not in nameList: 
            nameList.append(name)

print(nameList)