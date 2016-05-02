# SpatialFieldRetrieval
ArcGIS script to retrieve field data based on spatial relationship.

Dependencies: ArcPy, ArcGIS license

This tool is intended to be used as an ArcGIS Toolbox script in ArcMap. Given two layers, a source and destination field, and a spatial relationship, it retrieves values from the field in the source data and deposits it in the field in the target dataset. This is intended to replace a cycle of Spatial Join - Field Join - Field Calculate - Delete Field.

Setup

Save the script SpatialFieldRetrieval.py to your computer, and add it to ArcToolbox as a Script.

Set Parameters, in this order. All parameters are Required and Input except for Search Distance.
    Input_Layer - Feature Layer
    Input_Field - Field, Obtained from Input_Layer
    Source_Layer - Feature Layer
    Source_Field - Field, Obtained from Source_Layer
    Spatial Relationship - String
        Value List:
        INTERSECT
        INTERSECT_3D
        WITHIN_A_DISTANCE
        WITHIN_A_DISTANCE_GEODESIC
        CONTAINS
        COMPLETELY CONTAINS
        CONTAINS_CLEMENTINI
        WITHIN
        COMPLETELY_WITHIN
        WITHIN_CLEMENTINI
        ARE_IDENTICAL_TO
        BOUNDARY_TOUCHES
        SHARE_A_LINE_SEGMENT_WITH
        CROSSED_BY_THE_OUTLINE_OF
        HAVE_THEIR_CENTER_IN
        CLOSEST
        CLOSEST_GEODESIC
    Merge Rule - String
        Value List:
        FIRST
        LAST
        JOIN
        SUM
        MEAN
        MEDIAN
        MODE
        MIN
        MAX
        STDEV
        COUNT
    Search Distance - Linear Unit


