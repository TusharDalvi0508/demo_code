# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 23:23:42 2023

@author: Tushar_Dalvi
"""

def bounding_box_area(bbox):
    return (bbox[2] - bbox[0]) * (bbox[3] - bbox[1])

def bbox_intersection(bbox1, bbox2):

    # Calculate the overlapping region
    x1 = max(bbox1[0], bbox2[0])
    y1 = max(bbox1[1], bbox2[1])
    x2 = min(bbox1[2], bbox2[2])
    y2 = min(bbox1[3], bbox2[3])
    
    # Check if the boxes intersect
    if x1 < x2 and y1 < y2:
        return (x1, y1, x2, y2)
    else:
        return None

def bbox_common_area(bbox1, bbox2):

    intersection = bbox_intersection(bbox1, bbox2)
    if intersection is not None:
        return bounding_box_area(intersection)
    else:
        return 0
bbox1 = (0, 0, 10, 10)
bbox2 = (5, 5, 15, 15)
common_area = bbox_common_area(bbox1, bbox2)
print(common_area)