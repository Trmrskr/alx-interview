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
    keys_to_test = set(boxes[0]).difference(unlocked_boxes)

    while len(keys_to_test) > 0:
        key = keys_to_test.pop()

        if key <= 0 or key >= n:
            continue
        if key not in unlocked_boxes:
            keys_to_test = keys_to_test.union(boxes[key])
            unlocked_boxes.add(key)

    return n == len(unlocked_boxes)
