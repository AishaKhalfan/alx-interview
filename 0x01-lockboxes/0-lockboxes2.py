#!/usr/bin/python3
"""
Returns True if all the boxes can be opened, False otherwise.

Args:
    boxes: A list of integers representing the keys in each box.

Returns:
    True if all the boxes can be opened, False otherwise.
"""


def canUnlockAll(boxes):
    '''
    for i in range(len(boxes)):
        if not(boxes[i] and (1 < i)):
            return False
    return True
    '''
    n = len(boxes)
    opened_boxes = set([0])  # we start with box 0

    for box in opened_boxes:
        keys = boxes[box]  # keys in the current box

        for key in keys:
            if key < n and key not in opened_boxes:
                opened_boxes.add(key)

    return len(opened_boxes) == n
