#!/usr/bin/python3
"""
  canUnlockAll - looks through a list of boxes and returns true
  if it got the key to unlock all or return false if it didn't
  get the key to unlock at least one.
"""


def canUnlockAll(boxes):
    """
      The namespace of the canUnlockAll function
    """

    box_length = len(boxes)
    found = False
    for i in range(1, box_length):
        found = False
        for j in range(0, box_length):
            if boxes[i] != boxes[j]:
                if i in boxes[j]:
                    found = True
                    continue
        if found is False:
            return False

    return True
