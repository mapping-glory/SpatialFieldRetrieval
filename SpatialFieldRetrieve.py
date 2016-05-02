#-------------------------------------------------------------------------------
# Name:        Spatial Field Retrieval
# Purpose:      Retrieve a field from the source dataset and use it to populate
#               the target field. Honors selections.
# Author:      Andy Bradford
#
# Created:     25/02/2016
# Copyright:   (c) andy.bradford 2016
#-------------------------------------------------------------------------------

import arcpy
from arcpy import env
env.overwriteOutput = True

#parameters

#Layer to be calculated
InLayer = arcpy.GetParameterAsText(0)
#InField: Layer which will receive final data
InField = arcpy.GetParameterAsText(1)
#SourceLayer: Layer which contributes data.
SourceLayer = arcpy.GetParameterAsText(2)
#SourceField: source field
SourceField = arcpy.GetParameterAsText(3)
#SpatShip = spatial relationship - same as Spatial Join tool
SpatShip = arcpy.GetParameterAsText(4)
#MergeRule: How to handle one-to-many relationships
MergeRule = arcpy.GetParameterAsText(5)
#SearchDist: search distance
SearchDist = arcpy.GetParameterAsText(6)

#Create field map a la forrestchev
#thanks to forrestchev on GIS StackExchange
#this field mapping code sets up the Spatial Join code later
#to create an output with only the Target_FID and the source field.
ScratchFMS = arcpy.FieldMappings()
ScratchFMS.addTable(SourceLayer)
SourceIndex = ScratchFMS.findFieldMapIndex(SourceField)
SourceFM = ScratchFMS.getFieldMap(SourceIndex)
ScratchFMS = arcpy.FieldMappings()
SourceFM.addInputField(SourceLayer, SourceField)
SourceFM.mergeRule = MergeRule
ScratchFMS.addFieldMap(SourceFM)




#spatial join to scratch features
arcpy.SpatialJoin_analysis(InLayer, SourceLayer, "ScratchSJ", "JOIN_ONE_TO_ONE",
                          "KEEP_ALL", ScratchFMS, SpatShip, SearchDist)
arcpy.AddMessage("Spatial Join completed.")

#create dictionary object for join purposes.
#the key will be the Target FID, and the value is the target field value.
JoinDict = {}
with arcpy.da.SearchCursor("ScratchSJ", ("TARGET_FID", SourceField)) as cursor:
    for row in cursor:
        fid = row[0]
        val = row[1]
        JoinDict[fid] = val

arcpy.AddMessage("Dictionary created.")

#Update cursor, hinges on dictionary
with arcpy.da.UpdateCursor(InLayer, ("OID@", InField)) as cursor:
    #reach into dictionary using FID values
    for row in cursor:
        #Search for dictionary item with feature's FID as key
        val = JoinDict[row[0]]
        row[1] = val
        cursor.updateRow(row)

#delete ScratchSJ file.
arcpy.Delete_management("ScratchSJ")

