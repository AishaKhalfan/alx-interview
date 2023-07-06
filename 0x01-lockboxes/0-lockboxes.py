#!/usr/bin/python3
"""A module for lockboxes.
"""


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.
    '''
    n = len(boxes)
    opened_boxes = set([0])
    unopened_boxes = set(boxes[0]).difference(set([0]))
    while len(unopened_boxes) > 0:
        boxId = unopened_boxes.pop()
        if not boxId or boxId >= n or boxId < 0:
            continue
        if boxId not in opened_boxes:
            unopened_boxes = unopened_boxes.union(boxes[boxId])
            opened_boxes.add(boxId)
    return n == len(opened_boxes)
