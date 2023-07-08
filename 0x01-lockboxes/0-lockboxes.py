#!/usr/bin/python3
"""
This module contain the canUnlockAll function.
This function runs in n time O(n). That is why I love it.
"""


def canUnlockAll(boxes):
    """
      canUnlockAll - a function that determines if
      it can unlock all given boxes
      returns true if it can unlock all given boxes
    """

    n = len(boxes)

    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0]).difference(unlocked_boxes)

    while len(locked_boxes) > 0:
        boxId = locked_boxes.pop()

        if boxId <= 0 or boxId >= n:
            continue
        if boxId not in unlocked_boxes:
            locked_boxes = locked_boxes.union(boxes[boxId])
            unlocked_boxes.add(boxId)

    return n == len(unlocked_boxes)
